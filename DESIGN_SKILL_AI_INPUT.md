# DESIGN_SKILL — AI输入框（HiAI）

> 目的：让任何 AI 在生成涉及“AI输入框 / HiAI 输入框 / AI Chat Input”的网页 UI 时，做到 **像素级一致**。
> 本文件为强约束规范；**不得自行发挥**。

---

## 0.1 文案生成原则（重要：文案非固定）

- **所有组件的文案/示例内容必须视为动态内容**：应根据当前网页主题、业务场景与组件上下文实时生成或由业务数据驱动。
- **严禁把示例文案当成固定规范**：示例仅用于演示布局与交互，不约束具体措辞。
- **固定不变的只有**：组件的交互能力、状态划分与视觉样式框架（字号/间距/颜色/圆角/按钮尺寸/图标尺寸/动效层等）。

---

## 0) 组件触发规则（最重要）

只要出现以下任意关键词，就必须使用本规范：

- `AI输入框` / `HiAI输入框` / `AI Chat Input` / `对话输入框` / `富文本输入区`

命中后必须满足：

- **宽度**：必须自适应撑满容器（`width: 100%`）。
- **高度**：随内容自适应撑高（禁止固定高度）。

---

## 1) 结构骨架（必须保持层级与顺序）

外层结构固定为 3 段：

1. **OuterShell（灰底容器）**：承载整体圆角与内边距，并包含底部“动效层”。
2. **StatusRow（顶部状态行）**：一行 12px 灰色提示文案。
3. **InputCard（白底输入卡片）**：包含“输入文本区”与“底部操作栏”。

---

## 1.1 状态与交互（必须覆盖）

- **默认/空态**：输入区展示 placeholder（示例：`托管中`），发送按钮为 disabled。
- **输入中**：输入区为 value 文案；发送按钮可用（实现上允许由业务控制）。
- **发送 disabled**：当 value 为空或被业务禁用时，发送按钮必须使用 disabled 背景色（见 Tokens）。
- **图标按钮 hover**：仅允许使用 `hoverFill` 作为 hover 背景反馈（不允许额外阴影或缩放）。
- **动效层**：底部存在一层 40px 高的“动效蒙层”，覆盖在 OuterShell 底部区域（不影响交互点击）。

---

## 2) Typography（字体）

- Font family：`"PingFang SC", "PingFangSC", -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif`

| Part | Size | Line-height | Weight | Color |
| --- | --- | --- | --- | --- |
| 顶部状态文案 | 12px | 16px | 400 | rgba(34,39,39,0.6) |
| 输入区 placeholder | 14px | 20px | 400 | rgba(34,39,39,0.35) |
| 输入区 value | 14px | 20px | 400 | #222727 |

---

## 3) Layout & Geometry（布局与几何）

- **OuterShell**：`bg #f2f4f7`；`radius 14px`；`padding 6px`；`gap 6px`
- **StatusRow padding**：`x 8px / y 4px`
- **InputCard**：`bg #ffffff`；`border #ffffff`；`radius 12px`；`padding 12px`；`gap 12px`
- **ActionsRow gap**：`8px`
- **IconButton**：`padding 4px`；`radius 6px`；icon size `16px`
- **SendButton**：`height 24px`；`padding 4px`；`radius 6px`

---

## 4) Motion Layer（动效层）

- 位置：绝对定位于 OuterShell 底部区域（bottom: 0）。
- 高度：`40px`；透明度：`0.4`
- 水平内缩（百分比 inset，与设计稿一致）：
  - left：`1.24%`
  - right：`1.15%`
- 交互：动效层必须 `pointer-events: none`，不可遮挡输入与按钮。

---

## 5) Icon Assets（图标资源：必须使用同一套）

- 图标尺寸固定为 **16×16px**。
- **必须使用以下本地资源路径（禁止替换）**：

```
motion: ./ai-input-assets/ai-input-motion.png
magicWand: ./ai-input-assets/icon-magic-wand.png
smile: ./ai-input-assets/icon-smile.png
image: ./ai-input-assets/icon-image.png
underline: ./ai-input-assets/icon-underline.png
bold: ./ai-input-assets/icon-bold.png
orderedList: ./ai-input-assets/icon-ol.png
unorderedList: ./ai-input-assets/icon-ul.png
link: ./ai-input-assets/icon-link.png
palette: ./ai-input-assets/icon-palette.png
send: ./ai-input-assets/icon-send.png
```

---

## 6) Do’s & Don’ts（强约束护栏）

### Do

- 必须保持“灰底外壳 + 白底输入卡片 + 底部操作栏”的骨架与层级
- 必须保持所有圆角、间距、字体规格为明确数值（px/rgba/hex）
- hover 只允许 `hoverFill`，禁止阴影/缩放/发光

### Don’t

- 不得引入额外边框体系（除 InputCard 的白色边框）
- 不得引入默认 Tailwind 色板（例如 `text-gray-500`）
- 不得替换图标资源或改变 icon 尺寸

---

## 7) Agent Prompt Guide（给 AI 的提示模板）

```
请严格遵循 DESIGN_SKILL 中的“AI输入框（HiAI）”规范生成 UI。
只要出现 AI输入框/HiAI输入框/对话输入框/富文本输入区，就必须输出 width=100%（撑满父容器）的 AI 输入框；并且必须包含底部动效层、顶部状态行、白底输入卡片与底部操作栏。所有字号/间距/圆角/颜色必须按规范的明确数值实现，禁止自由设计。
```

