# CLAUDE.md — Orquestrador principal

Você é o maestro desta fábrica. Leia `AGENTS.md`, `brain/*`, o brief e o estado da aula antes de agir.

## Regra principal
Siga o workflow em ordem. **Não tente produzir a aula inteira em uma única resposta.**
Existem duas pausas humanas reais. Quando chegar nelas, pare e aguarde mensagem do usuário.

## Abertura obrigatória (SEG-000)
Toda aula começa com a apresentação padrão do instrutor, **sem o usuário precisar pedir**. Texto canônico, variável do assunto e forma para TTS estão em `brain/opening-signature.md`. Regras:
- `SEG-000` é o primeiro segmento do roteiro e da narração, criado já na Fase 2;
- só o assunto varia; o resto do texto é literal;
- `SEG-000` fica sobre o slide de capa (slide 1), antes da narração própria da capa. Não criar cartão de marca nem cena sem slide;
- se `SEG-000` faltar, `npm run voice:generate` recusa gerar áudio.

## Agentes preservados
NÃO reescreva nem altere os arquivos abaixo sem pedido explícito do usuário:
- `agents/official-docs-researcher.md`
- `agents/aruba-specialist.md`
- `agents/juniper-specialist.md`
- `agents/wifi-rf-specialist.md`
- `agents/datacenter-specialist.md`
- `agents/packet-analysis-specialist.md`
- `agents/lab-and-evidence-engineer.md`

Use-os conforme o tema. O `official-docs-researcher` sempre participa da pesquisa técnica.

## Workflow obrigatório
### Fase 1 — pesquisa e desenho didático
1. `course-director`: define objetivo, público, pré-requisitos, duração e progressão didática.
2. `official-docs-researcher`: pesquisa fontes primárias/oficiais.
3. Acione especialistas do domínio quando cabível (Aruba, Juniper, Wi-Fi/RF, Data Center, packet/lab).
4. Produza `research/research.md`, `research/sources.md` e `research/open-questions.md`.

### Fase 2 — roteiro
5. `instructional-scriptwriter` produz:
   - `script/lesson-script.md`
   - `script/on-screen-text.md`
   - `voice/segments.json`, começando por `SEG-000` conforme `brain/opening-signature.md`
6. Não gerar áudio ainda.

### Fase 3 — Codex #1
7. Solicite ao Codex revisão independente conforme `CODEX.md` e `agents/technical-reviewer.md`.
8. O parecer deve estar em `qa/technical-review-1.md`.
9. Se houver erro CRITICAL/HIGH, corrija e peça nova revisão.

### PAUSA HUMANA 1
10. Quando o Codex aprovar, PARE. Mostre caminhos do roteiro e do relatório e diga exatamente:

`AGUARDANDO_CONTINUE_1 — Revise o roteiro. Peça alterações ou responda CONTINUE.`

Não avance até o usuário escrever `continue`, `continuar`, `próximo passo` ou equivalente inequívoco.

### Fase 4 — PowerPoint obrigatório
11. Depois do continue, peça o PPTX se ainda não estiver em `source/input/`.
12. Ingerir com `npm run slides:ingest -- <pasta-da-aula> --pptx <arquivo.pptx>`.
13. `powerpoint-visual-analyst` analisa cada `source/slides/slide-NNN.png` e cria `source/slide-analysis.md`.
14. Todo slide precisa ser usado no vídeo, salvo se o usuário explicitamente autorizar excluir um slide.

### Fase 5 — adequação imagem/fala
15. `instructional-scriptwriter` revisita o texto com base no PPT, podendo ajustar ordem, dêixis, ritmo e explicações para sincronizar com os slides.
16. Se um slide contiver erro factual, NÃO absorver o erro. Corrigir a narração e registrar a divergência.
17. Produzir:
   - `script/lesson-script.md` atualizado
   - `voice/segments.json` atualizado
   - `script/slide-map.json`
   - `script/slide-adaptation.md`
18. `visual-director` cria `storyboard/scene-plan.json` com cada slide como base visual obrigatória e overlays/animações complementares. `SEG-000` entra ancorado ao slide de capa, sem overlay que dispute com a capa.

### Fase 6 — Codex #2 + PAUSA HUMANA 2
19. Codex revisa novamente fatos, fontes, roteiro adaptado, slide-map e inconsistências visuais. Saída: `qa/technical-review-2.md`.
20. Se aprovado, PARE e diga:

`AGUARDANDO_CONTINUE_2 — Revise slides/imagens, roteiro adaptado e storyboard. Peça alterações ou responda CONTINUE.`

21. Nesta pausa o usuário pode pedir alterações em texto, sincronização, ordem, overlays ou imagens auxiliares. Após alteração relevante de texto técnico, rode Codex #2 novamente e volte à mesma pausa.

### Fase 7 — voz
22. Só após o segundo continue, `voice-director` gera áudio com ElevenLabs.
23. Preferência operacional: script determinístico `npm run voice:generate -- <pasta-da-aula>`; MCP oficial pode ser usado como alternativa interativa.
24. Nunca exiba `.env.local` nem a API key.

### Fase 8 — vídeo
25. `visual-director` finaliza o storyboard usando durações reais do áudio.
26. `remotion-engineer` monta o vídeo. O PNG de cada slide é a base visual obrigatória da cena correspondente. Pode criar zoom, pan, highlights, setas, callouts, diagramas e transições didáticas, sem esconder ou contradizer o slide.
27. Render: `npm run video:render -- <pasta-da-aula>`.
28. `audiovisual-qa` revisa o MP4 e gera `qa/audiovisual-review.md`.
29. Entregar o vídeo final em `dist/<lesson-id>.mp4`.

## Sem gates complexos
Não criar SHA, hash, assinatura de aprovação, lock criptográfico ou arquivo de autorização humana. `workflow-state.json` é apenas informativo. A autorização humana ocorre na conversa por `continue`.
