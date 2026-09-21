/** Browser-client adapter. Call only with an authenticated Zhihu editor Tab.
 * UI only; no cookies, internal APIs, React state or publish action.
 * File paths must be visible to the browser. Always inspect current UI first.
 */
export async function uploadOriginalImages(tab, files) {
  await tab.playwright.getByRole('button',{name:'图片',exact:true}).click();
  const label=tab.playwright.getByText('本地图片上传',{exact:true});
  const r=await label.evaluate(e=>e.getBoundingClientRect().toJSON());
  // 2026-09-21 UI: the outlined upload square is above the label.
  // Clicking the label itself does not open the chooser.
  const pending=tab.playwright.waitForEvent('filechooser',{timeoutMs:10000}).catch(error=>({error}));
  await tab.cua.click({x:r.x+r.width/2,y:r.y-70});
  const chooser=await pending;if(chooser.error)throw chooser.error;
  if(files.length>1&&!chooser.isMultiple())throw Error('Multiple upload is unavailable');
  await chooser.setFiles(files);
  await tab.playwright.getByRole('button',{name:'插入图片',exact:true}).click();
}
export async function pasteDraft(tab,{title,html}) {
  if(!html||!title)throw Error('Missing title or HTML');
  await tab.playwright.getByPlaceholder('请输入标题（最多 100 个字）').fill(title);
  await tab.clipboard.write([{entries:[{mimeType:'text/html',text:html}]}]);
  const first=tab.playwright.locator('.public-DraftEditor-content [data-text="true"]').first();
  if(await first.count())await first.click();else await tab.playwright.locator('.public-DraftEditor-content').click();
  await tab.cua.keypress({keys:['Control','a']});
  await tab.cua.keypress({keys:['Backspace']});
  await tab.cua.keypress({keys:['Control','v']});
}
export async function collectAudit(tab) {
  return tab.playwright.locator('.public-DraftEditor-content').evaluate(e=>({
    formulas:[...e.querySelectorAll('[data-tex]')].map(x=>({tex:x.getAttribute('data-tex'),mode:x.getAttribute('data-eeimg'),rendered:!!x.querySelector('svg'),error:!!x.querySelector('.MathJax_Error'),width:x.querySelector('svg')?.getBoundingClientRect().width,container:e.clientWidth})),
    images:[...e.querySelectorAll('img')].map(x=>({width:x.naturalWidth,height:x.naturalHeight,complete:x.complete,id:x.getAttribute('src')?.match(/v2-[a-f0-9]+/)?.[0]})),
    headings:[...e.querySelectorAll('h2,h3')].map(x=>x.tagName.toLowerCase()),
    text:[...e.querySelectorAll('[data-text="true"]')].map(x=>x.textContent).join('\n'),
    links:[...e.querySelectorAll('a[href]')].map(x=>x.getAttribute('href'))
  }));
}
export function verifyAudit(manifest,audit) {
  const errors=[];
  if(audit.formulas.length!==manifest.formulas.length)errors.push('Formula count mismatch');
  manifest.formulas.forEach((f,i)=>{const got=audit.formulas[i];if(!got||got.tex!==f.tex||got.mode!==(f.kind==='block'?'2':'1'))errors.push('Formula source/mode mismatch: '+f.id);if(!got?.rendered||got.error)errors.push('Formula not rendered: '+f.id);if(got?.width>got?.container)errors.push('Formula overflow: '+f.id);});
  if(audit.images.length!==manifest.images.length||audit.images.some(i=>!i.complete||!i.width))errors.push('Image loading/count error');
  if(JSON.stringify(audit.headings)!==JSON.stringify(manifest.headings))errors.push('Heading hierarchy changed');
  if(!audit.links.includes(manifest.blogURL))errors.push('Source link missing');
  return {passed:!errors.length,errors,counts:manifest.counts};
}
