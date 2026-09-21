# Hugo → 知乎草稿

保留正文、公式源码和图片字节。不会改写推导，不会公开发布，不读取登录凭证。

## 导出

需要 Node.js 20+。在仓库根目录执行：

```sh
npm ci --prefix tools/zhihu_export
node tools/zhihu_export/export.mjs content/plasma-physics/magnetic-mirror-reflection-force/index.md --title '从磁场散度为零到磁镜力：一个完整的近轴推导'
```

其他文章更换路径、标题即可。默认输出 `.zhihu-export/<文章目录名>/`：

- `preview.html`：离线 KaTeX 校验预览，不能直接复制 KaTeX DOM 到知乎。
- `clipboard.html`：富文本载荷；公式是知乎识别的 `ee_img`，不是美元符号源码。
- `manifest.json`：逐个公式原文、SHA256、模式、图片哈希、标题层级和来源 commit。
- `images/`：逐字节复制的原图。
- `source.md`：原文审计快照。
- `title.txt`：标题。

目前支持 YAML front matter、普通 Markdown、`$...$`、`$$...$$`、`\(...\)`、`\[...\]` 和博客的 `math-display` 外层 div。遇到其他 HTML、shortcode、自定义 Hugo 路由会停止，避免悄悄丢正文。标题内公式、强调和图注内公式保留。中断的有序列表转换为带显式数字的段落，避免知乎忽略 `ol[start]` 后重置编号。图注保留为图片之后的普通斜体段落，支持其中的公式。

## 上传与草稿

使用现有登录的浏览器，通过知乎图片上传控件上传 `manifest.images` 对应原始文件，顺序与 manifest 相同。点击文字上方的方框，再点“插入图片”。PNG 和 WebP 均已在当前编辑器实测上传成功。

读取上传后图片 DOM 的地址，仅保存在本地 `image-map.local.json`，键为原文件名，值为知乎生成的图址。**草稿图址可能是带短期签名的 pic-private.zhihu.com URL，禁止 commit 或公开分享，禁止把它当永久图床。**

```sh
node tools/zhihu_export/export.mjs content/plasma-physics/magnetic-mirror-reflection-force/index.md --title '从磁场散度为零到磁镜力：一个完整的近轴推导' --image-map .zhihu-export/magnetic-mirror-reflection-force/image-map.local.json
```

将 `clipboard.html` 作为 `text/html` 写入浏览器剪贴板，粘贴到正文编辑器。不能粘贴 HTML 源码文本。`browser-workflow.mjs` 提供可复用的已登录 Browser Tab 适配器：`uploadOriginalImages`、`pasteDraft`、`collectAudit`、`verifyAudit`。它使用浏览器正常 UI，不调用未公开写作 API；需要宿主提供 Browser Tab，不是独立 CLI 登录工具。UI 改版时应先检查控件，上传框定位失败会停止。

粘贴后必须滚动全文触发知乎懒加载：未进入视区的公式会暂时显示占位源码。`verifyAudit` 不会把数量匹配当作渲染成功；它核对每个公式的源码、行内/块级模式、SVG 渲染、错误、宽度、标题层级、图片数量及正文链接。正文完整性还需比较 `clipboard.html` 去标签后的文字与草稿的 `data-text` 内容（忽略排版空白）；图片顺序需结合图像哈希/尺寸和视觉核对。

等待“草稿”保存标记，重新打开，再检查公式与图片。最后只停在草稿，由作者手动发布。

## 文末说明

磁镜文章默认添加本次指定的学习说明；其他文章默认只添加来源链接。导出其他主题时使用 `--footer <UTF-8文本文件>` 提供相应结语；标题默认读取 front matter。结语仅影响新增尾注，不改变原文。

## 认证与隐私

不存用户名、密码、Cookie、Token。所有生成物和本地映射均被 `.gitignore` 排除。不要把浏览器 profile 或 `.env` 提交到仓库。公开提交只包含工具、依赖锁文件和不带签名的验收报告。
