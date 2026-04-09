# 贡献指南

欢迎参与 HiAI 组件规范平台的维护与优化！在提交代码前，请仔细阅读本指南。

---

## 目录

- [分支策略](#分支策略)
- [开发流程](#开发流程)
- [Commit 规范](#commit-规范)
- [代码规范](#代码规范)
- [UI 改动必须同步的三件套](#ui-改动必须同步的三件套)
- [PR 提交标准](#pr-提交标准)
- [常见问题](#常见问题)

---

## 分支策略

```
main          ← 保护分支，只接受 PR 合并，始终可部署
dev           ← 日常开发主分支，PR 先合入 dev 再合入 main
feature/xxx   ← 每个新功能 / 优化独立一个分支
fix/xxx       ← Bug 修复分支
```

**基本流程：**

```bash
# 1. 从 dev 切出新分支
git checkout dev
git pull origin dev
git checkout -b feature/form-recommend-refresh

# 2. 开发完成后推送
git push origin feature/form-recommend-refresh

# 3. 在 GitHub 发起 PR → dev
# 4. Code Review 通过后合并
```

---

## 开发流程

### 环境准备

```bash
git clone <仓库地址>
cd smart-summary
python3 -m http.server 5174
# 访问 http://127.0.0.1:5174/index.html
```

### 主要编辑文件

所有代码目前集中在 `index.html`，按以下区域进行修改：

| 内容类型 | 搜索关键词 | 位置说明 |
|---------|-----------|---------|
| 全局 CSS / 动效 | `<style>` / `@keyframes` | 文件顶部 |
| Token 定义 | `SMART_SUMMARY_TOKENS` / `FORM_RECOMMEND_TOKENS` / `AI_INPUT_TOKENS` | CSS 之后 |
| Design Skill 构建函数 | `buildDesignSkillMarkdown` / `buildFormRecommend...` / `buildAiInput...` | Token 之后 |
| React 组件 | `function SmartSummaryCard` / `function FormRecommend` 等 | 中段 |
| Token 面板 UI | `TokensPanel` / `activeComponentId === "formRecommend"` | 后段 |
| 沙盒逻辑 | `parseMdDesignValues` / `SandboxModal` / `Spec*` | 尾部 |

---

## Commit 规范

使用以下前缀，便于追溯变更：

```
feat:   新增功能（新组件、新交互）
fix:    Bug 修复
style:  样式调整（不涉及逻辑）
token:  Token 新增或修改
skill:  Design Skill 文档更新
refac:  重构（不改变功能）
docs:   文档更新（README / CONTRIBUTING）
chore:  构建、依赖、配置类改动
```

**示例：**

```bash
git commit -m "feat: 表单推荐输入框 hover 显示刷新按钮"
git commit -m "token: 新增 refreshIconGradient，图标渐变色由 token 驱动"
git commit -m "skill: FormRecommend §5.4 补充刷新按钮交互规范"
git commit -m "fix: 修复 SmartSummary shimmer 动效在沙盒中不显示"
```

---

## 代码规范

### JavaScript / JSX

- **禁止** 使用 `var`，统一使用 `const` / `let`
- **禁止** 在组件内写行内注释解释显而易见的代码
- **禁止** 引入新的外部依赖（保持无 npm install 的单文件方案）
- React 组件名使用 **PascalCase**
- 函数 / 变量使用 **camelCase**
- Token 对象 Key 使用 **camelCase**（如 `refreshBtnRadiusPx`）

### CSS / 动效

- **禁止** 使用 Tailwind 默认色板名（`bg-blue-500`）—— 必须使用 Token 显式数值
- 新增 `@keyframes` 必须写在文件顶部的 `<style>` 块内，并添加注释说明用途
- 动效时长、缓动函数必须来自 Token（禁止魔数）

### Token 规范

- Token Key 命名格式：`[位置][属性][单位]`，如 `refreshBtnRadiusPx`、`titleFontSizePx`
- 颜色 Token 统一使用 `rgba(r,g,b,a)` 或 `#RRGGBB`，**禁止** `#000` 简写
- 新增组件必须在对应的 `*_TOKENS` 对象中定义所有设计变量

---

## UI 改动必须同步的三件套

**每次修改 UI 组件的样式或交互，必须同步以下三处，缺一不可：**

```
1. Token 定义
   → 在 *_TOKENS 对象中新增对应字段

2. Token 面板 UI
   → 在 TokensPanel 的对应分组中加入可编辑控件
   → 使用者应能在界面上实时调整该 Token

3. Design Skill 文档
   → §2 更新数值表格
   → §3 更新 HTML 结构注释
   → §5 更新交互规范（如有新交互）
   → §6/§7 更新禁止项和校验规则
```

**检查清单（PR 描述中必须勾选）：**

```markdown
- [ ] Token 已定义且命名规范
- [ ] Token 面板已新增对应控件（用户可调节）
- [ ] Design Skill §2 数值表已更新
- [ ] Design Skill §5 交互规范已更新（如涉及动效/交互）
- [ ] Design Skill §7 校验规则已更新
- [ ] 页面可正常访问（无 JS 报错）
- [ ] 沙盒测试可正常打开并显示正确预览
```

---

## PR 提交标准

### PR 标题格式

```
[feat/fix/token/skill] 简短描述（≤50 字符）
```

### PR 描述模板

```markdown
## 改动内容
<!-- 一句话描述本次改动 -->

## 截图对比
| 改前 | 改后 |
|------|------|
| （截图） | （截图） |

## 三件套同步确认
- [ ] Token 已定义
- [ ] Token 面板已更新
- [ ] Design Skill 已同步

## 测试步骤
1. 启动本地服务：`python3 -m http.server 5174`
2. 访问 http://127.0.0.1:5174/index.html
3. 切换到「xxx」组件
4. 验证：...

## 备注
<!-- 其他需要 Reviewer 注意的事项 -->
```

---

## 常见问题

**Q：改了代码，刷新页面后看不到变化？**  
A：Babel 在浏览器端编译，有时需要强刷（`Cmd+Shift+R` / `Ctrl+Shift+R`）清除缓存。

**Q：页面打不开，提示 JS 错误？**  
A：JSX 语法错误最常见。检查：① 模板字符串里的 Unicode 转义（`\u` 后必须跟 4 位十六进制）；② 标签未正确闭合；③ 用 Chrome DevTools Console 看报错行号。

**Q：新增 Token 后，Token 面板看不到新控件？**  
A：需要在 `TokensPanel` 组件的对应 `fields` 数组中手动添加条目，Token 面板不会自动感知新 Token。

**Q：修改了 Token，Design Skill 文档内容是否自动更新？**  
A：是的。Design Skill 由 `buildDesignSkillMarkdown(activeTokens)` 实时生成，Token 变化后文档立即更新。沙盒测试同理。

**Q：如何添加新的 UI 组件？**  
A：参考现有组件（如 `FormRecommend`），按以下顺序：  
① 定义 `NEW_COMPONENT_TOKENS`；  
② 写 React 组件函数；  
③ 写 `buildNewComponentDesignSkillMarkdown(t)`；  
④ 在 `TokensPanel` 中添加对应分组；  
⑤ 在 `Demo` 组件中注册新组件切换逻辑；  
⑥ 写 `SpecNewComponent`（沙盒预览组件）；  
⑦ 在 `SandboxModal` 中接入。

---

如有疑问，请在 GitHub Issue 中讨论，或联系项目负责人。
