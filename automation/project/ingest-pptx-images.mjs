// Ingestao de PPTX cujos slides sao imagens full-bleed (1 imagem por slide, sem texto).
// Extrai os PNGs originais embutidos, sem LibreOffice e sem re-render: nenhuma recompressao,
// nenhuma troca de fonte, nenhum deslocamento de layout.
//
// Para decks com texto/vetor editavel, use `npm run slides:ingest` (caminho LibreOffice).
// Este script BLOQUEIA se o deck nao for 1 imagem por slide, em vez de degradar em silencio.
//
// uso: npm run slides:ingest-images -- <pasta-da-aula> --pptx <arquivo.pptx>

import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';

const args = process.argv.slice(2);
const lessonArg = args[0];
const idx = args.indexOf('--pptx');
const pptxArg = idx >= 0 ? args[idx + 1] : null;
if (!lessonArg || !pptxArg) {
  console.error('uso: npm run slides:ingest-images -- <pasta-da-aula> --pptx <arquivo.pptx>');
  process.exit(1);
}
const lesson = path.resolve(lessonArg);
const pptx = path.resolve(pptxArg);
if (!fs.existsSync(lesson)) throw new Error(`aula nao encontrada: ${lesson}`);
if (!fs.existsSync(pptx) || path.extname(pptx).toLowerCase() !== '.pptx') throw new Error('PPTX invalido');

// ---------- leitor de ZIP minimo (central directory), suficiente para OOXML ----------
const buf = fs.readFileSync(pptx);
function findEOCD(b) {
  for (let i = b.length - 22; i >= 0 && i > b.length - 66000; i--) {
    if (b.readUInt32LE(i) === 0x06054b50) return i;
  }
  throw new Error('EOCD nao encontrado: arquivo nao parece um zip');
}
const eocd = findEOCD(buf);
const entryCount = buf.readUInt16LE(eocd + 10);
let cdOff = buf.readUInt32LE(eocd + 16);
const entries = new Map();
for (let n = 0; n < entryCount; n++) {
  if (buf.readUInt32LE(cdOff) !== 0x02014b50) throw new Error('central directory corrompido');
  const method = buf.readUInt16LE(cdOff + 10);
  const compSize = buf.readUInt32LE(cdOff + 20);
  const nameLen = buf.readUInt16LE(cdOff + 28);
  const extraLen = buf.readUInt16LE(cdOff + 30);
  const commentLen = buf.readUInt16LE(cdOff + 32);
  const localOff = buf.readUInt32LE(cdOff + 42);
  const name = buf.toString('utf8', cdOff + 46, cdOff + 46 + nameLen);
  entries.set(name, { method, compSize, localOff });
  cdOff += 46 + nameLen + extraLen + commentLen;
}
function read(name) {
  const e = entries.get(name);
  if (!e) throw new Error(`entrada ausente no pptx: ${name}`);
  const nameLen = buf.readUInt16LE(e.localOff + 26);
  const extraLen = buf.readUInt16LE(e.localOff + 28);
  const start = e.localOff + 30 + nameLen + extraLen;
  const raw = buf.subarray(start, start + e.compSize);
  if (e.method === 0) return Buffer.from(raw);
  if (e.method === 8) return zlib.inflateRawSync(raw);
  throw new Error(`metodo de compressao nao suportado: ${e.method}`);
}
const text = (name) => read(name).toString('utf8');

