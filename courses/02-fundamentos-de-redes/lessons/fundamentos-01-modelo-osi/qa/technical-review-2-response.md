# Resposta à revisão técnica #2

- Parecer respondido: `qa/technical-review-2.md` — `VERDICT: PASS_WITH_WARNINGS`
- Achados: 0 CRITICAL, 0 HIGH, 1 MEDIUM, 2 LOW
- Respondido por: Claude Code (orquestrador/produtor), 2026-07-29

Os três achados foram aceitos e tratados, embora nenhum bloqueasse o avanço.

---

## TR2-001 — MEDIUM — ACEITO E CORRIGIDO

**O achado procede, e é o espelho do TR1-001.** Ao corrigir "aplicação cobre 5, 6 e 7" eu passei do
ponto na direção oposta: escrevi "sessão sem contraparte" e "não dá nenhum destino para a camada de
sessão".

O que a fonte sustenta, e só isso:

- O RFC 1122 enumera **quatro** camadas, e sessão não está entre elas [CLM-013].
- Ele atribui à sua camada de aplicação as funções de apresentação e aplicação [CLM-014].
- Ele **não** diz o que acontece com as funções de sessão.

"Sem contraparte" afirma mais do que isso: sugere que não existem funções equivalentes em lugar
nenhum. E o próprio RFC 1122 registra que alguns protocolos de aplicação da Internet contêm
sub-camadas internas — o que torna a afirmação forte não só sem apoio, mas provavelmente falsa.

Formulação adotada: **"sem camada separada"**, mais o acréscimo explícito na narração de que isso
não significa que nada cuide de sessão na prática, apenas que a arquitetura da Internet não reserva
uma camada para ela.

Corrigido em seis lugares:

| Arquivo | O que mudou |
|---|---|
| `script/lesson-script.md`, SEG-030 | Reescrito, com a ressalva explícita |
| `voice/segments.json` | Regenerado a partir do roteiro |
| `source/slide-build/gen_slides.py` | Callout do slide 011 e cartão 05 do slide 015 |
| `source/slides/slide-011.png`, `slide-015.png` | Re-renderizados e **inspecionados visualmente** |
| `storyboard/build-scene-plan.py` | Rótulo do overlay de SEG-030 |
| `script/on-screen-text.md`, `research/research.md` | Restrição e precisão de pesquisa |

Corrigi a **fonte** dos slides, não os PNGs, para que a próxima regeração não reintroduza o erro —
foi exatamente assim que o TR1-001 voltou no primeiro deck.

**Defeito de processo encontrado no caminho:** a primeira tentativa de re-render rasterizou de
`source/slide-build/html`, uma pasta obsoleta, enquanto o gerador escreve em
`source/slide-build/slides_html`. Os slides saíram inalterados e eu só percebi porque fui conferir o
PNG em vez de confiar no "15/15 rasterizados". A pasta duplicada foi removida.

## TR2-002 — LOW — ACEITO E CORRIGIDO

Procede. `source/slide-analysis.md` declarava todas as divergências fechadas e afirmava que voz e
imagem coincidiam "sem ressalvas", enquanto TR2-001 estava aberto. Corrigido: os dois documentos
passam a registrar TR2-001 e seu fechamento, sem reabrir as seis divergências históricas do deck
original, que continuam fechadas.

## TR2-003 — LOW — ACEITO, REGISTRO ABERTO COM PENDÊNCIA SUA

Procede. Não havia registro de autoria e licença, exigido por `brain/source-policy.md`.

Criado `release/credits.md`, com a separação que importa:

- **Slides do vídeo:** material próprio, gerado por esta pipeline. Sem logo de terceiro, sem imagem
  de banco, sem arquivo de fonte incorporado. Risco nulo.
- **Deck original ingerido:** substituído, nenhum pixel dele no vídeo. Mas **três perguntas ficaram
  em aberto para você responder** antes do release: se o deck foi gerado por você a partir do texto
  desta aula, se a licença da ferramenta permite uso comercial, e se há terceiro a creditar.

Não declarei autoria em seu nome. A evidência sugere que o deck deriva do texto desta produção via
NotebookLM, mas a declaração é sua.

---

## Consequência processual

TR2-001 alterou **texto técnico falado**, além de dois slides e um overlay. Conforme
`CLAUDE.md` Fase 6 item 21 e a própria observação do parecer, **a revisão #2 precisa ser repetida**
antes de a Pausa Humana 2 valer.

## Estado dos artefatos após a correção

| Métrica | Valor |
|---|---|
| Segmentos | 40 |
| Palavras | 2.101 |
| Duração estimada | 15,6 min a 135 ppm (teto autorizado: 16) |
| Slides narrados | 15/15 |
| Segmentos com slide | 40/40 |
| Cenas | 40, sendo 12 com destaque |
| Slides em 1920×1080 | 15/15 |

Validações reexecutadas sem erro: `script/build-artifacts.py` e
`storyboard/build-scene-plan.py`.

| Achado | Severidade | Situação |
|---|---|---|
| TR2-001 | MEDIUM | corrigido em 6 arquivos; slides re-renderizados e conferidos |
| TR2-002 | LOW | documentação corrigida |
| TR2-003 | LOW | `release/credits.md` criado; 3 perguntas aguardam o responsável |
