# DESIGN_SKILL — AI输入框（HiAI）

> 目的：让任何 AI 在生成「AI输入框 / HiAI输入框 / AI Chat Input」时，按最新 UI 交互样式进行像素级还原。  
> 本文件为强约束规范；不得自行发挥。

---

## 0) 组件触发规则

命中以下任一关键词必须使用本规范：

- `AI输入框`
- `HiAI输入框`
- `AI Chat Input`
- `对话输入框`
- `富文本输入区`

强制要求：

- 组件宽度必须 `width: 100%`，默认撑满父容器。
- 组件高度随内容自适应，禁止固定高度。

---

## 1) 结构骨架（必须保持）

固定三层：

1. `OuterShell`（灰底外壳）
2. `StatusRow`（顶部提示文案）
3. `InputCard`（白底输入卡片，包含推荐区/输入区/操作栏）

---

## 2) 产品定义：StatusRow 提醒文案（重点）

- 该位置文案定义为：**AI 基于当前聊天内容自动生成的提醒文案**，用于提示当前回复状态/下一步动作。
- 文案必须支持按输入框使用场景动态生成，不得写死为固定句子。
- 文案默认限制在 **20 个字以内**（中文口径）；超出时应自动压缩语义，优先保留动作信息。
- 该行始终保留结构占位，即使无文案也保留 `StatusRow` 容器。

生成策略（执行规则）：

- 优先级顺序：`风险提醒` > `发送状态` > `推荐状态` > `常规引导`。
- 单条文案只表达一个主动作，禁止并列两个以上动作指令。
- 推荐模板：`{主体}{状态}，{下一动作}`（示例：`AI已生成回复，待发送`）。
- 词汇建议：状态词优先使用 `已生成/待审核/可发送/需复核/已匹配`，动作词优先使用 `发送/采纳/复核/补充`。
- 长度裁剪顺序：先删修饰词，再删次要分句，最后保留“状态 + 动作”主干。
- 兜底文案（无明确状态时）：`可继续输入，AI将辅助生成`（需按 20 字规则压缩到可展示版本）。

推荐语气示例（仅示例，不是固定文案）：

- `AI已生成回复，待发送`
- `检测到风险词，建议复核`
- `已匹配话术，可一键采纳`

---

## 3) 样式 Tokens（与当前实现对齐）

- `OuterShell`：`bg semi-bluegrey-2`，`radius 14px`，`padding 6px`，`gap 6px`
- `StatusRow`：`padding x=8px y=4px`，`font 12/16`，`color rgba(34,39,39,0.6)`
- `InputCard`：`bg #fff`，`border 1px #fff`，`radius 12px`，`padding 12px`，`gap 12px`
- 文本区：`font 14/20`，placeholder `rgba(34,39,39,0.35)`，value `#222727`
- 动效层：`height 40px`，`opacity 0.4`，`left inset 2.11%`，`right inset 2.02%`

---

## 4) 推荐区（回复推荐）规范

- 推荐区容器：`bg semi-bluegrey-1`，`radius 12px`，`padding 8px`，`gap 4px`
- 标题：`回复推荐`，`12/16`，`600`，渐变文字（保留渐变）
- 条目：`radius 6px`，`padding 4px`，hover 底 `rgba(52,59,57,0.05)`
- hover tooltip：深灰底、白字、上方悬浮，文案随交互模式变化

右上角操作区（关闭/刷新/复制/发送）必须满足：

- 使用平台基础组件 `HiUI Button` 的 **`borderless + tertiary + small + icon-only`**
- 容器尺寸固定 `24x24`
- icon 尺寸 `16x16`，居中
- 竖分割线 `1x12`，颜色 `rgba(34,39,39,0.09)`

图标库 name（必须）：

- 关闭：`hiai-x-close-stroked`
- 刷新：`refresh`
- 复制：`IconCopyStroked2`
- 发送：`hiai-send-stroked`

---

## 5) 底部操作栏按钮规范

左侧工具按钮（如表情、图片）：

- 使用平台基础组件 `HiUI Button` 的 **`borderless + tertiary + default + icon-only`**
- 容器尺寸固定 `36x36`
- icon 尺寸 `16x16`，居中

右下角发送按钮：

- 使用平台基础组件 `HiUI Button` 的 **`solid + secondary + small + icon-only`**
- 容器尺寸固定 `24x24`
- 圆角 `8px`
- 有效态背景：`#222727`（黑底）
- 禁用态背景：`semi-grey-1`
- 发送 icon 使用图标库 `hiai-send-stroked`

---

## 6) 图标资源约束

- 组件内所有 icon 必须来自平台图标库（`getIcon(name)` 语义）。
- 禁止 emoji、临时 SVG、第三方 iconfont、未入库资源。
- 推荐区关闭 icon 必须使用 `hiai-x-close-stroked`，不得退回旧别名导致视觉尺寸偏差。
- icon 基准尺寸固定 `16px`，禁止随意改成 14/18/20。

---

## 7) 状态与交互

- `Default/空态`：value 为空，发送按钮禁用。
- `Typing`：value 非空，发送按钮可用（黑底）。
- 推荐区可选显示；关闭后本轮隐藏。
- 推荐条点击支持两种模式：`adopt`（采纳到输入框）与 `send`（直接发送）。

---

## 8) 禁止项（必须遵守）

- 禁止将状态行文案写死为固定句子。
- 禁止状态文案超过 20 字仍直接展示（需压缩）。
- 禁止把推荐区右上角按钮做成 `light` 类型或 `36x36`。
- 禁止将底部左侧工具按钮错误改成 `small`。
- 禁止发送按钮出现绿色背景（深色类型统一黑底体系）。
- 禁止使用 `filter: brightness(0) invert(1)` 作为强依赖规则。

---

## 9) Agent Prompt Guide

```text
请严格遵循 DESIGN_SKILL「AI输入框（HiAI）」规范生成 UI。
必须输出：OuterShell + StatusRow + InputCard 三层结构，宽度100%，高度自适应。
StatusRow 文案定义为 AI 根据聊天内容自动生成的提醒文案，按场景动态变化，默认不超过20个字。
推荐区右上角四个按钮必须为 borderless+tertiary+small+icon-only（24x24）。
底部左侧工具按钮必须为 borderless+tertiary+default+icon-only（36x36）。
右下发送按钮必须为 solid+secondary+small+icon-only（24x24，黑底）。
所有图标必须来自图标库 name，不得使用未入库资源。
```
