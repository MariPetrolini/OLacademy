# Análise visual dos slides — fundamentos-01-modelo-osi

---

# ⬛ RESOLUÇÃO (2026-07-29) — slides reconstruídos, divergências fechadas

O deck analisado abaixo **foi substituído**. Em vez de regerar por ferramenta externa, os 15 slides
foram **reconstruídos nativamente** na identidade da escola:

- Gerador: `source/slide-build/gen_slides.py` (HTML/SVG, tokens de `brain/branding.md`)
- Rasterização: `npm run slides:render-html` → Chrome headless
- Saída: `source/slides/slide-001.png` … `slide-015.png`, **todos 1920×1080 exatos**
- Deck original preservado em `source/original/deck.pptx`; render antigo em
  `source/superseded-notebooklm/`

## Divergências fechadas

| ID | Severidade | O que foi feito | Verificado |
|---|---|---|---|
| DIV-001 | HIGH | Cartão 05 do resumo agora diz "aplicação combina 6 e 7. Sessão sem camada separada" | ✅ slide 015 inspecionado |
| DIV-002 | HIGH | Machine A e B com as **sete** camadas, idênticas; relay com 1–3 | ✅ slide 006 inspecionado |
| DIV-005 | HIGH | **LLC acima de MAC** | ✅ slide 012 inspecionado |
| DIV-003 | MEDIUM | Colchete liga só 6 e 7 a "Aplicação"; camada 5 isolada, sem ligação, marcada em vermelho | ✅ slide 011 inspecionado |
| DIV-006 | MEDIUM | Escada 1–2–3 no slide 013 e 4 / 5–7 no slide 014, sem repetir nem omitir; faixa não cobre degrau | ✅ slides 013 e 014 inspecionados |
| DIV-004 | LOW | "Camada" grafado corretamente | ✅ slide 004 inspecionado |

## Observações fechadas

- **OBS-001** — marca d'água de terceiro: eliminada. Nenhuma marca no material.
- **OBS-002** — resolução: 1376×768 → **1920×1080**. Upscale zero.
- **OBS-003** — proporção: agora exatamente 16:9. Sem letterbox.
- **OBS-004** — tipografia: monoespaçada restrita a string técnica (siglas de norma, LLC/MAC,
  termos procurados, rótulos de dado). Prosa em sans.
- **OBS-005** — slide 006 continua acumulando dois focos. Mantido, resolvível por revelação
  progressiva na Fase 5.
- **OBS-006** — slide 003 recomposto, rótulos na horizontal.

## Defeitos encontrados na própria reconstrução e corrigidos

Registrado porque a primeira rasterização não saiu limpa:

| Slide | Defeito | Correção |
|---|---|---|
| 004 | Texto atravessado pela linha vermelha da camada 3; colchete malformado; rótulos "Machine A/B" cortados na base | Rótulo movido acima da linha; colchete redesenhado como geometria previsível; altura do SVG de 620 → 680 |
| 013, 014 | Texto de evidência transbordando as caixas da escada | Caixa de 480 → 660 px, deslocamento reduzido |
| 014 | Escada empurrada para fora do quadro e faixa preta ocupando um terço do slide | Escada reancorada à esquerda com rótulo de continuação; faixa com `flex:none` |
| 002 | O "X" cobria só o topo da coluna | SVG sem altura explícita caía no default de 150 px; corrigido para 100% |
| 008 | Rótulo "Exemplo Ethernet: FCS no fim do quadro." truncado na borda | Reposicionado à esquerda, abaixo da barra |

**Todos os 15 slides foram abertos e inspecionados visualmente após a correção final.**

## Ressalva posterior — TR2-001 (revisão técnica #2)

As seis divergências acima seguem fechadas. Mas a revisão #2 apontou que a formulação **"sessão sem
contraparte"**, usada nos slides 011 e 015 e na narração, ia além do que o RFC 1122 sustenta — o
espelho do erro TR1-001, agora na direção oposta.

Trocado por **"sem camada separada"** nos dois slides e na fala, com a fonte
(`source/slide-build/gen_slides.py`) corrigida antes do re-render. Slides 011 e 015 re-renderizados
e inspecionados. Ver `qa/technical-review-2-response.md`.

Portanto: a afirmação de que voz e imagem coincidem vale **após** essa correção, não antes dela.

## Reprodutibilidade

```bash
python3 source/slide-build/gen_slides.py
npm run slides:render-html -- <aula>/source/slide-build/slides_html <aula>/source/slides
```

O `slides-manifest.json` declara `ingestMode: native-html-rebuild` e **não** afirma que os PNGs
derivam do PPTX — eles não derivam.

---

# Análise do deck original (histórico)

