# Workflow operacional

`RESEARCH -> SCRIPT -> CODEX1 -> HUMAN1 -> PPT -> ADAPT -> CODEX2 -> HUMAN2 -> VOICE -> VIDEO -> QA`

As pausas HUMAN1 e HUMAN2 existem na conversa. Não são verificações criptográficas.

As alterações feitas pela pessoa revisora no Estúdio são autoritativas. Isso inclui reescrever trechos e apagar seções completas. Ao salvar, o arquivo editado passa a ser a versão oficial, a versão anterior é preservada em `qa/human-edits/` e os agentes posteriores são instruídos a não restaurar conteúdo removido.

Além da instrução, o Estúdio protege tecnicamente os arquivos editados: se um agente tentar sobrescrevê-los, a versão humana é restaurada ao término da execução. Uma edição posterior à aprovação invalida a aprovação daquela fase e exige nova confirmação explícita. Substituir o PowerPoint também invalida a segunda aprovação.

### HUMAN1
Usuário revisa `script/lesson-script.md`, `voice/segments.json` e `qa/technical-review-1.md`.

### HUMAN2
Usuário revisa imagens do PPT, `source/slide-analysis.md`, roteiro adaptado, `script/slide-map.json`, storyboard e `qa/technical-review-2.md`. Pode pedir alterações nas imagens auxiliares, overlays ou texto. O Claude só continua após mensagem inequívoca.

## Vídeos vinculados de abertura e conclusão

O Remotion anexa automaticamente um vídeo padrão antes das cenas da aula e outro ao final. No Estúdio, abra **Vídeos padrão** no menu lateral e faça upload dos dois arquivos uma única vez. Eles serão gravados em `assets/video/`, e a configuração global ficará em `config/video-defaults.json`.

Em cada aula, somente os textos variáveis ficam em `video-config.json`:

```json
{
  "openingTitle": "Título exibido na abertura desta aula",
  "nextTopic": "Camada física e meios de transmissão"
}
```

A abertura padrão é inserida antes do restante da composição e recebe `openingTitle`. Quando esse campo não é informado, o tema do `lesson-brief.md` é usado automaticamente. A conclusão padrão é inserida depois da última cena, e `nextTopic` aparece sobre ela.

Também é possível parametrizar sem alterar o JSON:

```bash
npm run video:render -- courses/curso/lessons/aula \
  --opening-title "Título desta aula" \
  --next-topic "Próximo assunto"
```

Os parâmetros da linha de comando têm precedência sobre `video-config.json`. O render é bloqueado enquanto os dois vídeos globais não estiverem configurados. O pipeline usa `ffprobe` para calcular automaticamente as durações e ajustar o total da composição.
