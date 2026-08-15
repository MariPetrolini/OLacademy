import fs from 'node:fs';
import path from 'node:path';
import {spawnSync} from 'node:child_process';

const args=process.argv.slice(2);
const lessonArg=args.find(a=>!a.startsWith('--'))||'';
const option=(name)=>{const i=args.indexOf(name);return i>=0?args[i+1]:undefined};
const lesson=path.resolve(lessonArg);
if(!fs.existsSync(lesson)) throw new Error('aula não encontrada');

const readJson=(file)=>JSON.parse(fs.readFileSync(file,'utf8'));
const plan=readJson(path.join(lesson,'storyboard','scene-plan.json'));
const audio=readJson(path.join(lesson,'voice','audio-manifest.json'));
const manifest=readJson(path.join(lesson,'source','slides-manifest.json'));
const configPath=path.join(lesson,'video-config.json');
const config=fs.existsSync(configPath)?readJson(configPath):{};
const defaultsPath=path.resolve('config/video-defaults.json');
const defaults=fs.existsSync(defaultsPath)?readJson(defaultsPath):{};
const brief=fs.existsSync(path.join(lesson,'lesson-brief.md'))?fs.readFileSync(path.join(lesson,'lesson-brief.md'),'utf8'):'';
const lessonTitle=brief.match(/- Tema:\s*(.+)/)?.[1]?.trim()||plan.lessonId;

const rt=path.resolve('remotion/public/runtime',plan.lessonId);
fs.rmSync(rt,{recursive:true,force:true});
fs.mkdirSync(path.join(rt,'slides'),{recursive:true});
fs.mkdirSync(path.join(rt,'audio'),{recursive:true});
fs.mkdirSync(path.join(rt,'linked-video'),{recursive:true});
for(const s of manifest.slides){const src=path.join(lesson,s.file);fs.copyFileSync(src,path.join(rt,'slides',path.basename(src)))}
for(const a of audio.segments){const src=path.join(lesson,a.file);fs.copyFileSync(src,path.join(rt,'audio',path.basename(src)))}

const resolveInput=(value)=>{
  if(!value)return undefined;
  const candidates=[path.resolve(lesson,value),path.resolve(value)];
  const found=candidates.find(fs.existsSync);
  if(!found)throw new Error(`vídeo configurado não encontrado: ${value}`);
  return found;
};
const duration=(file)=>{
  const r=spawnSync('ffprobe',['-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',file],{encoding:'utf8'});
  const seconds=Number(r.stdout.trim());
  if(r.status!==0||!Number.isFinite(seconds)||seconds<=0)throw new Error(`não foi possível determinar a duração de ${file}: ${r.stderr.trim()}`);
  return seconds;
};
const linkVideo=(value,name)=>{
  const src=resolveInput(value);
  if(!src)return undefined;
  const ext=path.extname(src)||'.mp4';
  const filename=`${name}${ext}`;
  fs.copyFileSync(src,path.join(rt,'linked-video',filename));
  return {file:`runtime/${plan.lessonId}/linked-video/${filename}`,durationSeconds:duration(src)};
};

const openingValue=option('--opening')??defaults.openingVideo??config.openingVideo;
const conclusionValue=option('--conclusion')??defaults.conclusionVideo??config.conclusionVideo;
const openingTitle=option('--opening-title')??config.openingTitle??lessonTitle;
const nextTopic=option('--next-topic')??config.nextTopic;
if(!openingValue||!conclusionValue)throw new Error('configure os vídeos padrão de abertura e conclusão no Estúdio antes de renderizar');
if(!String(nextTopic||'').trim())throw new Error('informe a próxima aula para personalizar o vídeo de encerramento');
const conclusionVideo=linkVideo(conclusionValue,'conclusion');
if(nextTopic&&!conclusionVideo)throw new Error('nextTopic requer conclusionVideo para ser exibido');
const props={
  lessonId:plan.lessonId,
  scenes:plan.scenes,
  audioSegments:audio.segments.map(a=>({id:a.id,durationSeconds:a.durationSeconds,file:`runtime/${plan.lessonId}/audio/${path.basename(a.file)}`})),
  slideBase:`runtime/${plan.lessonId}/slides`,
  openingVideo:linkVideo(openingValue,'opening'),
  openingTitle:openingTitle||undefined,
  conclusionVideo,
  nextTopic:nextTopic||undefined
};
fs.writeFileSync(path.join(rt,'props.json'),JSON.stringify(props,null,2));
console.log(path.join(rt,'props.json'));
