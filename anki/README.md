# Anki Multi-Card Review

单网页 Anki 复习工具，通过 Anki-Connect 插件与本地 Anki 交互，支持一次同时复习 6 张卡片。

**功能：**
- 连接本地 Anki（需安装 [Anki-Connect](https://ankiweb.net/shared/info/2055492159) 插件）
- 随机抽取 6 张待学卡片，3×2 网格布局
- 键盘 `1-6` / `qweasd` 或鼠标点击切换卡片状态：Front → Good → Again
- Enter 一键揭示全部答案，再次 Enter 提交评分并刷新下一轮
- 右侧帮助面板（中英文切换、折叠）

**部署：**

```bash
git clone https://github.com/madokast/anki-batch.git
cd anki-batch
# 直接浏览器打开 index.html，或
python -m http.server 8080
```

**GitHub Pages：**

1. Fork 或推送到你自己的仓库
2. Settings → Pages → Source 选 main 分支，目录 `/ (root)`，Save
3. 访问 `https://madokast.github.io/anki-batch/`

**依赖：**

- Anki 需在后台运行，并安装 Anki-Connect 插件（插件 ID: 2055492159）
- Anki-Connect 配置中建议设置 `apiKey` 并修改 `webBindAddress` 为 `0.0.0.0`（如需跨设备访问）
