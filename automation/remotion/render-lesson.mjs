import fs from 'node:fs'; import path from 'node:path'; import {spawnSync} from 'node:child_process';
const args=process.argv.slice(2); const lessonArg=args.find(a=>!a.startsWith('--'))||''; const lesson=path.resolve(lessonArg); if(!fs.existsSync(lesson)) throw new Error('aula não encontrada');
const forwarded=[]; for(let i=0;i<args.length;i++){if(args[i].startsWith('--')){forwarded.push(args[i]);if(args[i+1]&&!args[i+1].startsWith('--'))forwarded.push(args[++i])}}
let r=spawnSync(process.execPath,['automation/remotion/prepare-runtime.mjs',lesson,...forwarded],{stdio:'inherit'}); if(r.status!==0)process.exit(r.status||1);
const plan=JSON.parse(fs.readFileSync(path.join(lesson,'storyboard','scene-plan.json'),'utf8')); const props=path.resolve('remotion/public/runtime',plan.lessonId,'props.json'); const out=path.resolve('dist',`${plan.lessonId}.mp4`);fs.mkdirSync(path.dirname(out),{recursive:true});
r=spawnSync('npx',['remotion','render','src/index.ts','LessonVideo',out,'--props',props],{cwd:path.resolve('remotion'),stdio:'inherit'});process.exit(r.status||0);
