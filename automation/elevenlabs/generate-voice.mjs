import fs from 'node:fs'; import path from 'node:path'; import {spawnSync} from 'node:child_process';
function loadEnv(file){if(!fs.existsSync(file))return;for(const l of fs.readFileSync(file,'utf8').split(/\r?\n/)){if(!l||l.trim().startsWith('#'))continue;const i=l.indexOf('=');if(i>0&&!process.env[l.slice(0,i).trim()])process.env[l.slice(0,i).trim()]=l.slice(i+1).trim()}}
loadEnv(path.resolve('.env.local'));
const argv=process.argv.slice(2); const positional=argv.filter(a=>!a.startsWith('--'));
const lesson=path.resolve(positional[0]||''); const segFile=path.join(lesson,'voice','segments.json');
if(!fs.existsSync(segFile)){console.error('voice/segments.json não encontrado');process.exit(1)}
// --only SEG-000[,SEG-004] regera apenas os segmentos citados e preserva o áudio e as durações
// dos demais no manifest. Sem a flag, gera a aula inteira.
const onlyIdx=argv.findIndex(a=>a==='--only'||a.startsWith('--only='));
let only=null;
if(onlyIdx>=0){const raw=argv[onlyIdx].includes('=')?argv[onlyIdx].split('=').slice(1).join('='):argv[onlyIdx+1];
 if(!raw){console.error('--only exige lista de ids, ex.: --only SEG-000');process.exit(1)}
 only=new Set(raw.split(',').map(s=>s.trim()).filter(Boolean))}
const data=JSON.parse(fs.readFileSync(segFile,'utf8'));

// Abertura obrigatória: brain/opening-signature.md. Toda aula abre com a apresentação do
// instrutor, sem o usuário precisar pedir. Só o assunto varia; o resto é literal.
const nfc=s=>(s||'').normalize('NFC');
const OPENING=/^Olá, eu sou André Brazioli, diretor de pós-vendas na O L Tecnologia e especialista em redes\. Hoje falaremos sobre .+\. Vamos começar\?$/u;
if(process.env.SKIP_OPENING_CHECK!=='true'){
 const first=data.segments[0];
 if(!first||first.id!=='SEG-000') throw new Error('SEG-000 ausente: o primeiro segmento de voice/segments.json deve ser a abertura obrigatória de brain/opening-signature.md');
 if(!OPENING.test(nfc(first.text))) throw new Error(`SEG-000 divergente do texto canônico de brain/opening-signature.md.\nesperado: "Olá, eu sou André Brazioli, diretor de pós-vendas na O L Tecnologia e especialista em redes. Hoje falaremos sobre <assunto>. Vamos começar?"\nencontrado: "${first.text}"`);
}

const api=process.env.ELEVENLABS_API_KEY, voice=process.env.ELEVENLABS_VOICE_ID; if(!api||!voice) throw new Error('Configure ELEVENLABS_API_KEY e ELEVENLABS_VOICE_ID em .env.local');
const model=process.env.ELEVENLABS_MODEL_ID||'eleven_multilingual_v2'; const outFmt=process.env.ELEVENLABS_OUTPUT_FORMAT||'mp3_44100_128';
const stability=Number(process.env.ELEVENLABS_STABILITY||0.5), similarity=Number(process.env.ELEVENLABS_SIMILARITY_BOOST||0.75), style=Number(process.env.ELEVENLABS_STYLE||0), speaker=(process.env.ELEVENLABS_USE_SPEAKER_BOOST||'true')==='true';
const speed=Math.min(1.2,Math.max(0.7,Number(process.env.ELEVENLABS_SPEED||0.93))); // 1.0 = normal; <1 fala mais devagar
const outDir=path.join(lesson,'voice','generated');fs.mkdirSync(outDir,{recursive:true});
const manifestFile=path.join(lesson,'voice','audio-manifest.json');
const previous=new Map();
if(only&&fs.existsSync(manifestFile)) for(const s of JSON.parse(fs.readFileSync(manifestFile,'utf8')).segments||[]) previous.set(s.id,s);
if(only){const ids=new Set(data.segments.map(s=>s.id));for(const id of only) if(!ids.has(id)) throw new Error(`--only ${id}: id ausente de voice/segments.json`)}
const manifest={lessonId:data.lessonId,voiceId:voice,modelId:model,speed,segments:[]};
const probe=file=>{const p=spawnSync('ffprobe',['-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',file],{encoding:'utf8'});return Number((p.stdout||'').trim())};
for(const s of data.segments){
 const file=path.join(outDir,`${s.id}.mp3`);
 if(only&&!only.has(s.id)){
  const keep=previous.get(s.id);
  if(!keep||!fs.existsSync(file)) throw new Error(`${s.id}: sem áudio anterior para preservar; rode sem --only`);
  manifest.segments.push({...keep,text:s.text}); console.log(`↻ ${s.id} (${keep.durationSeconds.toFixed(2)}s, preservado)`);
  continue;
 }
 const res=await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${encodeURIComponent(voice)}?output_format=${encodeURIComponent(outFmt)}`,{method:'POST',headers:{'xi-api-key':api,'content-type':'application/json','accept':'audio/mpeg'},body:JSON.stringify({text:s.text,model_id:model,voice_settings:{stability,similarity_boost:similarity,style,use_speaker_boost:speaker,speed}})});
 if(!res.ok) throw new Error(`ElevenLabs ${s.id}: ${res.status} ${await res.text()}`);
 const buf=Buffer.from(await res.arrayBuffer());fs.writeFileSync(file,buf);
 const duration=probe(file);
 manifest.segments.push({id:s.id,file:`voice/generated/${s.id}.mp3`,durationSeconds:duration,text:s.text}); console.log(`✅ ${s.id} (${duration.toFixed(2)}s)`);
}
fs.writeFileSync(manifestFile,JSON.stringify(manifest,null,2));
console.log('Áudio concluído.');
