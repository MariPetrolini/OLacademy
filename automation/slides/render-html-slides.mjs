// Rasteriza uma pasta de slides HTML em PNG 1920x1080 usando Chrome headless.
// Serve para slides reconstruidos nativamente na identidade da escola, sem PowerPoint.
//
// uso: npm run slides:render-html -- <pasta-com-html> <pasta-de-saida> [--width 1920] [--height 1080]

import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const CHROME_CANDIDATES = [
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  '/Applications/Chromium.app/Contents/MacOS/Chromium',
  '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
  '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser',
];

const args = process.argv.slice(2);
const [srcArg, outArg] = args.filter((a) => !a.startsWith('--'));
const flag = (name, def) => {
  const i = args.indexOf(`--${name}`);
  return i >= 0 ? Number(args[i + 1]) : def;
};
if (!srcArg || !outArg) {
  console.error('uso: npm run slides:render-html -- <pasta-com-html> <pasta-de-saida> [--width N] [--height N]');
  process.exit(1);
}
const W = flag('width', 1920);
const Hh = flag('height', 1080);
const src = path.resolve(srcArg);
const out = path.resolve(outArg);
if (!fs.existsSync(src)) throw new Error(`pasta nao encontrada: ${src}`);

const chrome = CHROME_CANDIDATES.find((p) => fs.existsSync(p));
if (!chrome) {
  console.error('Nenhum navegador baseado em Chromium encontrado. Instale o Google Chrome.');
  process.exit(2);
}

const files = fs.readdirSync(src).filter((f) => f.toLowerCase().endsWith('.html')).sort();
if (!files.length) throw new Error(`nenhum .html em ${src}`);
fs.mkdirSync(out, { recursive: true });

const pngSize = (file) => {
  const b = fs.readFileSync(file);
  if (b.length < 24 || b.readUInt32BE(0) !== 0x89504e47) return null;
  return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) };
};

let ok = 0;
const problems = [];
for (const f of files) {
  const target = path.join(out, f.replace(/\.html$/i, '.png'));
  const r = spawnSync(chrome, [
    '--headless=new', '--disable-gpu', '--hide-scrollbars',
    '--force-device-scale-factor=1', `--window-size=${W},${Hh}`,
    `--screenshot=${target}`, `file://${path.join(src, f)}`,
  ], { stdio: 'ignore' });
  if (r.status !== 0 || !fs.existsSync(target)) { problems.push(`${f}: falha na rasterizacao`); continue; }
  const d = pngSize(target);
  if (!d) { problems.push(`${f}: PNG invalido`); continue; }
  if (d.w !== W || d.h !== Hh) { problems.push(`${f}: saiu ${d.w}x${d.h}, esperado ${W}x${Hh}`); continue; }
  ok++;
}
console.log(`${ok}/${files.length} slides rasterizados em ${W}x${Hh} -> ${out}`);
for (const p of problems) console.error('ERRO ' + p);
process.exit(problems.length ? 3 : 0);
