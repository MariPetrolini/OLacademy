# Adaptação do roteiro aos slides — Fase 5

- Lesson ID: `fundamentos-01-modelo-osi`
- Data: 2026-07-29
- Passagem 2 do `instructional-scriptwriter`, conforme `CLAUDE.md` Fase 5

## Situação de partida

Os slides desta aula foram **reconstruídos** na Fase 4 a partir de `script/on-screen-text.md`
(ver `source/slide-analysis.md`). Consequência importante para esta fase: as seis divergências
factuais do deck original já estão fechadas.

**Nenhum erro de slide precisou ser corrigido pela narração.** O item 16 da Fase 5 não foi
acionado. O que o slide afirma e o que a voz diz coincidem nos 15 quadros.

> **Ressalva posterior (TR2-001).** A revisão #2 encontrou uma formulação excessiva presente ao
> mesmo tempo na fala e nos slides 011 e 015 — "sessão sem contraparte", mais forte do que o
> RFC 1122 sustenta. Não era divergência entre voz e imagem: as duas estavam igualmente fortes.
> Corrigido para "sem camada separada" em ambos. Ver `qa/technical-review-2-response.md`.

## Mudanças no roteiro

Três mudanças, todas motivadas pelo casamento com as imagens. Nenhuma altera claim técnico.

### 1. SEG-009 movido para antes de SEG-008 — ordem

**Antes:** SEG-007 (serviço ≠ protocolo) → SEG-008 (entidades pares) → SEG-009 (liberdade de
engenharia) → SEG-010 (serviço cumulativo).

**Depois:** SEG-007 → **SEG-009** → **SEG-008** → SEG-010.

**Motivo:** o slide 003 trata de serviço × protocolo; o slide 004 trata de entidades pares e
serviço cumulativo. Na ordem antiga a fala ia 003 → 004 → 003 → 004, fazendo o vídeo alternar
entre duas imagens e voltar. Com a troca, cada slide é falado de uma vez.

**Ganho didático colateral:** SEG-009 é a *consequência* de SEG-007 — trocar o protocolo sem
quebrar o serviço. Agora a consequência vem imediatamente depois da distinção, e não separada
por outro assunto.

### 2. A correção da camada 3 saiu de SEG-014 e virou SEG-018A — ordem

**Antes:** SEG-014 enumerava a camada 3 *e* já corrigia o erro "a camada do IP", no meio da
contagem das sete camadas.

**Depois:** SEG-014 apenas enumera a camada 3, junto das outras seis, no slide 005. A correção
passou a ser o novo **SEG-018A**, no slide 006 — que é precisamente onde a comparação
`Errado | O que a norma diz` aparece na tela.

**Motivo:** o slide 006 existe para essa correção. Deixá-la em SEG-014 significaria narrá-la
sobre o slide 005 e depois exibir o slide 006 sem fala própria, ou quebrar a enumeração no meio
para trocar de imagem.

**Ganho didático colateral:** enumerar as sete e só então voltar na mais mal contada ensina
melhor do que interromper a contagem para corrigir. Sustentação: CLM-010.

### 3. Nenhuma dêixis visual foi adicionada — decisão deliberada

A Fase 5 autoriza incluir dêixis ("aqui", "nesta tabela") agora que as imagens existem.
**Não incluí.**

**Motivo:** o texto atual já está sincronizado por ordem e por destaque de overlay, e dêixis
amarra a narração à arte de forma permanente. Se um slide for recomposto adiante, a locução
gravada passa a apontar para algo que mudou de lugar — e regravar custa chamada de API e
conferência. O ganho seria pequeno; o acoplamento, definitivo.

Onde a fala precisa apontar, o overlay aponta.

## Cobertura

