import fs from 'node:fs'; import path from 'node:path'; import os from 'node:os'; import {spawnSync} from 'node:child_process';
function run(cmd,args){const r=spawnSync(cmd,args,{stdio:'inherit'}); if(r.status!==0) throw new Error(`${cmd} falhou`)}
const args=process.argv.slice(2); const lessonArg=args[0]; const idx=args.indexOf('--pptx'); const pptxArg=idx>=0?args[idx+1]:null;
if(!lessonArg||!pptxArg){console.error('uso: npm run slides:ingest -- <pasta-da-aula> --pptx <arquivo.pptx>');process.exit(1)}
const lesson=path.resolve(lessonArg), pptx=path.resolve(pptxArg); if(!fs.existsSync(pptx)||path.extname(pptx).toLowerCase()!=='.pptx') throw new Error('PPTX inválido');
const originalDir=path.join(lesson,'source','original'), slidesDir=path.join(lesson,'source','slides'), mediaDir=path.join(lesson,'source','extracted-media');
for(const d of [originalDir,slidesDir,mediaDir]){fs.rmSync(d,{recursive:true,force:true});fs.mkdirSync(d,{recursive:true})}
const dest=path.join(originalDir,'deck.pptx'); fs.copyFileSync(pptx,dest);
const tmp=fs.mkdtempSync(path.join(os.tmpdir(),'course-ppt-'));
try{
 run('soffice',['--headless','--convert-to','pdf','--outdir',tmp,dest]);
 const pdf=path.join(tmp,'deck.pdf'); if(!fs.existsSync(pdf)) throw new Error('LibreOffice não produziu deck.pdf');
 run('pdftoppm',['-png','-r','160',pdf,path.join(tmp,'slide')]);
 const pngs=fs.readdirSync(tmp).filter(f=>/^slide-\d+\.png$/.test(f)).sort((a,b)=>Number(a.match(/\d+/)[0])-Number(b.match(/\d+/)[0]));
 pngs.forEach((f,i)=>fs.copyFileSync(path.join(tmp,f),path.join(slidesDir,`slide-${String(i+1).padStart(3,'0')}.png`)));
 const unzip=spawnSync('unzip',['-j',dest,'ppt/media/*','-d',mediaDir],{stdio:'ignore'}); // no media is acceptable
 const manifest={source:'source/original/deck.pptx',slideCount:pngs.length,slides:pngs.map((_,i)=>({number:i+1,file:`source/slides/slide-${String(i+1).padStart(3,'0')}.png`,required:true}))};
 fs.writeFileSync(path.join(lesson,'source','slides-manifest.json'),JSON.stringify(manifest,null,2));
 fs.writeFileSync(path.join(lesson,'STATUS.md'),`# Status\n\nPHASE: PPT_INGESTED\n\nSlides: ${pngs.length}\nPróximo: análise visual + adaptação do roteiro.\n`);
 console.log(`PPT ingerido: ${pngs.length} slides.`);
} finally {fs.rmSync(tmp,{recursive:true,force:true})}
