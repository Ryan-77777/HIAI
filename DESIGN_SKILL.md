# DESIGN_SKILL — 智能摘要组件面板（HiAI）

> 目的：让任何 AI 在生成涉及“智能摘要组件面板/服务摘要/SmartSummaryCard”的网页 UI 时，做到 **像素级一致**。  
> 本文件为强约束规范；**不得自行发挥**。

---

## 0.1 文案生成原则（重要：文案非固定）

- **所有组件的文案/示例内容必须视为动态内容**：应根据当前网页主题、业务场景与组件上下文实时生成或由业务数据驱动。
- **严禁把示例文案当成固定规范**：示例仅用于演示布局与信息密度。
- **固定不变的只有**：组件的交互能力、状态机与视觉样式框架（字号/间距/颜色/圆角/渐变/动效等）。

---

## 0) 组件触发规则（最重要）

只要用户需求、页面信息架构、或现有 UI 中出现以下任意关键词，就必须使用本规范：

- `智能摘要` / `摘要面板` / `服务摘要` / `服务总结` / `工单摘要` / `SmartSummaryCard`

命中后必须满足：

- **宽度**：必须自适应撑满容器区域（`width: 100%`）。容器自身决定最终宽度。
- **高度**：随内容自适应撑高（禁止固定高度；仅允许 skeleton 用 `min-height`）
- **不允许**换皮肤、换圆角、换间距、换字号、换配色。

---

## 1) Visual Theme & Atmosphere（视觉主题）

- **风格关键词**：干净、克制、轻量、信息密度中等、可信赖
- **表面策略**：白底为主，带轻描边；允许少量低饱和渐变做“智能感”提示
- **动效策略**：仅用于 loading 骨架（shimmer）；禁止额外动效

---

## 2) Color Palette & Roles（颜色角色）

| Role | Value | Usage |
| --- | --- | --- |
| Primary / Focus | `#1aa38a` | 图标主色、focus ring |
| Text Main | `#222727` | 标题/正文主文字 |
| Text Sub | `rgba(34,39,39,0.6)` | 更新时间/说明/空态文案 |
| Border (Outer) | `rgba(34,39,39,0.09)` | 外层卡片描边 |
| Hover Fill | `rgba(83,96,143,0.07)` | 可点击元素 hover 背景 |
| Icon Neutral | `rgba(34,39,39,0.75)` | 折叠按钮图标颜色 |

### Tag Tones（固定三套，不得新增）

| Tone | Background | Foreground |
| --- | --- | --- |
| Pink | `rgba(233,30,99,0.15)` | `#8c0f3d` |
| Teal | `rgba(0,179,161,0.15)` | `#015a58` |
| Violet | `rgba(106,58,199,0.15)` | `#331c77` |

### Gradient Background（必须按顺序叠加 + 随高度自适应）

- 高度阈值：`200px`
- 当高度 < 阈值：第一层白色渐变 stop = `40%`
- 当高度 >= 阈值：第一层白色渐变 stop = `20%`

```css
background-image:
  linear-gradient(180deg, rgba(255,255,255,0) 0%, #ffffff <AUTO_STOP>%),
  linear-gradient(30.9916862265deg, rgba(63,226,213,0.10) 0%, rgba(64,147,224,0.10) 37.358%, rgba(122,97,250,0.10) 69.65%, rgba(214,130,235,0.10) 100%),
  linear-gradient(90deg, #ffffff 0%, #ffffff 100%);
```

---

## 3) Typography Rules（字体与层级）

- **Font family**：`"PingFang SC", "PingFangSC", -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif`

| Level | Size | Line-height | Weight | Color | Usage |
| --- | --- | --- | --- | --- | --- |
| Title (Header) | `12px` | `16px` | `600` | `#222727` | 顶部标题（单行省略） |
| Body | `12px` | `16px` | `400` | `#222727` | 摘要正文段落 |
| Meta | `12px` | `16px` | `400` | `rgba(34,39,39,0.6)` | 更新时间/说明文案 |

文本规则（强制）：

- 标题 **必须** 单行省略（ellipsis）
- 正文段落间距 **必须** `4px`

---

## 4) Component Stylings（组件样式，强制骨架）

### 4.1 Outer Card（外层容器）

- `width`: `100%`（必须，撑满父容器）
- `border-radius`: `12px`（必须）
- `padding`: `12px`（必须）
- `gap`: `12px`（必须）
- `border`: `1px solid rgba(34,39,39,0.09)`

