# Skill: generate-elevenlabs-voice

Pré-condição: usuário já deu o segundo `continue`. Gere um MP3 por segmento exato de `voice/segments.json` usando a voz configurada. Não modificar texto durante TTS. Se uma pronúncia falhar, voltar ao roteiro/segmento e solicitar/regenerar de forma explícita.

## Abertura obrigatória

O script recusa gerar áudio se `SEG-000` não for o primeiro segmento ou se o texto divergir do canônico de `brain/opening-signature.md`. Corrija o roteiro — não contorne. `SKIP_OPENING_CHECK=true` existe só para depuração local, nunca para produzir aula.

## Regerar segmento isolado

`npm run voice:generate -- <pasta-da-aula> --only SEG-000,SEG-012`

Gera apenas os ids citados, preserva os MP3 e as durações medidas dos demais e reescreve `voice/audio-manifest.json` na ordem de `segments.json`. Use sempre que só um segmento mudou — regerar a aula inteira gasta crédito à toa. Se um segmento preservado não tiver áudio anterior, o script falha e pede execução completa.
