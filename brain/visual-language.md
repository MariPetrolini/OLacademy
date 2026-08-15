# Linguagem visual

## Referências de base (2026-07-25)

`brain/references/design-reference.pdf` e `brain/references/switch-mac-learning-reference.html` são a base visual escolhida pelo responsável para esta escola — um formato de "apresentação de slides" bem produzida. Todo agente visual (`visual-director`, `video-visual-designer`, `remotion-engineer`) deve consultá-las antes de propor uma cena. Delas vêm as regras concretas abaixo; onde há conflito com o resto deste documento, este documento (mais restritivo) prevalece.

## Canvas
1920x1080, 30 fps, safe area de 8%.

## Tipografia por função

- Texto de leitura (títulos, corpo, rótulos de conceito): Barlow — display, humano.
- **Toda string técnica** (endereço MAC, nome/número de porta, comando ou saída de CLI, nome de coluna de tabela, timer) usa fonte monoespaçada (`JetBrains Mono`, `theme.monoFontFamily`), nunca Barlow — distingue "dado técnico" de "prosa" à primeira vista, como em `switch-mac-learning-reference.html`.

## Hierarquia
- título: 70–90 px;
- subtítulo: 48–60 px;
- corpo: 42–50 px;
- rótulo técnico: mínimo 42 px.

## Rótulo de topo ("eyebrow")

Toda cena não decorativa pode abrir com uma linha pequena, mono, letter-spacing largo, maiúscula, com uma barra de cor à esquerda (ex.: "PASSO 1 DE 4", "O PROBLEMA", "RESUMO") — padrão de `design-reference.pdf` e do `.eyebrow`/`.step-num` do HTML de referência. Serve para orientar o espectador sobre que tipo de cena está vendo (problema, passo numerado, conceito-chave, resumo), sem repetir a narração.

## Redes
Dispositivos são nós; enlaces são linhas; movimento de quadros/pacotes é animado ao longo do enlace. Endereços MAC, IP, VLAN e interfaces usam estilos visuais distintos, definidos por tokens e não por cores isoladas.

### Chassi do switch (padrão de referência)

O switch é desenhado como um chassi — não uma caixa genérica: uma carcaça com uma fileira de portas numeradas (cada porta com seu próprio retângulo/slot e um indicador de estado — apagado/ativo/ocupado), e os hosts abaixo como ícones simples de dispositivo (não círculos genéricos), conectados por hastes verticais. Um quadro em trânsito é um "tag" (pílula colorida com o texto `MAC → Porta`, fonte mono) que se desloca da origem até o chassi, não apenas um ponto. Referência: `.switch-chassis`, `.port`, `.device`, `.frame-tag` em `switch-mac-learning-reference.html`.

### Tabela de endereços MAC (padrão de referência)

Cabeçalho com fundo sólido `brand.red`, texto branco, colunas em mono; linhas de dados em mono sobre fundo claro. Uma entrada nova aparece com um pequeno deslizar + fade (nunca "pop" instantâneo); uma entrada em aging esmaece para ~25% de opacidade, nunca desaparece de forma abrupta. Rótulo de status (ex.: "aprendido", "expirando") como badge com cantos arredondados, cor associada ao estado — nunca só a cor da célula. Referência: page 8 e page 18 de `design-reference.pdf`; `.mac-table`, `.tag-learned`, `.tag-aging` em `switch-mac-learning-reference.html`.

### Comparação lado a lado (padrão de referência)

Quando o roteiro contrasta dois comportamentos (conhecido vs. desconhecido; dinâmico vs. estático; hub vs. switch), usar duas colunas/cartões emparelhados com o mesmo diagrama em miniatura, cor associada a cada lado (ex.: verde para "conhecido"/sucesso, vermelho para "desconhecido"/alerta — dentro da paleta desta escola, sem introduzir uma terceira cor de marca) e uma legenda mono curta por coluna (ex.: "P1 → P3 apenas"). Referência: `.compare`, `.compare-col` em `switch-mac-learning-reference.html`; page 3 de `design-reference.pdf`.

### Recapitulação em grade numerada (padrão de referência)

Recapitulação final como grade de cartões numerados (01, 02, 03…), cada um com número mono em destaque, título curto e uma frase — não uma lista vertical de ícones nem um parágrafo. Referência: `.recap-grid`, `.recap-card` em `switch-mac-learning-reference.html`; page 21 de `design-reference.pdf`.

## Acessibilidade
Não depender apenas de cor. Usar ícones, traços, rótulos e padrões. Legendas com duas linhas no máximo e contraste forte.

## Slide do PDF reconstruído (tipo de cena `slide`)

A aula nasce de um PDF, e cada página que vira cena é **reconstruída nativamente** nesta
identidade — a página nunca é exibida como imagem, fundo ou textura. `source/slides/page-NNN.png`
é material de leitura e revisão, não asset de render.

- **Estrutura da cena**: eyebrow mono opcional no topo, título (68 px, ou 82 px no layout
  `statement`), régua vermelha curta sob o título, e blocos revelados um a um.
- **Layouts**: `statement` (uma ideia forte), `bullets` (sequência curta), `split`
  (contraste binário em duas colunas), `data` (linhas técnicas em mono).
- **Tipos de bloco**: `bullet` (marcador quadrado vermelho + texto 48 px), `mono` (dado
  técnico em cartão de tinta clara, 44 px), `note` (texto secundário 42 px a 82% de
  opacidade), `metric` (número/valor curto, 92 px, mono, `brand.red`).
- **Revelação**: cada bloco entra com fade + deslize curto (~14 quadros) no frame em que a
  narração o menciona — nunca tudo de uma vez, nunca "pop" instantâneo. O timing vem de
  `npm run storyboard:sync`, calculado sobre a duração real da voz.
- **Densidade**: até 8 blocos por cena, 220 caracteres por bloco, 1 a 3 focos simultâneos. O
  slide de origem quase sempre precisa ser cortado; o resto vai para a narração.
- **Página de figura/diagrama** (`needsNativeDiagram`) não é resolvida com `slide`: usar as
  famílias de cena desta seção (chassi, tabela MAC, comparação, grade numerada).

## Gramática de cena
- Relação/topologia: nós, enlaces, agrupamentos e rótulos persistentes.
- Sequência/causalidade: revelar estados na ordem da narração.
- Comparação: split screen ou matriz com escalas equivalentes.
- Interface: captura sanitizada, contexto preservado e spotlight localizado.
- RF: mapa espacial com legenda, escala e padrão além da cor.
- Capítulo: título curto, assinatura da marca e duração mínima.
- Síntese: diagrama consolidado ou até cinco pontos curtos.

## Movimento
Animar somente para indicar direção, causalidade, agrupamento ou mudança de estado. Priorizar corte, dissolve curto, wipe direcional e match move simples. Evitar partículas, glow, parallax decorativo, bounce e zoom contínuo.

## Densidade
Manter de 1 a 3 focos simultâneos. Não exibir a narração inteira na tela. Diagramas complexos devem ser construídos progressivamente e preservar contexto entre etapas.
