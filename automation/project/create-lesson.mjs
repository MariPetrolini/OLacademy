import fs from 'node:fs'; import path from 'node:path';
const [course, id, ...titleParts] = process.argv.slice(2); const title=titleParts.join(' ');
if(!course||!id||!title){console.error('uso: npm run lesson:new -- <curso> <lesson-id> "Título"');process.exit(1)}
const root=path.resolve('courses',course,'lessons',id);
for(const d of ['research','script','voice/generated','source/input','source/original','source/slides','source/extracted-media','storyboard','visuals','qa']) fs.mkdirSync(path.join(root,d),{recursive:true});
const brief=`# Lesson Brief\n\n- Lesson ID: ${id}\n- Tema: ${title}\n- Curso: ${course}\n- Público: \n- Pré-requisitos: \n- Objetivo de aprendizagem: \n- Duração alvo: \n- Escopo incluído: \n- Fora de escopo: \n`;
fs.writeFileSync(path.join(root,'lesson-brief.md'),brief);
fs.writeFileSync(path.join(root,'STATUS.md'),`# Status\n\nPHASE: RESEARCH\n\nPróximo: pesquisa oficial + especialistas.\n`);
fs.writeFileSync(path.join(root,'workflow-state.json'),JSON.stringify({lessonId:id,phase:'RESEARCH',humanCheckpoint:null},null,2));
console.log(root);
