#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';
import MarkdownIt from 'markdown-it';
import katex from 'katex';
import YAML from 'yaml';

const args=process.argv.slice(2), input=args.shift();
if(!input){console.error('node tools/zhihu_export/export.mjs <article.md> [--title TITLE] [--image-map map.json] [--out DIR] [--footer FILE]');process.exit(1);}
const opts={}; while(args.length){const k=args.shift();if(!['--title','--image-map','--out','--footer'].includes(k)||!args.length)throw Error('Unknown/missing option: '+k);opts[k]=args.shift();}
const file=path.resolve(input), root=execFileSync('git',['-C',path.dirname(file),'rev-parse','--show-toplevel'],{encoding:'utf8'}).trim();
const source=fs.readFileSync(file,'utf8');
const fm=source.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n/);if(!fm)throw Error('YAML front matter required');
const meta=YAML.parse(fm[1]),config=YAML.parse(fs.readFileSync(path.join(root,'hugo.yaml'),'utf8'));
if(!config.baseURL)throw Error('Missing baseURL');
if(config.permalinks||config.uglyURLs||config.languages)throw Error('Custom Hugo routing requires explicit support; refusing to guess URL');
let rel=path.relative(path.join(root,'content'),file).replaceAll(path.sep,'/');if(rel.startsWith('..'))throw Error('Article outside content');
let route=rel.replace(/(?:\/index)?\.md$/,'/');if(meta.slug)route=route.replace(/[^/]+\/$/,meta.slug+'/');
const blogURL=new URL(meta.url||route,config.baseURL).href;
const title=opts['--title']||meta.title;
let body=source.slice(fm[0].length).replace(/^[ \t]*<div class="math-display">\s*$/gm,'').replace(/^[ \t]*<\/div>\s*$/gm,'');
if(/{{[<%]/.test(body))throw Error('Unrecognised Hugo shortcode: convert explicitly, never silently drop content');
const out=path.resolve(opts['--out']||path.join(root,'.zhihu-export',path.basename(path.dirname(file))));fs.mkdirSync(out,{recursive:true});
const imageMap=opts['--image-map']?JSON.parse(fs.readFileSync(opts['--image-map'],'utf8')):{};
const formulas=[],pictures=[],warnings=[];
const esc=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const md=new MarkdownIt({html:true,typographer:false,breaks:false});
md.inline.ruler.before('escape','math_inline',(state,silent)=>{
 const start=state.pos,delim=state.src.startsWith('\\(',start)?'\\(':(state.src[start]==='$'&&!state.src.startsWith('$$',start)?'$':null);if(!delim)return false;
 const close=delim==='\\('? '\\)': '$';let end=start+delim.length;
 while((end=state.src.indexOf(close,end))>=0){let n=0;for(let j=end-1;j>=0&&state.src[j]==='\\';j--)n++;if(n%2===0)break;end+=close.length;}
 if(end<0)throw Error('Unclosed inline math at '+start);
 if(!silent){const t=state.push('math_inline','',0);t.content=state.src.slice(start+delim.length,end);}
 state.pos=end+close.length;return true;
});
md.block.ruler.before('fence','math_block',(state,start,end,silent)=>{
 const pos=state.bMarks[start]+state.tShift[start],line=state.src.slice(pos,state.eMarks[start]);let open,close;
 if(line.startsWith('$$')){open='$$';close='$$';}else if(line.startsWith('\\[')){open='\\[';close='\\]';}else return false;
 let stop=state.src.indexOf(close,pos+open.length);if(stop<0)throw Error('Unclosed display math');
 let last=start;while(last<end&&state.eMarks[last]<stop+close.length)last++;
 if(state.src.slice(stop+close.length,state.eMarks[last]).trim())throw Error('Text after block math delimiter');
 if(!silent){const t=state.push('math_block','',0);t.block=true;t.content=state.src.slice(pos+open.length,stop);t.map=[start,last+1];}
 state.line=last+1;return true;
},{alt:['paragraph','reference','blockquote','list']});
const tokens=md.parse(body,{});
function visit(ts,fn){for(const t of ts){fn(t);if(t.children)visit(t.children,fn);}}
visit(tokens,t=>{
 if(t.type==='html_block'||t.type==='html_inline')throw Error('Unsupported raw HTML: '+t.content.slice(0,100));
 if(t.type==='math_inline'||t.type==='math_block'){
  const f={id:formulas.length+1,kind:t.type==='math_block'?'block':'inline',tex:t.content,sha256:hash(t.content),aligned:(t.content.match(/\\begin\{aligned\}/g)||[]).length};
  try{katex.renderToString(f.tex,{displayMode:f.kind==='block',throwOnError:true,strict:'ignore',trust:false});}catch(e){throw Error('Formula '+f.id+' failed: '+e.message);}
  formulas.push(f);t.meta={formula:f};
 }
 if(t.type==='image'){
  const src=t.attrGet('src');if(/^[a-z]+:|^\//i.test(src))throw Error('Image must be a local article asset: '+src);
  const local=path.resolve(path.dirname(file),decodeURIComponent(src));if(!local.startsWith(path.dirname(file)+path.sep))throw Error('Image outside article directory');
  const data=fs.readFileSync(local),dest='images/'+path.basename(local);fs.mkdirSync(path.join(out,'images'),{recursive:true});fs.copyFileSync(local,path.join(out,dest));
  if(imageMap[src]&&!/^https:\/\/(?:[^/]*\.zhimg\.com|pic-private\.zhihu\.com)\//.test(imageMap[src]))throw Error('Image map must use uploaded zhimg.com assets');
  const p={index:pictures.length+1,source:src,alt:t.content,sha256:hash(data),bytes:data.length,local:dest,url:imageMap[src]||null};pictures.push(p);t.meta={picture:p};
 }
});
let mode='native';
function math(t){const f=t.meta.formula;if(mode==='preview')return '<span data-formula="'+f.id+'">'+katex.renderToString(f.tex,{displayMode:f.kind==='block',throwOnError:true,strict:'ignore',trust:false})+'</span>';
 return '<img class="ee_img tr_noresize" eeimg="'+(f.kind==='block'?2:1)+'" src="https://www.zhihu.com/equation?tex='+encodeURIComponent(f.tex)+'" alt="'+esc(f.tex)+'">';}
md.renderer.rules.math_inline=(ts,i)=>math(ts[i]);md.renderer.rules.math_block=(ts,i)=>'<p>'+math(ts[i])+'</p>\n';
md.renderer.rules.image=(ts,i)=>{const p=ts[i].meta.picture;return '<img src="'+esc(mode==='preview'?p.local:(p.url||p.local))+'" alt="'+esc(p.alt)+'">';};
// Zhihu ignores ol[start]; preserve visible step numbers explicitly, including interrupted lists.
const stack=[];
md.renderer.rules.ordered_list_open=(ts,i)=>{stack.push({ordered:true,next:Number(ts[i].attrGet('start')||1)});return '';};
md.renderer.rules.ordered_list_close=()=>{stack.pop();return '';};
md.renderer.rules.bullet_list_open=()=>{stack.push({ordered:false});return '<ul>\n';};
md.renderer.rules.bullet_list_close=()=>{stack.pop();return '</ul>\n';};
md.renderer.rules.list_item_open=()=>stack.at(-1)?.ordered?'<p>'+(stack.at(-1).next++)+'. ':'<li>';
md.renderer.rules.list_item_close=()=>stack.at(-1)?.ordered?'</p>\n':'</li>\n';
const originalNative=md.renderer.render(tokens,md.options,{});
let footer='<hr><p>本文是我在学习等离子体物理过程中整理的一次完整推导。相比直接记住<br>F_parallel = -mu nabla_parallel B，<br>我更希望把这个公式从哪里来、每一步用了什么近似记录清楚。</p><p>长期修订版本收录于个人研究笔记：<br>轨迹与场 / Trajectories &amp; Fields</p><p><a href="'+esc(blogURL)+'">'+esc(blogURL)+'</a></p>';
if(opts['--footer']){footer='<hr>'+fs.readFileSync(opts['--footer'],'utf8').split(/\n\s*\n/).map(p=>'<p>'+esc(p).replaceAll('\n','<br>')+'</p>').join('')+'<p><a href="'+esc(blogURL)+'">'+esc(blogURL)+'</a></p>';}else if(!file.endsWith('/magnetic-mirror-reflection-force/index.md')){footer='<hr><p>长期修订版本收录于个人研究笔记：轨迹与场 / Trajectories &amp; Fields</p><p><a href="'+esc(blogURL)+'">'+esc(blogURL)+'</a></p>';}
const native=originalNative+footer;
mode='preview';const preview=md.renderer.render(tokens,md.options,{})+footer;
const katexDist=path.join(path.dirname(new URL(import.meta.url).pathname),'node_modules/katex/dist');fs.cpSync(katexDist,path.join(out,'katex'),{recursive:true});
fs.writeFileSync(path.join(out,'clipboard.html'),native);
fs.writeFileSync(path.join(out,'preview.html'),'<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>'+esc(title)+'</title><link rel="stylesheet" href="katex/katex.min.css"><style>body{max-width:900px;margin:40px auto;padding:0 24px;font:18px/1.8 sans-serif;color:#222}img{max-width:100%}.katex-display{overflow:auto;padding:8px 0}h2{margin-top:2em}p{margin:1em 0}blockquote{border-left:3px solid #bbb;padding-left:18px}</style><h1>'+esc(title)+'</h1><article>'+preview+'</article></html>');
fs.writeFileSync(path.join(out,'title.txt'),title);
const manifest={title,blogURL,source:path.relative(root,file),sourceCommit:execFileSync('git',['-C',root,'rev-parse','HEAD'],{encoding:'utf8'}).trim(),sourceSHA256:hash(source),counts:{inline:formulas.filter(f=>f.kind==='inline').length,block:formulas.filter(f=>f.kind==='block').length,aligned:formulas.reduce((n,f)=>n+f.aligned,0),images:pictures.length},formulas,images:pictures,headings:tokens.filter(t=>t.type==='heading_open').map(t=>t.tag),warnings,localCompileErrors:[],zhihuVerified:false,readyForPaste:pictures.every(p=>p.url)};
fs.writeFileSync(path.join(out,'manifest.json'),JSON.stringify(manifest,null,2));
// Plain source retained solely for auditing, never to be pasted as the final article.
fs.writeFileSync(path.join(out,'source.md'),source);
console.log(JSON.stringify({out,title,blogURL,counts:manifest.counts,readyForPaste:manifest.readyForPaste},null,2));
