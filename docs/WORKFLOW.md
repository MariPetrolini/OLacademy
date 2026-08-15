# Workflow operacional

`RESEARCH -> SCRIPT -> CODEX1 -> HUMAN1 -> PPT -> ADAPT -> CODEX2 -> HUMAN2 -> VOICE -> VIDEO -> QA`

As pausas HUMAN1 e HUMAN2 existem na conversa. Não são verificações criptográficas.

### HUMAN1
Usuário revisa `script/lesson-script.md`, `voice/segments.json` e `qa/technical-review-1.md`.

### HUMAN2
Usuário revisa imagens do PPT, `source/slide-analysis.md`, roteiro adaptado, `script/slide-map.json`, storyboard e `qa/technical-review-2.md`. Pode pedir alterações nas imagens auxiliares, overlays ou texto. O Claude só continua após mensagem inequívoca.

## Vídeos vinculados de abertura e conclusão

O Remotion pode anexar automaticamente um vídeo antes das cenas da aula e outro ao final. Coloque os arquivos reutilizáveis em `assets/video/` e crie `video-config.json` na raiz da aula usando `templates/video-config.example.json` como modelo:

```json
{
  "openingVideo": "../../../../assets/video/opening.mp4",
  "conclusionVideo": "../../../../assets/video/conclusion.mp4",
  "nextTopic": "Camada física e meios de transmissão"
}
```

Os caminhos podem ser relativos à pasta da aula ou à raiz do projeto. A abertura é inserida antes do restante da composição. A conclusão é inserida depois da última cena, e `nextTopic` aparece sobre o vídeo de conclusão.

Também é possível parametrizar sem alterar o JSON:

```bash
npm run video:render -- courses/curso/lessons/aula \
  --opening assets/video/opening.mp4 \
  --conclusion assets/video/conclusion.mp4 \
  --next-topic "Próximo assunto"
```

Os parâmetros da linha de comando têm precedência sobre `video-config.json`. Se nenhum vídeo for configurado, o comportamento anterior é preservado. O pipeline usa `ffprobe` para calcular automaticamente as durações e ajustar o total da composição.