### 4.2 Header（顶部区域）

- Header padding：`8px 4px`（左右/上下）
- Header gap：`8px`

#### Header Left Logo（强制使用你的 Logo 资产）

**硬性约束（零容忍）**：

- **必须使用本项目内置图片**作为左上角 logo：`./summary-icon.png`
- **禁止**用任意 SVG/emoji/iconfont/第三方图标库替代（即使看起来相似也不允许）
- **禁止**改色、描边、加滤镜、加阴影、加圆角遮罩（除非设计稿明确要求）。必须保持图片原样呈现
- **尺寸固定**：`16x16px`（必须）
- **渲染方式**：必须使用 `<img>`（或等价图片组件）渲染，并确保资源可被打包/部署访问

实现参考（必须遵循，不得改结构）：

```html
<img src="./summary-icon.png" alt="" aria-hidden="true" width="16" height="16" />
```

#### Header Right Collapse Icon（必须为常规箭头）

- **图标**：chevron-up（常规箭头样式）
- **尺寸**：`16x16px`
- **颜色**：`rgba(34,39,39,0.75)`

### 4.3 Collapse Button（折叠按钮）

- 点击区：`24x24`
- padding：`4px`
- radius：`6px`
- icon：`16px`，颜色 `rgba(34,39,39,0.75)`
- hover：背景 `rgba(83,96,143,0.07)`
- focus：1px ring `#1aa38a`

> 重要：设计稿默认仅展示“折叠/展开”按钮；复制/刷新/反馈等额外交互必须以“可选 action”方式提供，默认关闭，避免破坏视觉一致性。

### 4.4 Body States（内容状态）

- **Ready**：两段正文，段落 gap `4px`
- **Loading**：shimmer skeleton
  - skeleton radius：`6px`
  - skeleton base：`rgba(45,66,107,0.10)`
  - duration：`1.2s`
- **Empty**：文案颜色用 Text Sub；如有 CTA 按钮，用 Primary 按钮规范（见下）
- **Error**：错误标题 `#f74331`；说明用 Text Sub；重试按钮用 Outline 按钮规范（见下）

### 4.5 Tags（标签组）

- height：`20px`
- padding：`8px` `2px`
- radius：`3px`
- 颜色严格限定在 Pink/Teal/Violet 三套

### 4.6 Buttons（仅在 Empty/Error 等状态出现）

- 高度：`36px`
- 圆角：`8px`
- Primary：bg `#1aa38a` / text `#ffffff` / hover 仅 opacity
- Outline：bg #fff / border `rgba(45,66,107,0.12)` / hover `rgba(83,96,143,0.07)`

---

## 5) Layout Principles（间距与布局原则）

本组件只允许使用以下间距：

- Outer padding: `12px`
- Outer gap: `12px`
- Header paddingX/Y: `8px` / `4px`
- Header gap: `8px`
- Paragraph gap: `4px`

---

## 6) Do’s & Don’ts（强约束护栏）

### Do

- 必须使用本规范给出的 **明确数值**（px/rgba/hex）
- 必须保持“面板卡片形态”，宽度随容器撑满，不得私自加 max-width 造成不满宽
- 必须保持渐变叠加顺序不变

### Don’t

- 不得添加阴影系统（shadow）、玻璃态、额外渐变、额外描边
- 不得使用非规定的 hover 方案（只允许 Hover Fill 或 opacity）
- 不得改变文字层级（字号/行高/字重）
- 不得引入新的 Tag 颜色

---

## 7) Responsive Behavior（响应式）

- 面板宽度永远 `width: 100%`；由父容器决定宽度。小屏时不额外改变 padding
- 折叠逻辑不因断点变化而改变

---

## 8) Agent Prompt Guide（给 AI 的提示模板）

将以下提示作为系统/任务前置约束：

```
请严格遵循 DESIGN_SKILL 中的“智能摘要组件面板（HiAI）”规范生成 UI。
必须使用左上角 HiAI Logo 图片资源：./summary-icon.png（禁止任何替代）。
只要出现智能摘要/服务摘要/SmartSummaryCard，即必须输出 width=100%（撑满父容器）的摘要面板，
所有颜色/间距/圆角/字号都按规范的明确数值实现，禁止自由设计。
```

