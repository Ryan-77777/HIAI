#!/usr/bin/env node
/**
 * 校验 index.html 内 type="text/babel" 的 JSX 片段可被解析（避免引号/反引号错配导致整页白屏）。
 * 用法：node scripts/check-inline-babel.mjs
 * 依赖：通过 npx 临时拉取 esbuild（无需仓库内 package.json）。
 */
import { readFileSync, unlinkSync, writeFileSync } from "fs";
import { spawnSync } from "child_process";
import { dirname, join } from "path";
import { fileURLToPath } from "url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const htmlPath = join(root, "index.html");
const html = readFileSync(htmlPath, "utf8");
const marker = '<script type="text/babel" data-presets="react">';
const start = html.indexOf(marker);
if (start < 0) {
  console.error("check-inline-babel: marker not found in index.html");
  process.exit(1);
}
const bodyStart = html.indexOf(">", start) + 1;
const end = html.indexOf("</script>", bodyStart);
if (end < 0) {
  console.error("check-inline-babel: closing </script> not found");
  process.exit(1);
}
const code = html.slice(bodyStart, end);
const tmpJsx = join(root, ".inline-babel-check.jsx");
const tmpOut = join(root, ".inline-babel-check.out.js");
writeFileSync(tmpJsx, code, "utf8");
const r = spawnSync(
  "npx",
  ["--yes", "esbuild", tmpJsx, "--loader:.jsx=jsx", "--outfile=" + tmpOut],
  { stdio: "inherit", cwd: root, shell: process.platform === "win32" },
);
try {
  unlinkSync(tmpJsx);
} catch {}
try {
  unlinkSync(tmpOut);
} catch {}
if (r.status !== 0) {
  console.error("check-inline-babel: esbuild parse/transform failed (fix syntax in index.html babel block)");
  process.exit(r.status ?? 1);
}
console.log("check-inline-babel: OK");