O que segue é a análise que motivou a reconstrução. Mantida como registro de auditoria.

- Deck: `source/original/deck.pptx` (`OSI_Architecture.pptx`, 9,4 MB)
- 15 slides, ingeridos em 2026-07-29 por `ingest-pptx-images.mjs` (extração direta, sem re-render)
- Analista: `powerpoint-visual-analyst`
- Cada um dos 15 PNGs foi aberto e inspecionado visualmente

## Natureza do deck

Os 15 slides **não têm nenhum texto editável**: cada slide é uma única imagem PNG em full-bleed
(`blips=1, shapes=0, runs=0` em todos). O deck é um contêiner de imagens, não uma apresentação
editável.

Consequência prática: **não é possível corrigir um erro editando o slide.** Qualquer correção exige
regerar a imagem. Isso pesa na decisão do fim deste documento.

O conteúdo dos slides deriva de `script/on-screen-text.md` — eyebrows, títulos e blocos coincidem
com o que o roteirista especificou. **Mas deriva da versão anterior à correção do TR1-001**, e por
isso reintroduz o erro que o Codex havia bloqueado (ver DIV-001).

## Restrições atendidas

Três das seis restrições visuais obrigatórias de `script/on-screen-text.md` foram respeitadas, e
são justamente as mais fáceis de errar:

- **Restrição 1** — nenhum ícone ou nome de protocolo dentro das caixas das sete camadas (slide 5). ✅
- **Restrição 2** — o slide 8 mostra `DADOS | FCS`, com a informação de controle **depois** dos
  dados, e o modelo `HEADER | DATA` riscado. Exatamente o que a narração afirma. ✅
- **Restrição 4** — o slide 9 representa o encapsulamento como caixas aninhadas, **sem** simular
  tela de analisador nem exibir valor concreto. Respeita OQ-001. ✅
- **Restrição 5** — slides 13 e 14 trazem o eyebrow `MÉTODO DA ESCOLA — NÃO É NORMA`. ✅
- **Restrição 6** — o slide 10 reproduz a tabela de contagem e a linha de procedência corretamente,
  sem atribuir quadro/pacote/segmento ao OSI. ✅

## Slide a slide

| # | Eyebrow / título | Segmentos correspondentes | Situação |
|---|---|---|---|
| 001 | O PROBLEMA — "Nada disso foi testado junto." | SEG-001, SEG-002 | OK |
| 002 | A NORMA — "Open Systems Interconnection" | SEG-004, SEG-005, SEG-006 | OK |
| 003 | CONCEITO-CHAVE — "Serviço não é protocolo." | SEG-007 | OK, com ressalva de layout |
| 004 | A ENGRENAGEM — "Entidades pares e aprimoramento passo a passo." | SEG-008, SEG-010 | **DIV-004** (erro de digitação) |
| 005 | AS SETE CAMADAS | SEG-011 a SEG-017 | OK — melhor slide do deck |
| 006 | DEFINIÇÃO EXATA + "Passagem, não destino." | SEG-014, SEG-018 | **DIV-002** (camadas faltando) + slide sobrecarregado |
| 007 | PASSO 1 DE 3 — "SDU + PCI = PDU" | SEG-019 | OK |
| 008 | ERRO COMUM — "O cabeçalho não vai necessariamente na frente." | SEG-020, SEG-022 | OK — exemplar |
| 009 | EVIDÊNCIA — "A mesma estrutura, em bytes." | SEG-021, SEG-023, SEG-024 | OK |
| 010 | RIGOR DE FONTE — "Esses nomes não são do OSI." | SEG-025, SEG-026, SEG-027 | OK — exemplar |
| 011 | OSI × INTERNET — "Por que tanta gente desenha quatro." | SEG-028, SEG-029, SEG-030, SEG-031 | **DIV-003** (agrupamento contradiz o rótulo) |
| 012 | "NEM TUDO TEM NÚMERO" — Camada 2 / TLS | SEG-032 | **DIV-005** (LLC e MAC invertidos) |
| 013 | MÉTODO DA ESCOLA — "Diagnóstico: de baixo para cima." | SEG-033, SEG-034, SEG-035 | OK |
| 014 | MÉTODO DA ESCOLA (continuação) | SEG-036, SEG-037 | **DIV-006** (degrau 3 ausente, degrau 2 repetido) |
| 015 | RESUMO + SEU EXERCÍCIO | SEG-038, SEG-039, SEG-040 | **DIV-001** (erro HIGH reintroduzido) |

Cobertura: **todos os 11 blocos do roteiro têm slide.** Nenhum slide é dispensável, e nenhum slide
está órfão. A proporção de 15 slides para 39 segmentos significa que vários slides sustentam mais de
um segmento — o casamento exato é trabalho do `slide-map.json`, na Fase 5.

