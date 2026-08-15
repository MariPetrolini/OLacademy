import fs from 'node:fs'; import path from 'node:path';
const lesson=path.resolve(process.argv[2]||''); if(!fs.existsSync(lesson)){console.error('aula não encontrada');process.exit(1)}
const state=path.join(lesson,'workflow-state.json'); if(fs.existsSync(state)) console.log(fs.readFileSync(state,'utf8')); else console.log(fs.readFileSync(path.join(lesson,'STATUS.md'),'utf8'));
