# QA audiovisual — fundamentos-01-modelo-osi

- Data: 2026-07-29
- Agente: `audiovisual-qa`
- Artefato: `dist/fundamentos-01-modelo-osi.mp4`

## Ficha técnica medida

| Item | Valor | Conforme |
|---|---|---|
| Duração | **729,92 s = 12,16 min** | ✅ dentro da faixa 12–15 do brief |
| Resolução | 1920×1080 | ✅ canvas de `brain/visual-language.md` |
| Taxa de quadros | 30/1 | ✅ |
| Vídeo | H.264 | ✅ |
| Áudio | AAC, 48 kHz, estéreo | ✅ presente |
| Tamanho | 49,4 MB | — |
| Quadros renderizados | 21.896 | ✅ = 729,85 s × 30, casa com a soma do áudio |

Sincronia macro conferida: a duração do MP4 (729,92 s) bate com a soma medida dos 40 MP3
(729,85 s), diferença de 0,07 s — arredondamento de quadro. Nenhuma deriva acumulada.

## A duração real desmentiu a estimativa

| | Palavras/min | Duração |
|---|---|---|
| Modelo usado no roteiro | 135 | 15,5 min |
| **Voz clonada, medido** | **172,1** | **12,16 min** |

**O modelo errou 21,6% para cima.** Consequência prática: os três passes de compressão feitos entre
as Fases 2 e 3 — que levaram o roteiro de 2.567 para 2.066 palavras — foram desnecessários. Na
velocidade real, a versão original de 2.567 palavras daria cerca de 14,9 min, dentro do alvo.

Isso não é defeito deste vídeo, e sim uma calibração errada em
`skills/write-spoken-lesson.md`, que prescreve 125–145 ppm. Ver a seção de recomendações.

## Verificação de áudio por segmento

- 40 de 40 MP3 gerados, nenhum vazio (mínimo 96 KB), bitrate coerente em todos (~16 KB/s).
- Caracteres por segundo: mediana 16,11; faixa 13,23 a 20,22.
- **Um outlier:** `SEG-011` a 20,22 c/s (6,1 s para 123 caracteres). Tamanho de arquivo e bitrate
  proporcionais, então não é truncamento — provavelmente menos silêncio de borda numa frase curta de
  transição. **Requer conferência de ouvido** antes da publicação.
- Não foi possível avaliar pronúncia por inspeção automática. Os pontos de risco marcados na Fase 2
  seguem pendentes de escuta: a palavra `framework` em inglês dentro de SEG-026, e as siglas
  soletradas (`O S I`, `P D U`, `S D U`, `T C P`, `I E E E`, `R F C`, `I E T F`).

## Verificação visual por amostragem

Quadros extraídos no meio de cenas com destaque e inspecionados:

| Segmento | Slide | O que foi verificado | Resultado |
|---|---|---|---|
| SEG-012 | 005 | Destaque na linha da camada 1 | ✅ acertou a linha |
| SEG-017 | 005 | Destaque na linha da camada 7 | ✅ |
| SEG-022 | 008 | Destaque na barra `DADOS \| FCS` | ✅ |
| SEG-030 | 011 | Destaque na camada 5 (Sessão) | ✅ |
| SEG-032 | 012 | Destaque no bloco LLC/MAC | ✅ |
| SEG-035 | 013 | Destaque no callout de erro comum | ✅ |
| SEG-001 | 001 | Cena sem overlay | ✅ fundo branco puro (255,255,255) |

As 12 coordenadas de destaque, que eram aproximadas, **acertaram o alvo em todas as amostras**.

## Achados

### AVQA-001 — MEDIUM — chip de rótulo cobria conteúdo do slide · CORRIGIDO

O overlay desenhava um chip escuro com o texto de `label` a 52 px **acima** da caixa de destaque.
Em destaque de linha de tabela, onde a linha tem ~73 px, o chip caía sobre a linha vizinha e
escondia o texto dela.