---

## Divergências — slide × fonte primária

Registradas conforme `CLAUDE.md`, Fase 5, item 16: erro de slide **não é absorvido**. A narração
corrige e a divergência fica registrada.

### DIV-001 — HIGH — slide 015, cartão 05: reintroduz o erro do TR1-001

O cartão diz: *"Internet real | Quatro camadas; aplicação **cobre 5, 6 e 7**."*

É exatamente o erro que o Codex classificou como HIGH em TR1-001 e que já foi corrigido no roteiro.
`CLM-014` registra o verbatim do RFC 1122: a camada de aplicação da Internet combina as funções das
**duas** camadas mais altas — apresentação e aplicação. A camada de sessão não é atribuída ali.

Causa: o deck foi gerado a partir do `on-screen-text.md` **antes** da correção.

**Contradição direta com a narração.** SEG-039 hoje diz "combina apresentação e aplicação do O S I".
Se este slide entrar como está, o aluno lê no slide o oposto do que ouve.

Correção no slide: `Quatro camadas; aplicação combina 6 e 7. Sessão: sem contraparte.`

### DIV-002 — HIGH — slide 006: as pilhas de camadas estão erradas

As duas pilhas de sistema final têm apenas seis caixas, e cada uma omite uma camada diferente:

- **Machine A**: 7, 6, **4**, 3, 2, 1 — a camada **5 (sessão) está ausente**
- **Machine B**: 7, 6, **5**, 3, 2, 1 — a camada **4 (transporte) está ausente**
- Relay Router: 3, 2, 1 — correto

Contradiz `CLM-001`, que é o claim mais básico da aula: o modelo tem sete camadas, e a aula acabou
de enumerá-las no slide 5. Um sistema final com seis camadas, e duas pilhas discordando entre si,
desmonta o que o slide anterior ensinou.

Agravante: este slide é o único do deck que aparece **imediatamente depois** da enumeração das sete
camadas, onde o aluno está formando a imagem mental da pilha.

### DIV-003 — MEDIUM — slide 011: o agrupamento visual contradiz o próprio rótulo

O slide traz o rótulo correto — *"Sessão: sem contraparte"* — mas o desenho agrupa **7, 6 e 5 na
mesma caixa**, com uma única chave ligando o grupo ao bloco "Aplicação" do RFC 1122. Ou seja: o
texto diz que sessão não tem contraparte, e o diagrama mostra sessão mapeada para a aplicação.

É a correção do TR1-001 aplicada pela metade: o rótulo entrou, o agrupamento não foi refeito.

Correção no slide: separar a camada 5 do grupo 6–7. A chave liga apenas 6 e 7 a "Aplicação"; a
camada 5 fica isolada, sem chave e sem linha tracejada.

### DIV-004 — LOW — slide 004: erro de digitação

*"**Camad** 3 fala com camada 3"* — falta o "a" em "Camada". Visível, em texto de destaque.

### DIV-005 — HIGH — slide 012: LLC e MAC estão invertidos

O diagrama empilha **MAC em cima, LLC embaixo**. Está invertido.

`CLM-018` traz o verbatim do IEEE Std 802: *"the Data Link layer is structured as two sublayers,
with the **LLC sublayer operating over a MAC sublayer**"* — e ainda: *"The MAC sublayer of the
LAN&MAN/RM exists **between the Physical layer and the LLC sublayer**"*. LLC fica acima de MAC.

Erro de conceito, não de estética: a ordem das sub-camadas é a informação que o slide existe para
transmitir. E é especialmente ruim numa aula cujo tema é ordem de camadas.

Correção no slide: trocar as duas faixas de posição — LLC acima, MAC abaixo.

### DIV-006 — MEDIUM — slide 014: escada inconsistente com o slide 013

O slide 013 mostra os degraus 1, 2 e 3. O slide 014, que continua a mesma escada, mostra **2, 4 e
5–7**: o degrau **3 desapareceu** e o degrau **2 aparece repetido**. A sequência de diagnóstico
perde justamente a camada 3, que é onde está o erro mais comum que a aula destaca.

Problema secundário no mesmo slide: a faixa preta inferior cobre parcialmente o primeiro degrau.

Correção no slide: continuar de 4 em diante — degraus 4 e 5–7 — sem repetir 2 e sem omitir 3.

---

## Observações que não são erro factual

### OBS-001 — Marca d'água "NotebookLM" nos 15 slides

Todos os slides têm a marca `NotebookLM` no canto inferior direito. `brain/branding.md` determina
não usar logo de terceiro como decoração e, quando o material não é próprio, registrar autoria em
`release/credits.md`.