// ---------- descobre a ordem real dos slides ----------
const presRels = text('ppt/_rels/presentation.xml.rels');
const relTarget = new Map();
for (const m of presRels.matchAll(/Id="([^"]+)"[^>]*Target="([^"]+)"/g)) relTarget.set(m[1], m[2]);
const pres = text('ppt/presentation.xml');
const order = [];
for (const m of pres.matchAll(/<p:sldId[^>]*r:id="([^"]+)"/g)) {
  const t = relTarget.get(m[1]);
  if (!t) throw new Error(`rel de slide nao resolvido: ${m[1]}`);
  order.push('ppt/' + t.replace(/^\.\.\//, '').replace(/^\/*/, ''));
}
if (!order.length) throw new Error('nenhum slide encontrado em presentation.xml');

// ---------- valida 1 imagem full-bleed por slide e resolve a imagem ----------
const pngSize = (b) => {
  if (b.readUInt32BE(0) !== 0x89504e47) return null;
  return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) };
};
const slides = [];
const problems = [];
for (let i = 0; i < order.length; i++) {
  const sPath = order[i];
  const xml = text(sPath);
  const blips = [...xml.matchAll(/<a:blip[^>]*r:embed="([^"]+)"/g)].map((m) => m[1]);
  const shapes = (xml.match(/<p:sp>/g) || []).length;
  const runs = (xml.match(/<a:t>/g) || []).length;
  if (blips.length !== 1) problems.push(`slide ${i + 1}: ${blips.length} imagens (esperado 1)`);
  if (runs > 0) problems.push(`slide ${i + 1}: contem ${runs} trechos de texto editavel`);
  const relsPath = sPath.replace(/slides\/(slide\d+\.xml)$/, 'slides/_rels/$1.rels');
  const rels = text(relsPath);
  const map = new Map();
  for (const m of rels.matchAll(/Id="([^"]+)"[^>]*Target="([^"]+)"/g)) map.set(m[1], m[2]);
  const target = map.get(blips[0]);
  if (!target) { problems.push(`slide ${i + 1}: imagem nao resolvida`); continue; }
  const mediaName = 'ppt/' + target.replace(/^\.\.\//, '');
  const bytes = read(mediaName);
  const dim = pngSize(bytes);
  slides.push({ number: i + 1, mediaName, bytes, dim, shapes });
}
if (problems.length) {
  console.error('BLOQUEADO: este deck nao e "uma imagem full-bleed por slide".');
  for (const p of problems) console.error('  - ' + p);
  console.error('\nUse o caminho com LibreOffice: npm run slides:ingest -- <aula> --pptx <arquivo>');
  process.exit(2);
}

// ---------- escreve os artefatos ----------
const originalDir = path.join(lesson, 'source', 'original');
const slidesDir = path.join(lesson, 'source', 'slides');
const mediaDir = path.join(lesson, 'source', 'extracted-media');
for (const d of [originalDir, slidesDir, mediaDir]) {
  fs.rmSync(d, { recursive: true, force: true });
  fs.mkdirSync(d, { recursive: true });
}
fs.copyFileSync(pptx, path.join(originalDir, 'deck.pptx'));

const CANVAS = { w: 1920, h: 1080 };
const warnings = [];
for (const s of slides) {
  const pad = String(s.number).padStart(3, '0');
  const ext = path.extname(s.mediaName).toLowerCase() || '.png';
  fs.writeFileSync(path.join(slidesDir, `slide-${pad}${ext}`), s.bytes);
  fs.writeFileSync(path.join(mediaDir, path.basename(s.mediaName)), s.bytes);
  if (s.dim && s.dim.h < CANVAS.h) {
    warnings.push(`slide ${s.number}: ${s.dim.w}x${s.dim.h} abaixo de ${CANVAS.w}x${CANVAS.h} (upscale de ${(CANVAS.h / s.dim.h).toFixed(2)}x)`);
  }
}
const manifest = {
  source: 'source/original/deck.pptx',
  ingestedBy: 'ingest-pptx-images.mjs',
  ingestMode: 'embedded-image-extraction',
  note: 'PNGs originais extraidos do PPTX sem re-render. Nenhuma recompressao aplicada.',
  targetCanvas: `${CANVAS.w}x${CANVAS.h}`,
  slideCount: slides.length,
  slides: slides.map((s) => ({
    number: s.number,
    file: `source/slides/slide-${String(s.number).padStart(3, '0')}${path.extname(s.mediaName).toLowerCase() || '.png'}`,
    sourceMedia: s.mediaName,
    width: s.dim?.w ?? null,
    height: s.dim?.h ?? null,
    required: true,
  })),
  warnings,
};
fs.writeFileSync(path.join(lesson, 'source', 'slides-manifest.json'), JSON.stringify(manifest, null, 2) + '\n');
fs.writeFileSync(
  path.join(lesson, 'STATUS.md'),
  fs.readFileSync(path.join(lesson, 'STATUS.md'), 'utf8').replace(/^PHASE: .*$/m, 'PHASE: PPT_INGESTED')
);

console.log(`PPT ingerido: ${slides.length} slides (extracao direta, sem re-render).`);
for (const w of warnings) console.log('AVISO ' + w);
