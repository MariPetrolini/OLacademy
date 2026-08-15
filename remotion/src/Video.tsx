import React from 'react';
import {AbsoluteFill,Audio,Img,Sequence,Video,interpolate,staticFile,useCurrentFrame,useVideoConfig} from 'remotion';

export type Overlay={type:string;x?:number;y?:number;w?:number;h?:number;label?:string;text?:string};
export type Scene={id:string;slideNumber:number;segmentIds:string[];overlays?:Overlay[];transition?:string;durationSeconds?:number};
export type AudioSeg={id:string;durationSeconds:number;file:string};
export type LinkedVideo={file:string;durationSeconds:number};
export type LessonProps={
  lessonId:string;
  scenes:Scene[];
  audioSegments:AudioSeg[];
  slideBase:string;
  openingVideo?:LinkedVideo;
  openingTitle?:string;
  conclusionVideo?:LinkedVideo;
  nextTopic?:string;
};

const BRAND_RED='#771215';
const SCRIM='rgba(0,0,0,.10)';
const frames=(sec:number,fps:number)=>Math.max(1,Math.round(sec*fps));
const lessonFrames=(p:LessonProps,fps:number)=>p.scenes.reduce((sum,s)=>sum+frames(s.segmentIds.reduce((a,id)=>a+(p.audioSegments.find(x=>x.id===id)?.durationSeconds||0),0)||s.durationSeconds||1,fps),0);
export const calcDuration=(p:LessonProps,fps:number)=>
  (p.openingVideo?frames(p.openingVideo.durationSeconds,fps):0)+
  lessonFrames(p,fps)+
  (p.conclusionVideo?frames(p.conclusionVideo.durationSeconds,fps):0);

const SceneView:React.FC<{scene:Scene;props:LessonProps}>=({scene,props})=>{const f=useCurrentFrame();const {fps}=useVideoConfig();const opacity=interpolate(f,[0,Math.min(12,Math.max(1,fps/2))],[0,1],{extrapolateRight:'clamp'});return <AbsoluteFill style={{backgroundColor:'#0b1220',opacity}}><Img src={staticFile(`${props.slideBase}/slide-${String(scene.slideNumber).padStart(3,'0')}.png`)} style={{width:'100%',height:'100%',objectFit:'contain'}}/>{(scene.overlays||[]).map((o,i)=>o.type==='highlight'?<div key={i} style={{position:'absolute',left:`${(o.x||0)*100}%`,top:`${(o.y||0)*100}%`,width:`${(o.w||.2)*100}%`,height:`${(o.h||.1)*100}%`,border:`5px solid ${BRAND_RED}`,borderRadius:14,boxSizing:'border-box',boxShadow:`0 0 0 9999px ${SCRIM}`}}/>:null)}</AbsoluteFill>};

const LinkedVideoView:React.FC<{video:LinkedVideo}>=({video})=><AbsoluteFill style={{backgroundColor:'#000'}}><Video src={staticFile(video.file)} style={{width:'100%',height:'100%',objectFit:'contain'}}/></AbsoluteFill>;

const OpeningView:React.FC<{video:LinkedVideo;title?:string}>=({video,title})=>{const frame=useCurrentFrame();const {fps}=useVideoConfig();const opacity=interpolate(frame,[Math.round(fps*.2),Math.round(fps*.65)],[0,1],{extrapolateLeft:'clamp',extrapolateRight:'clamp'});return <AbsoluteFill>
  <LinkedVideoView video={video}/>
  {title?<div style={{position:'absolute',left:110,right:110,bottom:90,padding:'28px 42px',background:'rgba(11,18,32,.88)',borderLeft:`10px solid ${BRAND_RED}`,borderRadius:16,color:'#fff',fontFamily:'Arial, sans-serif',boxShadow:'0 12px 36px rgba(0,0,0,.4)',opacity}}>
    <div style={{fontSize:30,textTransform:'uppercase',letterSpacing:3,opacity:.8}}>Nesta aula</div>
    <div style={{fontSize:58,fontWeight:700,lineHeight:1.12,marginTop:10}}>{title}</div>
  </div>:null}
</AbsoluteFill>};

const ConclusionView:React.FC<{video:LinkedVideo;nextTopic?:string}>=({video,nextTopic})=><AbsoluteFill>
  <LinkedVideoView video={video}/>
  {nextTopic?<div style={{position:'absolute',left:110,right:110,bottom:90,padding:'28px 42px',background:'rgba(11,18,32,.88)',borderLeft:`10px solid ${BRAND_RED}`,borderRadius:16,color:'#fff',fontFamily:'Arial, sans-serif',boxShadow:'0 12px 36px rgba(0,0,0,.4)'}}>
    <div style={{fontSize:30,textTransform:'uppercase',letterSpacing:3,opacity:.8}}>Próximo assunto</div>
    <div style={{fontSize:58,fontWeight:700,lineHeight:1.12,marginTop:10}}>{nextTopic}</div>
  </div>:null}
</AbsoluteFill>;

export const LessonVideo:React.FC<LessonProps>=(props)=>{const {fps}=useVideoConfig();let cursor=0;const output:React.ReactNode[]=[];
  if(props.openingVideo){const df=frames(props.openingVideo.durationSeconds,fps);output.push(<Sequence key="linked-opening" from={cursor} durationInFrames={df}><OpeningView video={props.openingVideo} title={props.openingTitle}/></Sequence>);cursor+=df;}
  for(const scene of props.scenes){const sceneSec=scene.segmentIds.reduce((a,id)=>a+(props.audioSegments.find(x=>x.id===id)?.durationSeconds||0),0)||scene.durationSeconds||1;const df=frames(sceneSec,fps);let ac=0;const audios=scene.segmentIds.map(id=>{const a=props.audioSegments.find(x=>x.id===id);if(!a)return null;const from=frames(ac,fps);ac+=a.durationSeconds;return <Sequence key={id} from={from} durationInFrames={frames(a.durationSeconds,fps)}><Audio src={staticFile(a.file)}/></Sequence>});output.push(<Sequence key={scene.id} from={cursor} durationInFrames={df}><SceneView scene={scene} props={props}/>{audios}</Sequence>);cursor+=df;}
  if(props.conclusionVideo){const df=frames(props.conclusionVideo.durationSeconds,fps);output.push(<Sequence key="linked-conclusion" from={cursor} durationInFrames={df}><ConclusionView video={props.conclusionVideo} nextTopic={props.nextTopic}/></Sequence>);}
  return <AbsoluteFill>{output}</AbsoluteFill>;
};