Para um curso publicado pela escola, a marca de um produto de terceiro em todos os quadros é
problema de identidade e de atribuição. Decisão do responsável: remover na regeração, ou manter e
registrar o crédito.

### OBS-002 — Resolução abaixo do canvas de entrega

As imagens são **1376×768**; o vídeo é **1920×1080**. Isso impõe upscale de **1,41×** em todos os
slides, e o resultado será perceptivelmente macio em texto fino — e este deck é quase todo texto.

Vale notar que exportar PDF do PowerPoint **não resolveria**: o ativo de origem já é raster nesta
resolução. A única solução real é regerar as imagens em 1920×1080 ou mais.

### OBS-003 — Proporção levemente fora de 16:9

As imagens têm proporção 1,7917; o canvas é 1,7778. Com `objectFit: contain`, sobram ~8 px de
barra no total. Irrelevante visualmente, registrado por completude.

### OBS-004 — Uso de fonte contraria a regra tipográfica

`brain/branding.md` reserva a monoespaçada para **string técnica** e Barlow para texto de leitura.
Nos slides 4, 7, 12 e 15 a monoespaçada é usada para prosa corrida, invertendo a regra: quando tudo
é mono, nada se destaca como dado técnico. O deck é visualmente coeso, então isto é desvio de
diretriz, não defeito de leitura.

### OBS-005 — Slide 006 acumula dois blocos do roteiro

O slide junta a correção da camada 3 (SEG-014, bloco 4) e o diagrama de relay (SEG-018, bloco 4,
outro momento). São dois focos independentes num só quadro, contra a regra de 1 a 3 focos
simultâneos de `brain/visual-language.md`. Sustentável com revelação progressiva na Fase 5, mas
ficaria melhor como dois slides.

### OBS-006 — Layout esparso no slide 003

O slide tem um vazio grande à direita e o rótulo "Serviço" em texto rotacionado na vertical, de
leitura difícil. Funciona, mas é o quadro mais fraco do deck em composição.

---

## Situação consolidada

| Divergência | Severidade | Slide | Absorvível? |
|---|---|---|---|
| DIV-001 | HIGH | 015 | não — contradiz a narração corrigida |
| DIV-002 | HIGH | 006 | não — contradiz CLM-001 |
| DIV-005 | HIGH | 012 | não — contradiz CLM-018 |
| DIV-003 | MEDIUM | 011 | não — o desenho contradiz o próprio rótulo |
| DIV-006 | MEDIUM | 014 | parcialmente, com recorte |
| DIV-004 | LOW | 004 | sim, mas é erro de digitação visível |

**Três divergências HIGH.** Nenhuma delas é do tipo que a narração resolve bem: em todas, o slide
afirma visualmente o contrário do que a voz diz. Corrigir apenas na fala produziria um vídeo em que
imagem e narração se contradizem em quatro momentos distintos, e o aluno tende a acreditar na
imagem.

## Recomendação

**Regerar o deck a partir do `script/on-screen-text.md` atual**, em 1920×1080 e sem a marca d'água.

Justificativa: os slides foram gerados do meu texto de tela, e a versão atual desse arquivo já
contém a correção do TR1-001, com instrução explícita de que a camada 5 deve aparecer sem
contraparte. Uma regeração corrige DIV-001 e DIV-003 automaticamente, e resolve OBS-001 e OBS-002 de
uma vez. DIV-002, DIV-004, DIV-005 e DIV-006 precisam de instrução explícita, listada abaixo.

Como os slides são imagens sem texto editável, não existe caminho de correção pontual: qualquer
conserto passa por gerar imagem nova.

### Instruções para a regeração

1. Camada 5 fora do grupo 6–7 no comparativo OSI × Internet, e sem chave de ligação (slide 011).
2. No resumo, cartão 05: `aplicação combina 6 e 7; sessão sem contraparte` (slide 015).
3. Pilhas de sistema final com **as sete camadas**, 1 a 7, iguais nas duas máquinas (slide 006).
4. LLC **acima** de MAC (slide 012).
5. Escada de diagnóstico continuando em 4 e 5–7, sem repetir o degrau 2 nem omitir o 3 (slide 014).
6. Corrigir "Camad" → "Camada" (slide 004).
7. Exportar em 1920×1080 ou superior.
8. Sem marca d'água de terceiro.
9. Opcional: dividir o slide 006 em dois (OBS-005) e refazer a composição do 003 (OBS-006).

Se a decisão for **manter o deck como está**, a Fase 5 fica viável mas com custo real: a narração
terá de corrigir explicitamente quatro slides em voz alta, e a divergência precisa ser registrada
em `script/slide-adaptation.md` e reauditada pelo Codex na revisão #2. Não recomendo — corrigir
imagem é mais barato que ensinar contra a imagem.
