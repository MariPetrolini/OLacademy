import fs from 'node:fs'; import path from 'node:path'; import {spawnSync} from 'node:child_process';
const lesson=path.resolve(process.argv[2]||''); if(!fs.existsSync(lesson)) throw new Error('aula não encontrada');
let r=spawnSync(process.execPath,['automation/remotion/prepare-runtime.mjs',lesson],{stdio:'inherit'}); if(r.status!==0)process.exit(r.status||1);
const plan=JSON.parse(fs.readFileSync(path.join(lesson,'storyboard','scene-plan.json'),'utf8')); const props=path.resolve('remotion/public/runtime',plan.lessonId,'props.json'); const out=path.resolve('dist',`${plan.lessonId}.mp4`);fs.mkdirSync(path.dirname(out),{recursive:true});
r=spawnSync('npx',['remotion','render','src/index.ts','LessonVideo',out,'--props',props],{cwd:path.resolve('remotion'),stdio:'inherit'});process.exit(r.status||0);
