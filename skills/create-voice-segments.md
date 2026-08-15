# Skill: segmentar voz

O `instructional-scriptwriter` deve preparar `voice/segments.json` como parte do pacote textual, antes da revisão técnica e da aprovação humana. Esta etapa não pode chamar o TTS nem criar áudio. O texto de cada segmento deve ser exatamente o que será enviado à API. Depois de criar ou alterar segmentos, encaminhar roteiro e segmentos ao `technical-reviewer`; após o veredito, interromper o fluxo para revisão humana. Nunca preencher o OK em nome da pessoa.

O primeiro segmento é sempre `SEG-000`, a abertura obrigatória de `brain/opening-signature.md`, com o texto na forma de TTS (`O L Tecnologia` soletrado) e ancorado ao slide de capa. `automation/elevenlabs/generate-voice.mjs` recusa gerar áudio se ele faltar ou divergir do texto canônico.

Crie JSON conforme `templates/voice-segments.schema.json`. Cada segmento deve ter ID estável, texto falado puro, referência ao trecho do roteiro e duração estimada. Prefira 1–4 frases. Evite segmentos maiores que 45 segundos. Separe termos críticos para permitir regeneração isolada.

## Quando informar `sourcePages`

Depende do pipeline da aula:

- **Pipeline 3 (script-first).** Em G3 **não** preencher `sourcePages`: o deck de imagens só é
  ingerido em G6, e as páginas ainda não existem. O texto precisa se sustentar sem imagem —
  nada de dêixis visual ("aqui", "nesta tabela", "como você vê"), porque é este texto que a
  pessoa responsável vai ler e aprovar sem ver arte nenhuma. O campo é preenchido em G7, ao
  adequar a fala às imagens, junto de `script/slide-map.md` e `script/slide-adaptation.md`.
- **Pipeline 2 (deck-first).** Informar `sourcePages` já na criação dos segmentos, porque o
  roteiro nasceu do deck.

Em qualquer pipeline, é esse campo que permite ao `visual-director` casar segmento, página e
cena, e ancorar a revelação dos blocos com `atSegment` no `scene-plan.json`. Segmentar pensando
na cena ajuda: um slide denso costuma pedir mais de um segmento, e vários slides simples podem
caber em um só.

A cobertura completa (todo segmento com página, toda página com narração ou justificativa) é
registrada em `script/slide-map.md` — em G7, no pipeline 3.
