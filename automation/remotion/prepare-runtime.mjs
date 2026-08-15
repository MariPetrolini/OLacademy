import fs from 'node:fs'; import path from 'node:path';
const lesson=path.resolve(process.argv[2]||''); if(!fs.existsSync(lesson)) throw new Error('aula não encontrada');
const plan=JSON.parse(fs.readFileSync(path.join(lesson,'storyboard','scene-plan.json'),'utf8')); const audio=JSON.parse(fs.readFileSync(path.join(lesson,'voice','audio-manifest.json'),'utf8')); const manifest=JSON.parse(fs.readFileSync(path.join(lesson,'source','slides-manifest.json'),'utf8'));
const rt=path.resolve('remotion/public/runtime',plan.lessonId); fs.rmSync(rt,{recursive:true,force:true}); fs.mkdirSync(path.join(rt,'slides'),{recursive:true}); fs.mkdirSync(path.join(rt,'audio'),{recursive:true});
for(const s of manifest.slides){const src=path.join(lesson,s.file);fs.copyFileSync(src,path.join(rt,'slides',path.basename(src)))}
for(const a of audio.segments){const src=path.join(lesson,a.file);fs.copyFileSync(src,path.join(rt,'audio',path.basename(src)))}
const props={lessonId:plan.lessonId,scenes:plan.scenes,audioSegments:audio.segments.map(a=>({id:a.id,durationSeconds:a.durationSeconds,file:`runtime/${plan.lessonId}/audio/${path.basename(a.file)}`})),slideBase:`runtime/${plan.lessonId}/slides`};
fs.writeFileSync(path.join(rt,'props.json'),JSON.stringify(props,null,2)); console.log(path.join(rt,'props.json'));
