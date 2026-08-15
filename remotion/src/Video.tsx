import React from 'react'; import {AbsoluteFill,Audio,Img,Sequence,interpolate,staticFile,useCurrentFrame,useVideoConfig} from 'remotion';
export type Overlay={type:string;x?:number;y?:number;w?:number;h?:number;label?:string;text?:string};
export type Scene={id:string;slideNumber:number;segmentIds:string[];overlays?:Overlay[];transition?:string;durationSeconds?:number};
export type AudioSeg={id:string;durationSeconds:number;file:string};
export type LessonProps={lessonId:string;scenes:Scene[];audioSegments:AudioSeg[];slideBase:string};
// Tokens de brain/branding.md. O destaque usava #ffd54a (amarelo), que competia com o
// vermelho da marca e nao era token declarado. O `label` do overlay deixou de ser
// desenhado: o chip ficava 52px acima da caixa e cobria a linha vizinha em destaque de
// tabela, e o texto duplicava a narracao, contra a regra de nao pôr a fala na tela.
// O campo `label` segue no scene-plan como registro de intencao.
const BRAND_RED='#771215';
const SCRIM='rgba(0,0,0,.10)';
const frames=(sec:number,fps:number)=>Math.max(1,Math.round(sec*fps));
export const calcDuration=(p:LessonProps,fps:number)=>p.scenes.reduce((sum,s)=>sum+frames(s.segmentIds.reduce((a,id)=>a+(p.audioSegments.find(x=>x.id===id)?.durationSeconds||0),0)||s.durationSeconds||1,fps),0);
const SceneView:React.FC<{scene:Scene;props:LessonProps}>=({scene,props})=>{const f=useCurrentFrame();const {fps}=useVideoConfig();const opacity=interpolate(f,[0,Math.min(12,Math.max(1,fps/2))],[0,1],{extrapolateRight:'clamp'});return <AbsoluteFill style={{backgroundColor:'#0b1220',opacity}}><Img src={staticFile(`${props.slideBase}/slide-${String(scene.slideNumber).padStart(3,'0')}.png`)} style={{width:'100%',height:'100%',objectFit:'contain'}}/>{(scene.overlays||[]).map((o,i)=>o.type==='highlight'?<div key={i} style={{position:'absolute',left:`${(o.x||0)*100}%`,top:`${(o.y||0)*100}%`,width:`${(o.w||.2)*100}%`,height:`${(o.h||.1)*100}%`,border:`5px solid ${BRAND_RED}`,borderRadius:14,boxSizing:'border-box',boxShadow:`0 0 0 9999px ${SCRIM}`}}/>:null)}</AbsoluteFill>}
export const LessonVideo:React.FC<LessonProps>=(props)=>{const {fps}=useVideoConfig();let cursor=0;return <AbsoluteFill>{props.scenes.map(scene=>{const sceneSec=scene.segmentIds.reduce((a,id)=>a+(props.audioSegments.find(x=>x.id===id)?.durationSeconds||0),0)||scene.durationSeconds||1;const df=frames(sceneSec,fps);let ac=0;const audios=scene.segmentIds.map(id=>{const a=props.audioSegments.find(x=>x.id===id);if(!a)return null;const from=frames(ac,fps);ac+=a.durationSeconds;return <Sequence key={id} from={from} durationInFrames={frames(a.durationSeconds,fps)}><Audio src={staticFile(a.file)}/></Sequence>});const seq=<Sequence key={scene.id} from={cursor} durationInFrames={df}><SceneView scene={scene} props={props}/>{audios}</Sequence>;cursor+=df;return seq})}</AbsoluteFill>}
