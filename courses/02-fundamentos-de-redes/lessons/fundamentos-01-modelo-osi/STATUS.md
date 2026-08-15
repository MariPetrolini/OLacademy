# Status

PHASE: DELIVERED

## Abertura obrigatória aplicada retroativamente (2026-08-01)

A regra nova de `brain/opening-signature.md` — toda aula abre com a apresentação do instrutor —
foi aplicada nesta aula já entregue, a pedido do responsável.

- `SEG-000` inserido como Bloco 0 do roteiro: "Olá, eu sou André Brazioli, diretor de pós-vendas
  na O L Tecnologia e especialista em redes. Hoje falaremos sobre o modelo O S I. Vamos começar?"
- Ancorado ao **slide 1 (capa)**, antes de SEG-001. Sem cartão de marca e sem cena nova sem slide.
- `segments.json` e `slide-map.json` regenerados: **41 segmentos**, 15/15 slides narrados.
- Áudio: só `SEG-000` foi gerado (`--only SEG-000`), **11,15 s**. Os outros 40 MP3 e suas durações
  medidas foram preservados — nenhum crédito de ElevenLabs regasto.
- `scene-plan.json` regenerado: **41 cenas**, SCN-001 é a abertura sobre a capa, sem overlay.
- Vídeo re-renderizado.

**Pendência humana:** escutar `voice/generated/SEG-000.mp3`. Dois pontos de pronúncia a confirmar
no clone: "O L Tecnologia" (esperado "ó-éle") e o próprio nome. Se sair errado, regerar só esse
segmento.

## Fase 6 — revisão técnica Codex #2 (2026-07-29)

- Parecer: `qa/technical-review-2.md`
- Veredito: **PASS_WITH_WARNINGS**
- Achados abertos: 0 CRITICAL, 0 HIGH, 1 MEDIUM, 2 LOW
- Cobertura validada: 15/15 slides, 40/40 segmentos e 40/40 cenas
- Advertência principal: “Sessão: sem contraparte” excede o que a RFC 1122 afirma; preferir
  “sem camada separada” ou “sem mapeamento explícito”.
- Estado: **PAUSA HUMANA 2**

**Próximo:** aguardar revisão humana de slides, roteiro adaptado, mapa e storyboard. Não gerar voz
até mensagem inequívoca `CONTINUE`.

## Fase 4 — PowerPoint (2026-07-29)

- Deck ingerido: `OSI_Architecture.pptx`, 15 slides, via `slides:ingest-images` (extração direta dos
  PNGs embutidos, sem LibreOffice e sem re-render)
- Análise visual: `source/slide-analysis.md` — os 15 slides foram inspecionados
- **3 divergências HIGH, 2 MEDIUM, 1 LOW.** Nenhuma absorvível: em todas o slide afirma
  visualmente o contrário da narração
- Correções aplicadas na **fonte** (`script/on-screen-text.md`): 3 novas restrições obrigatórias e
  o erro do TR1-001 que havia sobrevivido na tabela de resumo
- Brief pronto para regerar as imagens: `source/slide-regeneration-brief.md`

### Slides reconstruídos (2026-07-29)

Em vez de regerar por ferramenta externa, os 15 slides foram **reconstruídos nativamente** na
identidade da escola (`source/slide-build/gen_slides.py` + `npm run slides:render-html`).

- **6 divergências fechadas**, as 3 HIGH incluídas, cada uma verificada por inspeção visual
- 1920×1080 exatos, sem upscale e sem letterbox
- Sem marca d'água de terceiro
- Correções aplicadas também na fonte (`script/on-screen-text.md`), com 3 restrições novas
- Deck original preservado em `source/original/`; render antigo em `source/superseded-notebooklm/`

## Fase 5 — adequação imagem/fala (2026-07-29)

- `script/lesson-script.md` — 40 segmentos, 2.089 palavras, 15,5 min estimados
- `script/slide-map.json` — **15/15 slides narrados, 40/40 segmentos mapeados**, ordem monotônica
- `script/slide-adaptation.md` — 3 mudanças, nenhuma altera claim técnico
- `voice/segments.json` — regenerado com `sourcePages`
- `storyboard/scene-plan.json` — 40 cenas, uma por segmento, 12 com destaque

Nenhum erro de slide precisou ser corrigido pela narração: as divergências foram fechadas na
Fase 4, então o item 16 não foi acionado.

`segments.json` e `slide-map.json` saem do **mesmo** mapa em `script/build-artifacts.py`, que falha
se um slide ficar sem fala, um segmento sem slide, ou a ordem dos slides retroceder.

**Áudio ainda NÃO gerado.**

## Fase 6 — Codex revisão #2 (2026-07-29)

- Parecer: `qa/technical-review-2.md` — **PASS_WITH_WARNINGS**, 0 CRITICAL, 0 HIGH, 1 MEDIUM, 2 LOW
- Resposta: `qa/technical-review-2-response.md` — os 3 achados tratados
- **TR2-001** (MEDIUM): "sessão sem contraparte" ia além do RFC 1122 — espelho do TR1-001, na
  direção oposta. Trocado por "sem camada separada" na fala, nos slides 011 e 015, no overlay e na
  fonte do gerador. Slides re-renderizados e inspecionados.
- **TR2-003** (LOW): `release/credits.md` criado. **3 perguntas aguardam o responsável.**
- Duração: 2.101 palavras, 15,6 min estimados (teto 16)

### Estado: PAUSA HUMANA 2