Confirmado nos quadros: em SEG-012 o chip "Camada 1" cobria "Enlace de dados"; em SEG-030 o chip
"Sem camada separada" cobria a linha "Apresentação".

Agravante: o texto do chip duplicava a narração — o vídeo dizia "Camada um, física" enquanto exibia
"Camada 1" —, contra a regra de `brain/visual-language.md` de não exibir a narração na tela.

**Correção:** o `label` deixou de ser desenhado em `remotion/src/Video.tsx`. O campo continua no
`scene-plan.json` como registro de intenção. Não existe posição segura para um chip adjacente a um
destaque de largura total: qualquer lado ocluiria uma linha vizinha.

### AVQA-002 — MEDIUM — cor do destaque violava o branding · CORRIGIDO

A borda do destaque era `#ffd54a`, amarelo, hardcoded em `Video.tsx`.

`brain/branding.md` define branco e `#771215` como cores de identidade e determina que novas cores
semânticas sejam tokens separados, aprovados em contraste, e que **nunca compitam com o vermelho da
marca**. Um amarelo saturado em 5 px de borda compete diretamente.

**Correção:** borda passou a usar o token `brand.red` (`#771215`), declarado como constante no
componente.

### AVQA-003 — LOW — scrim global de 10% · MANTIDO, REGISTRADO

Quando existe destaque, `Video.tsx` aplica `boxShadow: 0 0 0 9999px rgba(0,0,0,.10)`, o que escurece
todo o quadro fora da caixa. Medido: o branco do slide vira `(229,229,229)` nessas cenas.

É um recurso de spotlight legítimo e o contraste do texto permanece confortável. Mantido. Registrado
porque significa que 12 das 40 cenas não exibem o slide na luminosidade original.

### AVQA-004 — LOW — folga de coordenada na última linha da tabela

No destaque da camada 1 (slide 005), a borda inferior da caixa fica alguns pixels abaixo da borda
da tabela. Origem: as coordenadas foram derivadas da geometria do gerador, não medidas no pixel.
Diferença visualmente irrelevante. Não corrigido.

### AVQA-005 — LOW — `wantedMotion` continua não implementado

As 10 intenções de movimento registradas no `scene-plan.json` (pan na topologia, revelação termo a
termo da equação, acender só as camadas baixas do relay, etc.) não existem no renderer. O vídeo
entrega slide + destaque + fade. Não é defeito desta entrega; é requisito de implementação aberto
para o `remotion-engineer`.

## Recomendações

1. **Recalibrar a meta de ritmo do projeto.** `skills/write-spoken-lesson.md` prescreve 125–145 ppm.
   A voz da escola narra a **172 ppm** com as configurações atuais (`eleven_multilingual_v2`,
   estabilidade 0,50, similaridade 0,75). Manter 135 fará toda aula futura ser cortada em ~20% sem
   necessidade. Sugestão: registrar 170 ppm como referência medida em `brain/voice-style.md` e
   ajustar a faixa da skill.
2. **Escutar o vídeo antes de publicar.** A inspeção automática cobre estrutura, sincronia e
   posicionamento, não timbre nem pronúncia. Prioridade: SEG-026 (`framework`) e SEG-011 (outlier
   de ritmo).
3. **Aproveitar a folga de duração.** Com 12,16 min contra teto de 16, existem quase 4 min livres.
   Conteúdo cortado por engano na compressão pode voltar — a menção ao RFC 3439, as listas de
   ferramentas de diagnóstico, a lição de procedência no fim do bloco 7.
4. **Adicionar retomada ao `generate-voice.mjs`** antes da próxima aula. Ele não pula MP3 já gerado:
   uma falha no meio cobra os 40 segmentos de novo.

## Veredito

`VERDICT: PASS_WITH_WARNINGS`

Estrutura, sincronia, resolução, áudio e posicionamento dos destaques conferidos e corretos. Os dois
achados MEDIUM foram corrigidos no renderer e o vídeo foi refeito. Permanecem três LOW registrados e
**uma verificação humana obrigatória antes da publicação: escutar o áudio.**
