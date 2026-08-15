# Resposta à revisão técnica #1

- Lesson ID: `fundamentos-01-modelo-osi`
- Parecer respondido: `qa/technical-review-1.md` — `VERDICT: BLOCKED`
- Respondido por: Claude Code (orquestrador/produtor), 2026-07-29
- Base: `CLAUDE.md`, Fase 3, item 9 — "Se houver erro CRITICAL/HIGH, corrija e peça nova revisão"

Cada achado foi avaliado no mérito antes de ser aceito. Nenhuma correção foi feita por deferência.

---

## TR1-001 — HIGH — ACEITO E CORRIGIDO

**Achado procede integralmente.** Era um erro meu, e pior: contradizia o meu próprio
`evidence-ledger.md`. O CLM-014 registra o verbatim do RFC 1122 como "the **top two** layers --
Presentation and Application", e ainda assim SEG-039 afirmava que a camada de aplicação da Internet
"cobre as três de cima do O S I". A camada de sessão foi incluída sem nenhuma fonte.

Corrigido em quatro lugares — o achado tinha propagado além do que o parecer apontou:

| Arquivo | Antes | Depois |
|---|---|---|
| `script/lesson-script.md`, SEG-039 | "cobre as três de cima do O S I" | "combina apresentação e aplicação do O S I" |
| `script/lesson-script.md`, SEG-030 | "não existem uma camada cinco e uma camada seis separadas" | agora ensina a **ausência**: o documento junta 6 e 7 e não dá destino nenhum à sessão |
| `script/on-screen-text.md`, Bloco 8 | restrição mandava Aplicação abranger 5, 6 e 7 | restrição agora manda abranger 6 e 7, com a camada 5 representada como **sem contraparte** |
| `research/research.md`, seções 6 e 9 | mesma sobre-extensão | precisão adicionada, separando fato de inferência |

Ganho didático colateral: a formulação corrigida é mais forte que a errada. A ausência de
contraparte para a sessão é exatamente o tipo de lacuna que o aluno precisa ver, e agora ela é
ensinada explicitamente em vez de encoberta por uma correspondência inventada.

## TR1-002 — HIGH — ACEITO E CORRIGIDO

**Achado procede.** SEG-015 apresentava retransmissão, ordenação e controle de fluxo como
comportamento da camada 4, o que ensina transporte ≡ TCP. UDP não oferece nenhuma das três. O erro é
especialmente ruim nesta aula, que combate justamente a confusão entre modelo e implementação.

SEG-015 reescrito. Agora diz explicitamente que transporte não é sinônimo de TCP, condiciona as três
garantias ao protocolo que as oferece, e fecha com "nem todo transporte oferece essas garantias".

## TR1-003 — MEDIUM — ACEITO E CORRIGIDO

**Achado procede.** A condição do X.200 é `act only as relay` [CLM-012], e eu generalizei para o
equipamento inteiro. Switches e roteadores reais terminam SSH, SNMP e HTTPS de gerenciamento.

SEG-018 reescrito: escopo restrito ao tráfego encaminhado, com ressalva explícita de que o
equipamento tem camadas altas para ser gerenciado e configurado.

## TR1-004 — MEDIUM — ACEITO E CORRIGIDO

**Achado procede.** "O programa mostra exatamente essa estrutura: uma linha por camada" prometia uma
dissecação linear e invariável, e a captura real nem existe para limitar o enunciado (OQ-001).

