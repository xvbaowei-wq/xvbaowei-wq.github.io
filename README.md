# 轨迹与场 · Trajectories & Fields

个人研究主页与长期知识库，使用 Hugo、PaperMod 与 GitHub Pages 构建。

## 本地预览

```bash
git clone --recurse-submodules https://github.com/xvbaowei-wq/xvbaowei-wq.github.io.git
cd xvbaowei-wq.github.io
hugo server -D
```

浏览器打开 <http://localhost:1313>。

## 新增文章

```bash
hugo new plasma-physics/example.md
```

编辑生成的 Markdown 文件，将头部的 `draft: true` 改为 `draft: false`，然后提交并推送：

```bash
git add .
git commit -m "content: add new article"
git push
```

推送到 `main` 后，GitHub Actions 会自动构建并部署网站。

## 内容目录

- `content/plasma-physics/`：等离子体物理
- `content/fusion/`：核聚变
- `content/magnetic-nozzle/`：磁喷管
- `content/robotics/`：机器人
- `content/mathematics/`：数学
- `content/notes/`：学习笔记