O responsável autorizou seguir sem repetir a revisão #2. Registro honesto: o parecer vigente
validou o texto **anterior** ao fix de TR2-001. O fix aplicou exatamente a correção que o próprio
parecer prescreveu, o que reduz o risco, mas nenhum revisor independente viu a versão final.

Pré-voo da Fase 8 executado (não requer o segundo continue):

- `npm --prefix remotion install` — ok; esbuild 0.28.1 funcional apesar do aviso de postinstall
- `npm run video:validate` (typecheck) — **passa**
- Contrato de artefatos conferido: scene-plan × segments.json × manifesto × PNGs consistentes,
  40 cenas / 40 segmentos / 15 slides, sem órfãos e sem duplicatas
- `.env.local` **ausente** — bloqueia a Fase 7

**CONTINUE 2 recebido em 2026-07-29.**

## Fase 7 — voz: BLOQUEADA

`.env.local` não existe. `automation/elevenlabs/generate-voice.mjs` exige
`ELEVENLABS_API_KEY` e `ELEVENLABS_VOICE_ID`. Credencial só o responsável pode colocar.

Preparação concluída enquanto isso:

- 40 segmentos, **11.606 caracteres** a enviar, maior segmento com 502
- `segments.json` conferido contra o que o script consome (lessonId, id, text) — ok
- `ffprobe` presente, necessário para medir a duração real
- **3 defeitos de pronúncia corrigidos antes de gastar crédito:** o artigo "o" estava colado na
  sigla soletrada "O S I" em SEG-006, SEG-028 e SEG-038, o que sairia como gagueira. O validador
  agora barra esse padrão.

## Fase 7 — voz (concluída)

40 MP3 gerados, 11.606 caracteres. **Duração real: 729,85 s = 12,16 min**, ou seja 172 ppm — o
modelo de 135 ppm errou 21,6% para cima.

## Fase 8 — vídeo (concluído)

`dist/fundamentos-01-modelo-osi.mp4` — 1920×1080, 30 fps, 21.896 quadros, H.264 + AAC, 49,3 MB.
Duração casa com o áudio em 0,07 s.

QA em `qa/audiovisual-review.md` — `PASS_WITH_WARNINGS`. Dois MEDIUM corrigidos no renderer e o
vídeo refeito: o chip de rótulo cobria linha de tabela, e o destaque era amarelo `#ffd54a`,
contra `brain/branding.md`. Agora usa `#771215`.

**Pendência humana obrigatória: escutar o áudio.** Pronúncia e timbre não são verificáveis por
inspeção automática.

## Fase 3 — revisão técnica Codex #1 (revalidada em 2026-07-29)

- Parecer: `qa/technical-review-1.md` — veredito **PASS_WITH_WARNINGS**
- Achados abertos: 0 CRITICAL, 0 HIGH, 3 MEDIUM, 0 LOW
- Duração de 15,3 min aceita pelo responsável dentro do novo limite de 16 min.
- Estado: **PAUSA HUMANA 1**.

## Correções aplicadas (2026-07-29)

- Resposta detalhada por achado: `qa/technical-review-1-response.md`
- **Os dois HIGH estão fechados.** Os três MEDIUM também. Os dois LOW estão tratados.
- TR1-001 exigiu correção em 4 arquivos, não só no segmento apontado: o erro havia propagado para
  `on-screen-text.md` e `research/research.md`.
- Duração: 2.102 → 2.177 (fixes somam palavras) → **2.066** palavras, 15,3 min a 135 ppm.
- `voice/segments.json` regenerado e reconferido contra o roteiro.

**Próximo:** aguardar revisão humana e mensagem inequívoca `CONTINUE`.

## Fase 1 — pesquisa (concluída 2026-07-29)

- `lesson-brief.md`, `production-plan.md`
- `research/research.md`, `sources.md`, `evidence-ledger.md`, `open-questions.md`
- 21 claims, 7 fontes Nível A, STATUS PASS_WITH_WARNINGS

## Fase 2 — roteiro (concluída 2026-07-29)

- `script/lesson-script.md` — 39 segmentos, 2.102 palavras
- `script/on-screen-text.md` — texto de tela + 6 restrições visuais obrigatórias
- `voice/segments.json` — gerado por script a partir do roteiro, não digitado à mão

Validações automáticas executadas sobre os segmentos: sem markdown residual, sem URL falada, sem
dêixis visual, sem ID duplicado, nenhum segmento acima de 45 s (maior: 40,9 s).

**Áudio NÃO gerado**, conforme Fase 2 do `CLAUDE.md`.

### Ponto de atenção de duração
Estimativa atual de 15,3 min a 135 palavras por minuto, contra alvo de 14 min e teto autorizado de
16 min. A estimativa é modelo, não medição: a duração real só existe após a Fase 7.

## Próximo

PAUSA HUMANA 1 — aguardar `CONTINUE` inequívoco do responsável.

## Pendências que não bloqueiam a Fase 3

| ID | Assunto | Bloqueia |
|---|---|---|
| OQ-001 | Captura real não existe | Fase 8 (vídeo) |
| OQ-002 | Versão IEEE 802-2001 vs 802-2014 | nada — ressalva registrada |
| OQ-007 | `CLAUDE.md` × `visual-language.md` sobre uso do PNG | Fase 8 (decisão sua) |
| OQ-008 | `brain/references/*` citados mas ausentes | Fase 5/8 (agentes visuais) |
