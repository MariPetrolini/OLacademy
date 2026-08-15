# Revisão técnica #2 — depois do PowerPoint

- Lesson ID: `fundamentos-01-modelo-osi`
- Revisor: Codex, revisão adversarial independente
- Data: 2026-07-29
- Escopo: `CODEX.md`, revisão #2, e `agents/technical-reviewer.md`

## Escopo

Foram auditados novamente fatos, fontes e roteiro, além dos 15 PNGs finais, análise visual,
adaptação aos slides, mapa de slides e storyboard. A inspeção visual considerou os PNGs atuais em
`source/slides/`, não o deck substituído preservado em `source/superseded-notebooklm/`.

## Artefatos auditados

- `lesson-brief.md`
- `research/research.md`
- `research/sources.md`
- `research/evidence-ledger.md`
- `script/lesson-script.md`
- `voice/segments.json`
- `source/slides/slide-001.png` a `slide-015.png`
- `source/slide-analysis.md`
- `script/slide-map.json`
- `script/slide-adaptation.md`
- `storyboard/scene-plan.json`
- ITU-T X.200 (07/94)
- RFC 1122, especialmente seções 1.1.3 e 1.3.1
- RFC 8446, seção 1
- RFC 9293, seção 2.2

## Verificações aprovadas

- Os 15 slides foram inspecionados visualmente.
- Todos estão em 1920×1080, sem letterbox nem marca d'água.
- As seis divergências do deck substituído foram corrigidas materialmente nos PNGs atuais:
  pilhas finais com sete camadas, LLC acima de MAC, FCS depois dos dados, escada de diagnóstico
  contínua e ausência de correspondência 1:1 entre sete e quatro camadas.
- 15/15 slides têm narração; 40/40 segmentos têm slide.
- A ordem do mapa é monotônica e nenhum slide foi excluído.
- `lesson-script.md` e `voice/segments.json` têm os mesmos 40 textos.
- Todo segmento possui `sourcePages`.
- O storyboard contém 40 cenas e cobre cada segmento exatamente uma vez.
- Não há coordenada de overlay fora do canvas, duração inválida ou referência a segmento
  inexistente.
- Os dois antigos achados HIGH da revisão #1 permanecem corrigidos.
- Nenhuma nova afirmação técnica sem fonte entrou durante a adaptação aos slides.
- A duração estimada é 15,5 minutos a 135 ppm, dentro do teto de 16 minutos autorizado pelo
  responsável.

## Achados

| ID | Severidade | Arquivo/trecho | Problema | Evidência | Correção sugerida |
|---|---|---|---|---|---|
| TR2-001 | MEDIUM | `script/lesson-script.md`, SEG-030; slides 011 e 015; `storyboard/scene-plan.json`, SCN-030; `research/research.md` | “Sessão: sem contraparte” e “não dá nenhum destino” são mais fortes que a fonte. A RFC 1122 não define uma camada de Sessão separada e não fornece ali um mapeamento explícito para ela, mas isso não demonstra ausência de funções equivalentes dentro de protocolos da camada de Aplicação. O destaque do storyboard reforça a formulação excessiva. | RFC 1122, 1.1.3: a camada de Aplicação combina essencialmente Apresentação e Aplicação e não é subdividida. A passagem não afirma “Session has no counterpart”. | Substituir em fala, slides e overlay por “sem camada separada” ou “sem mapeamento explícito na RFC 1122”. Depois regenerar somente os slides 011 e 015, o mapa não precisa mudar. |
| TR2-002 | LOW | `source/slide-analysis.md`, bloco “Divergências fechadas”; `script/slide-adaptation.md` | A documentação declara todas as divergências fechadas e diz que voz e imagem coincidem sem ressalvas, embora TR2-001 permaneça como advertência já identificada na revisão #1. Isso enfraquece a trilha de auditoria, ainda que mapa e cobertura estejam corretos. | Comparação entre `qa/technical-review-1.md` (RV1-001), SEG-030, slides 011/015 e os registros de fechamento. | Registrar TR2-001 como advertência aberta até a correção, sem reabrir as seis divergências históricas do deck original. |
| TR2-003 | LOW | `source/slides-manifest.json`, `source/slide-analysis.md` e árvore `source/` | A reconstrução e a origem técnica estão registradas, mas não foi localizado registro explícito de autoria/licença do PPTX original conforme `brain/source-policy.md`. Como os slides finais foram reconstruídos nativamente, o risco técnico é baixo, porém a comprovação deve existir antes da publicação. | `brain/source-policy.md` exige confirmação de autoria e licença antes da ingestão e créditos quando aplicáveis. | Registrar que o material é próprio da escola ou adicionar a atribuição/licença pertinente em `release/credits.md` antes do release. |

## Pontos obrigatórios para a implementação

- Os dez campos `wantedMotion` do storyboard são requisitos de implementação ainda não realizados,
  não defeitos desta fase. O `remotion-engineer` deve implementá-los ou justificar substituições
  equivalentes.
- OQ-001 continua bloqueando a evidência final em vídeo: slide 009 é um diagrama estrutural, não
  substitui a captura real prometida no brief.
- A revisão #2 deve ser repetida se TR2-001 alterar a fala, porque a mudança toca texto técnico,
  slides e overlay.

## Veredito

`VERDICT: PASS_WITH_WARNINGS`

Não há CRITICAL nem HIGH em aberto. A aula pode seguir para a Pausa Humana 2, com TR2-001
explicitamente apresentado ao responsável e obrigatório na conferência antes da voz.