| Slide | Segmentos | Cenas |
|---|---|---|
| 001 | SEG-001, SEG-002 | 2 |
| 002 | SEG-004, SEG-005, SEG-006 | 3 |
| 003 | SEG-007, SEG-009 | 2 |
| 004 | SEG-008, SEG-010 | 2 |
| 005 | SEG-011 … SEG-017 | 7 |
| 006 | SEG-018A, SEG-018 | 2 |
| 007 | SEG-019, SEG-020, SEG-021 | 3 |
| 008 | SEG-022, SEG-023 | 2 |
| 009 | SEG-024 | 1 |
| 010 | SEG-025, SEG-026, SEG-027 | 3 |
| 011 | SEG-028 … SEG-031 | 4 |
| 012 | SEG-032 | 1 |
| 013 | SEG-033, SEG-034, SEG-035 | 3 |
| 014 | SEG-036, SEG-037 | 2 |
| 015 | SEG-038, SEG-039, SEG-040 | 3 |

**15 de 15 slides narrados. 40 de 40 segmentos com slide. Nenhum slide excluído** — o item 14 da
Fase 4 é atendido sem precisar de autorização de exclusão.

## Garantias automatizadas

`script/build-artifacts.py` gera `voice/segments.json` e `script/slide-map.json` **do mesmo mapa**,
de modo que não possam divergir. Ele falha se:

- algum segmento ficar sem slide, ou algum slide sem narração;
- um ID mapeado não existir no roteiro;
- a ordem dos slides **retroceder** — a verificação que pegou o problema descrito na mudança 1;
- sobrar markdown no texto falado, houver URL na fala, ID duplicado, ou segmento acima de 45 s.

`storyboard/build-scene-plan.py` falha se um destaque sair do quadro ou usar um `type` que
`Video.tsx` não implementa.

## Storyboard — uma cena por segmento

`storyboard/scene-plan.json`: **40 cenas**, uma por segmento, 12 com destaque.

A escolha não é estética, é imposta pelo renderer. `remotion/src/Video.tsx` aplica os overlays de
uma cena pela duração inteira dela. O slide 005 sustenta 7 segmentos — se fossem uma cena única,
seriam cerca de dois minutos de quadro estático com um destaque parado, contra a regra de no máximo
35 s sem mudança significativa de `brain/visual-language.md`. Com uma cena por segmento, o destaque
desce a tabela camada por camada acompanhando a fala, usando apenas o que já existe no renderer.

## Movimento desejado que o renderer ainda não suporta

`Video.tsx` implementa **um** tipo de overlay: `highlight`. Qualquer outro `type` é descartado em
silêncio. Para não gravar intenção em campo que não renderiza, registrei 10 enriquecimentos no
campo `wantedMotion` das cenas — pan na topologia do slide 001, revelação termo a termo da equação
no 007, acender só as camadas 1 a 3 do relay no 006, desenhar o colchete deixando a camada 5 por
último no 011, entre outros.

São insumo para o `remotion-engineer` na Fase 8. Enquanto não existirem, o vídeo funciona: slide
como base, destaque acompanhando a fala, corte com fade.

## Duração

| Momento | Palavras | a 135 ppm |
|---|---|---|
| Fim da Fase 3 | 2.066 | 15,3 min |
| Após a Fase 5 | 2.089 | 15,5 min |
| Após TR2-001 | **2.101** | **15,6 min** |

Variação de +23 palavras: SEG-018A acrescenta a correção da camada 3 (+43) e SEG-014 foi enxugado
(−20). Dentro do teto de 16 min autorizado pelo responsável.

## Pendências que seguem abertas

- **OQ-001** — não há captura real. SEG-024 continua referencial e o slide 009 mostra o
  encapsulamento como caixas aninhadas, sem simular tela de analisador. Nada inventado.
- **OQ-007** — `CLAUDE.md` manda usar o PNG como base da cena, `brain/visual-language.md` proíbe.
  O storyboard segue o `CLAUDE.md` e declara isso em `slideBaseDecision`. Agora que os slides são
  nativos na identidade da escola e em 1920×1080, a opção de usá-los como base ficou mais
  defensável — mas a decisão continua sendo do responsável.
- **OQ-008** — `brain/references/*` citados e ausentes.
