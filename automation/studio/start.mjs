import {spawn} from 'node:child_process';
import path from 'node:path';
const root=path.resolve(import.meta.dirname,'../..');
const children=[spawn(process.execPath,['automation/studio/server.mjs'],{cwd:root,stdio:'inherit'}),spawn('npm',['run','dev'],{cwd:path.join(root,'studio'),stdio:'inherit'})];
const stop=()=>{for(const child of children)child.kill('SIGTERM')};process.on('SIGINT',stop);process.on('SIGTERM',stop);for(const child of children)child.on('exit',code=>{if(code){stop();process.exit(code)}});
