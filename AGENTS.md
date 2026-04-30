# AGENTS.md

## Cursor Cloud specific instructions

### Project overview

HiAI 组件规范平台 — a zero-install, single-file (index.html ~11k lines) React + Tailwind design-specification platform. All vendor dependencies (React 18, Babel Standalone, Tailwind CSS 3, Marked.js) are committed under `vendor/`. There is **no `package.json`**, no `npm install`, and no build step for the application itself.

### Running the dev server

```bash
cd /workspace
python3 -m http.server 5174
# Open http://127.0.0.1:5174/index.html
```

No other services (databases, caches, etc.) are needed — the app is fully client-side and uses `localStorage` for persistence.

### Lint / syntax checking

The only automated code-quality check is a JSX syntax validator that extracts the `<script type="text/babel">` block from `index.html` and runs it through esbuild:

```bash
node scripts/check-inline-babel.mjs
```

This requires Node.js (v20+). It uses `npx esbuild` (downloaded on-the-fly), so no pre-installed npm packages are needed.

### Building icons (optional)

```bash
python3 scripts/build_hiai_icon_library.py
```

Only needed when SVG sources in `hiai icon svg/` change. Requires only Python 3 stdlib.

### Key gotchas

- **Browser cache**: Babel compiles JSX at runtime in the browser. After editing `index.html`, you may need a hard-refresh (`Ctrl+Shift+R`) to see changes.
- **Single-file architecture**: All React components, tokens, and logic live in `index.html`. Search for function/token names to navigate.
- **No ESLint / Prettier / TypeScript**: The project has no traditional JS linting. The `check-inline-babel.mjs` script is the sole syntax gate.
- **Coding conventions**: See `CONTRIBUTING.md` for commit-message prefixes, token naming, and the "三件套" (three-piece sync) rule for UI changes.