SEG-024 reescrito com formulação não absoluta ("em uma captura simples", "organiza a dissecação
pelos encapsulamentos") e ressalva de que com túnel a árvore fica mais funda. A confirmação contra
a captura real fica registrada para a adaptação ao PPT, na Fase 5.

## TR1-005 — MEDIUM — ACEITO, RESOLVIDO POR AJUSTE DE ESCOPO

**Achado procede.** O caminho escolhido foi ajustar o brief, não inflar o roteiro, porque a duração
já estava acima do teto (TR1-006) e porque duas das promessas eram problemáticas na origem:

- **"Camada 8"** estava no escopo do brief e, ao mesmo tempo, na tabela de **claims rejeitados** do
  `evidence-ledger.md`. O brief contradizia a pesquisa. Agora está explicitamente fora de escopo,
  com o motivo.
- **"PDU de cada camada"** nunca foi realizável: OQ-004 registra que não existe termo primário
  consagrado para as camadas 5, 6 e 7. Movido para fora de escopo, com a decisão de dizer ao aluno
  que ali a terminologia é frouxa em vez de inventar tabela.
- **VPN/tunelamento** agora aparece como uma oração em SEG-024 (efeito colateral do fix de
  TR1-004), e o brief registra que o desenvolvimento fica para curso posterior.
- O objetivo de aprendizagem foi ampliado para incluir a procedência dos nomes de PDU, que o
  roteiro entrega no bloco 7 e o brief não mencionava.

## TR1-006 — LOW — PARCIALMENTE RESOLVIDO, DECISÃO EDITORIAL PENDENTE

Os fixes de correção **adicionaram** 75 palavras (qualificações têm custo). Foram feitos dois novos
passes de compressão sobre material não sustentado por fonte:

| Momento | Palavras | Estimativa a 135 ppm |
|---|---|---|
| No parecer | 2.102 | 15,6 min |
| Após fixes de correção | 2.177 | 16,1 min |
| Após compressão | **2.066** | **15,3 min** |

Histórico completo: 2.567 → 2.171 → 2.102 → 2.177 → **2.066**.

Cortes desta rodada, todos em material opcional: menção ao RFC 3439 removida (CLM-019 sai do
roteiro; CLM-015, que é Standards Track, permanece); recitação das ferramentas de diagnóstico
enxugada, porque a tabela completa já está em `on-screen-text.md` e narrar a tabela inteira viola
"não exibir a narração inteira na tela"; e supressão de fechos meta redundantes.

**Restam 41 palavras acima do limiar de 2.025** que daria 15,0 min exatos a 135 ppm. A 137 ppm já
cabe. Não cortei mais porque o que resta carrega claim verificado. O parecer admite explicitamente
"obter decisão editorial explícita aceitando a duração antes da voz" como resolução válida — essa
decisão é do responsável e está pendente.

## TR1-007 — LOW — DECISÃO REGISTRADA, MANTIDO COMO ESTÁ

O vão `SEG-002` → `SEG-004` é **deliberado**. Surgiu de uma fusão de segmentos durante a compressão
de duração. A renumeração foi proposta ao responsável e **recusada por ele**; a instrução foi
prosseguir sem renumerar.

Conforme a própria recomendação do parecer ("manter se a estabilidade dos IDs for deliberada, mas
registrar a decisão"), a decisão fica registrada aqui e em `research/open-questions.md` (OQ-009).
Impacto verificado: nenhum. `generate-voice.mjs` usa `s.id` como nome de arquivo, e
`auto-storyboard.mjs` agrupa por `slide-map.json`, não por índice de segmento.

---

## Verificação após as correções

Reexecutada a validação automática sobre os 39 segmentos:

- sem markdown residual no texto falado — **um erro real capturado aqui**: a primeira versão do fix
  de SEG-035 deixou `**` no texto, que teria ido literal para a API. Corrigido.
- sem URL falada, sem ID duplicado, sem dêixis visual
- nenhum segmento acima de 45 s (maior: 40,9 s)
- `voice/segments.json` regenerado a partir do roteiro; os 39 textos conferem contra o markdown

## Situação dos vereditos

| Achado | Severidade | Situação |
|---|---|---|
| TR1-001 | HIGH | corrigido |
| TR1-002 | HIGH | corrigido |
| TR1-003 | MEDIUM | corrigido |
| TR1-004 | MEDIUM | corrigido |
| TR1-005 | MEDIUM | resolvido por ajuste de escopo no brief |
| TR1-006 | LOW | 15,6 → 15,3 min; decisão editorial pendente |
| TR1-007 | LOW | mantido, decisão registrada |

**Os dois HIGH estão fechados.** Nova revisão #1 solicitada conforme `CODEX.md`.
