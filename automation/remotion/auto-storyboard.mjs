import fs from 'node:fs'; import path from 'node:path';
const lesson=path.resolve(process.argv[2]||''); const mapPath=path.join(lesson,'script','slide-map.json'); const audioPath=path.join(lesson,'voice','audio-manifest.json');
if(!fs.existsSync(mapPath)||!fs.existsSync(audioPath)) throw new Error('slide-map.json e audio-manifest.json são necessários');
const map=JSON.parse(fs.readFileSync(mapPath,'utf8')), audio=JSON.parse(fs.readFileSync(audioPath,'utf8')); const dur=Object.fromEntries(audio.segments.map(s=>[s.id,s.durationSeconds]));
const groups=[]; for(const item of map.segments){let g=groups.at(-1);if(!g||g.slideNumber!==item.slideNumber){g={id:`SCN-${String(groups.length+1).padStart(3,'0')}`,slideNumber:item.slideNumber,segmentIds:[],overlays:[],transition:'fade'};groups.push(g)}g.segmentIds.push(item.segmentId)}
for(const g of groups) g.durationSeconds=g.segmentIds.reduce((a,id)=>a+(dur[id]||0),0);
const plan={lessonId:audio.lessonId,scenes:groups}; fs.mkdirSync(path.join(lesson,'storyboard'),{recursive:true}); fs.writeFileSync(path.join(lesson,'storyboard','scene-plan.json'),JSON.stringify(plan,null,2)); console.log(`Storyboard base: ${groups.length} cenas. Claude pode enriquecer overlays.`);
