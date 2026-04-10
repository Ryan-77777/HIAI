# HiAI 组件规范平台

> AI 驱动的 UI 组件设计规范可视化平台，涵盖「智能摘要」「表单推荐」「AI 输入框」三大组件的 Token 管理、Design Skill 文档生成与沙盒验证。

---

## 目录结构

```
smart-summary/
├── index.html              # 主应用（所有组件、逻辑、Token、Design Skill）
├── vendor/                 # 本地离线依赖（React / Tailwind / Babel / Marked）
│   ├── react18.production.min.js
│   ├── react-dom18.production.min.js
│   ├── tailwindcss.js
│   ├── babel.min.js
│   └── marked.min.js
├── ai-input-assets/        # AI 输入框图标资源（SVG + PNG）
├── icon-library/           # 图标库数据（JSON）
├── icon-library-data.json  # 图标库总数据
├── DESIGN_SKILL.md         # 智能摘要 Design Skill 参考文档
├── DESIGN_SKILL_AI_INPUT.md
├── DESIGN_SKILL_FORM_RECOMMEND.md
├── CONTRIBUTING.md         # 贡献指南（必读）
└── README.md               # 本文件
```

---

## 快速上手

### 方式 A — 本地开发（推荐）

```bash
# 1. 克隆仓库
git clone <仓库地址>
cd smart-summary

# 2. 启动本地服务
python3 -m http.server 5174

# 3. 浏览器访问
open http://127.0.0.1:5174/index.html
```

### 方式 B — 直接打开

将整个目录复制到本地，用浏览器直接打开 `index.html`（部分功能需起服务才可正常使用）。

### 方式 C — 在线预览（Vercel）

访问 [线上预览地址](https://hiaidesign.vercel.app/) — 无需本地配置，直接打开即用。

---

## 功能模块

| 模块 | 说明 |
|------|------|
| **网页组件预览** | 实时渲染当前 Token 参数下的组件 UI |
| **Token 配置面板** | 可视化编辑所有设计变量（颜色 / 字号 / 间距 / 圆角 / 渐变） |
| **Design Skill 文档** | 自动从 Token 生成完整的 AI 可读设计规范 Markdown |
| **沙盒测试** | 模拟外部 LLM 阅读 Design Skill 后生成 UI，并进行参数校验 |

---

## 技术栈

| 依赖 | 版本 | 加载方式 |
|------|------|---------|
| React | 18 | 本地 vendor |
| ReactDOM | 18 | 本地 vendor |
| Tailwind CSS | 3 | 本地 vendor |
| Babel Standalone | — | 本地 vendor（浏览器编译 JSX） |
| Marked.js | — | 本地 vendor（Markdown 渲染） |

> 所有依赖均打包在 `vendor/` 目录，**无需联网、无需 npm install**。

---

## 组件列表

| 组件 | 说明 | 文件位置 |
|------|------|---------|
| `SmartSummaryCard` | 智能摘要卡片 | `index.html` |
| `FormRecommend` | 表单 AI 推荐 | `index.html` |
| `AiInputBox` | AI 输入框 | `index.html` |
| `TokensPanel` | Token 配置面板 | `index.html` |
| `SandboxModal` | 沙盒测试弹窗 | `index.html` |
| `IconLibraryView` | 图标库浏览 | `index.html` |

---

## 贡献

请阅读 [CONTRIBUTING.md](./CONTRIBUTING.md) 了解完整的贡献流程和编码规范。
