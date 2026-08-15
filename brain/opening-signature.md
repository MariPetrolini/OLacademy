# Abertura obrigatória (SEG-000)

Toda aula abre com a mesma apresentação do instrutor. Ela é **obrigatória e automática**: o
`instructional-scriptwriter` cria o segmento sem que o usuário precise pedir, em toda aula nova,
já na Passagem 1 do roteiro. Não é assunto de pausa humana nem de negociação por aula.

## Texto canônico

> Olá, eu sou André Brazioli, diretor de pós-vendas na OL Tecnologia e especialista em redes.
> Hoje falaremos sobre `<assunto da aula>`. Vamos começar?

Só a parte `<assunto da aula>` varia. O resto é literal: mesma ordem, mesma pontuação, mesmas
palavras. Não reescrever para "soar melhor", não encurtar, não adicionar boas-vindas antes.

## A variável do assunto

Escrever o assunto como se responde à pergunta "sobre o que é a aula?", em minúsculas e com o
artigo natural, derivado do `lesson-brief.md`:

| Aula | Trecho |
|---|---|
| Modelo OSI | `o modelo O S I` |
| MAC learning em switches | `como um switch aprende endereços MAC` |
| Wi-Fi 6 e OFDMA | `Wi-Fi 6 e OFDMA` |

Regras: sem título de slide em caixa alta, sem número de aula, sem nome de curso, sem sigla que
a aula ainda não explicou de forma que atrapalhe — a sigla aqui é só um rótulo do tema, a
definição vem depois. Manter curto: uma oração.

## Forma para o TTS

O texto que vai para a ElevenLabs é o mesmo, com dois ajustes de pronúncia:

- escrever `O L Tecnologia` (soletrado, "ó-éle"), não `OL Tecnologia` — ver
  `brain/pronunciation-dictionary.md`;
- siglas dentro da variável seguem a convenção da aula (`O S I`, `E V P N`), respeitando a regra
  de colisão artigo + sigla soletrada validada em `script/build-artifacts.py`.

O `?` final de "Vamos começar?" é o que dá a entonação de convite. Manter.

## Onde entra no vídeo

`SEG-000` é o **primeiro** segmento do roteiro e da narração, e fica **sobre o slide de capa**
(slide 1). A capa já está na tela quando a apresentação é falada; a narração própria da capa
(`SEG-001`) continua no mesmo slide, em seguida. Não criar cartão de marca, vinheta ou cena sem
slide para isso — a regra "toda cena referencia um slide real do PPT" continua valendo sem
exceção.

## Verificação

- `automation/elevenlabs/generate-voice.mjs` recusa gerar áudio se `SEG-000` não for o primeiro
  segmento de `voice/segments.json` ou não casar com o texto canônico.
- Codex checa a presença e a literalidade nas revisões #1 e #2 (`CODEX.md`).
