# DESIGN_SKILL — 表单推荐（HiAI）

> **目标**：让任何大语言模型在**无本地环境**下，仅凭本文档即可把“表单推荐 / AI 推荐表单字段 / FormRecommend”做到**像素级一致**（交互 + 样式）。
> 本文件为强约束规范；**不得自行发挥**。

---

## 0) 适用范围与触发规则

只要需求或 UI 出现以下任一关键词，即必须应用本规范：

- `表单推荐` / `AI推荐表单` / `AI 推荐字段` / `FormRecommend` / `AI推荐`

命中后必须满足：

- **宽度**：`width: 100%`（撑满父容器）
- **高度**：随内容自适应（禁止固定高度）
- **固定不变**：交互状态机 + 视觉样式框架（字号/间距/颜色/圆角/渐变/动效）
- **动态变化**：文案内容（见 1.2）

---

## 1) 组件定义（What it is）

### 1.1 结构骨架（固定，不得改）

组件结构固定为：

1. **标题行（Label Row）**：字段名 + AI 标签
2. **输入框（Input Wrapper）**：展示 placeholder 或已采纳内容
3. **下方区域（Below Area）**：根据交互场景展示“加载彩条”或“推荐列表”，采纳后隐藏

> 重要：当 **没有 AI 推荐** 或 **用户已采纳** 时，下方区域必须完全消失（保持干净）。

### 1.2 文案生成原则（重要：文案非固定）

- 文案必须根据网页主题、业务场景与字段语义动态生成（或由业务数据驱动）。
- 文案只用于承载信息，不得改变任何布局/样式框架。

---

## 2) 交互状态机（Must Implement）

必须覆盖以下场景：

- **Loading（加载中）**：输入框下方显示“彩色渐变骨架动效条”，不显示推荐文字。
- **Single（单条推荐）**：下方显示 1 条可采纳推荐。
- **Multi（多条推荐）**：下方显示 3 条可采纳推荐。
- **Ultra（超多字数）**：每条推荐约 100 汉字；默认单行省略号；hover 展开全文并自适应撑高。
- **Adopted（已采纳）**：点击任意推荐后：
  - 推荐文案写入输入框
  - 下方区域立刻消失
  - 输入框高度自适应撑高，完整展示采纳文案（允许换行）

必须提供：

- **Reset（重置）**：用于演示预览，恢复到当前场景初始状态（未采纳、下方区域可见）。

---

## 3) 内容约束（Copy Rules）

### 3.1 单条/多条推荐文案（动态）

- **语义**：必须是“用户问题描述”（如：登录失败、申诉失败、退款卡住等）
- **长度建议**：每条 **15–30** 个汉字

### 3.2 超多字数文案（Ultra）

- **长度**：每条约 **100** 个汉字
- **默认展示**：单行 + 省略号
- **hover 展示**：展开全文、自动换行、容器自适应撑高

---

## 4) 视觉与 Tokens（Pixel-perfect）

> 这里的数值是**唯一可信来源**。实现时必须严格按 tokens 数值输出。

### 4.1 Typography

- Font family：`"PingFang SC", "PingFangSC", -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif`

### 4.2 Colors & Gradients

- **AI 标签背景**：见 `aiBadgeBg`
- **AI 文字渐变**：见 `aiBadgeTextGradient`
- **加载彩条背景**：见 `recommendBarBg`
- **加载彩条动效时长**：见 `stripeAnimDurationSec`
- **推荐容器背景**：见 `recommendWrapBg`
- **推荐项 hover 背景**：见 `recommendItemBgHover`
- **推荐项选中/高亮背景**：见 `recommendItemBgSelected`

### 4.3 Spacing & Radius

- 外层 gap：`gapOuterPx`
- 输入框 padding/radius：`inputPadX/inputRightPadX/inputPadY/inputRadiusPx`
- 下方推荐容器：**禁止边框**（border=0），radius/padding/gap：`recommendWrapRadiusPx/recommendWrapPadPx/recommendWrapGapPx`

---

## 5) 可访问性（A11y）

- 推荐列表容器：`role="listbox"` + `aria-label="AI 推荐内容"`
- 每条推荐：button 可聚焦；hover/选中态需可感知（视觉层面已规定）

---

## 6) Do / Don’t（零容忍）

### Do

- 严格按 tokens 数值实现（px/rgba/渐变字符串）
- 严格实现状态机（Loading/Single/Multi/Ultra/Adopted/Reset）

### Don’t

- 不得新增边框、阴影体系、玻璃态
- 不得改动任何渐变配方/顺序/角度
- 不得把示例文案当成固定规范

---

## 7) Agent Prompt Guide（给 AI 的提示模板）

```txt
请严格遵循 DESIGN_SKILL 中的“表单推荐（HiAI）”规范生成 UI。
文案是动态内容（根据网页主题与字段语义生成），但交互状态机与视觉样式框架必须像素级一致。
必须实现：Loading/Single/Multi/Ultra/Adopted/Reset，并确保“采纳后下方区域消失、输入框自适应撑高展示全文”。
```

