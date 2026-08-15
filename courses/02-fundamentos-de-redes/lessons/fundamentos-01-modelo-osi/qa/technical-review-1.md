# Revisão técnica #1 — revalidação antes do PowerPoint

- Lesson ID: `fundamentos-01-modelo-osi`
- Revisor: Codex, revisão adversarial independente
- Data: 2026-07-29
- Escopo: `CODEX.md` e `agents/technical-reviewer.md`
- Substitui o veredito `BLOCKED` da primeira passagem após correções documentadas em
  `qa/technical-review-1-response.md`

## Fontes e artefatos auditados

- `lesson-brief.md`
- `research/research.md`
- `research/sources.md`
- `research/evidence-ledger.md`
- `research/open-questions.md`
- `script/lesson-script.md`
- `script/on-screen-text.md`
- `voice/segments.json`
- `qa/technical-review-1-response.md`
- ITU-T X.200 (07/94)
- RFC 1122, especialmente seções 1.1.3 e 1.3.1
- RFC 8446, seção 1
- RFC 9293, seção 2.2

## Fechamento dos bloqueadores anteriores

| ID | Severidade anterior | Resultado da revalidação |
|---|---|---|
| TR1-001 | HIGH | **FECHADO.** SEG-039 agora limita a correspondência documentada a Apresentação e Aplicação. SEG-029 também está coerente com o texto da RFC 1122. |
| TR1-002 | HIGH | **FECHADO.** SEG-015 distingue transporte de TCP, condiciona retransmissão, ordenação e controle de fluxo ao protocolo que oferece confiabilidade e registra que nem todo transporte oferece essas garantias. |
| TR1-003 | MEDIUM | **FECHADO NA NARRAÇÃO.** SEG-018 agora restringe a afirmação ao tráfego encaminhado e reconhece as camadas altas usadas para gerenciamento. Resta uma advertência visual, RV1-002. |
| TR1-004 | MEDIUM | **FECHADO.** SEG-024 passou a falar em captura simples, encapsulamentos e árvore mais profunda quando há túnel. |
| TR1-005 | MEDIUM | **PARCIALMENTE FECHADO.** O brief foi ajustado, mas ainda contém inconsistências internas descritas em RV1-003. |
| TR1-006 | LOW | **FECHADO POR DECISÃO EDITORIAL.** O responsável autorizou duração de até 16 minutos. A estimativa atual é 15,3 minutos a 135 palavras por minuto. |
| TR1-007 | LOW | **ACEITO.** O salto de SEG-002 para SEG-004 foi mantido por decisão registrada e não quebra as automações atuais. |

## Validações automáticas repetidas

- 39 segmentos no Markdown e 39 no JSON.
- 2.066 palavras; 15,30 minutos a 135 ppm.
- Textos do roteiro e de `voice/segments.json` idênticos.
- Nenhum ID duplicado.
- Nenhuma URL falada.
- Nenhum segmento estimado acima de 45 segundos; máximo de 40,9 segundos.
- Todos os IDs de claim usados no roteiro existem no ledger.

## Advertências remanescentes

| ID | Severidade | Arquivo/trecho | Problema | Evidência | Correção sugerida |
|---|---|---|---|---|---|
| RV1-001 | MEDIUM | `script/lesson-script.md`, SEG-030; `script/on-screen-text.md`, Bloco 8; `research/research.md`, seções 6 e 9 | “Sessão: sem contraparte” e “não dá nenhum destino” extrapolam a fonte. A RFC 1122 não define uma camada de Sessão separada e não a inclui na correspondência citada, mas isso não prova ausência de funções equivalentes dentro de protocolos de aplicação. | RFC 1122, 1.1.3, afirma somente que a camada de Aplicação combina essencialmente Apresentação e Aplicação e que não é subdividida. | Preferir: “a arquitetura da Internet não define uma camada de Sessão separada; a RFC 1122 não fornece aqui uma correspondência para ela”. Visualmente, marcar “sem camada separada” ou “sem mapeamento explícito”, não “sem contraparte”. |
| RV1-002 | MEDIUM | `script/on-screen-text.md`, Bloco 4, nota de SEG-018 | O texto visual ainda diz genericamente que switch e roteador “não têm pilha completa”, embora a narração já tenha corrigido essa generalização. | CLM-012 condiciona o caso aos sistemas que atuam apenas como relay; SEG-018 corrigido reconhece as camadas altas de gerenciamento. | Alinhar a nota visual à fala: “para encaminhar aquele tráfego, não precisam subir a pilha inteira”. |
| RV1-003 | MEDIUM | `lesson-brief.md`, progressão didática item 3 e seção fora de escopo | A progressão ainda promete “PDU e exemplo” para cada uma das sete camadas, enquanto a seção fora de escopo rejeita nomes de PDU para 5–7. Essa seção também afirma que a aula diz que a terminologia é frouxa, mas essa explicação não aparece na narração. | Comparação interna do brief com SEG-011 a SEG-017 e OQ-004. | Harmonizar o item 3 com o objetivo revisado: função de cada camada e terminologia PDU/SDU/PCI em separado. Remover a afirmação de que a fala explica “terminologia frouxa” ou acrescentar explicação sustentada. |

## Integridade para TTS

O texto está estruturalmente apto para segmentação. `framework` em SEG-026 e `TCP/IP` não espaçado
em SEG-006 permanecem como pontos de conferência do `voice-director`, sem impacto factual.

## Veredito

`VERDICT: PASS_WITH_WARNINGS`

Não há achado CRITICAL nem HIGH em aberto. As três advertências MEDIUM devem ser corrigidas
preferencialmente antes da adaptação ao PowerPoint e obrigatoriamente verificadas na revisão #2,
mas não impedem a Pausa Humana 1.
