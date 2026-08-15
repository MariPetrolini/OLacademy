# Fábrica de Cursos de Redes — Claude Code + Codex + ElevenLabs + Remotion

Esta versão foi refatorada a partir do projeto V3 para um fluxo **simples, humano e operacional**.

## Princípios
- Claude Code é o orquestrador e produtor.
- Os especialistas de rede e o `official-docs-researcher` da V3 foram preservados sem alteração.
- Codex é o revisor técnico independente.
- Não existem gates por hash. Existem somente **duas pausas humanas**: o Claude para e espera `continue`.
- O PowerPoint entra **depois** da primeira aprovação humana e seus slides são **obrigatórios** no vídeo.
- Depois do PPT, o roteiro pode ser ajustado para sincronizar fala e imagem, passa por nova revisão do Codex e volta para uma segunda pausa humana.
- ElevenLabs gera a narração com a voz clonada.
- Remotion usa os slides como base visual e pode acrescentar zoom, destaques, setas, diagramas, animações e overlays didáticos.

## Fluxo
1. Tema -> pesquisa + especialistas de rede.
2. Roteiro falado + segmentos para TTS.
3. Codex revisão técnica #1.
4. **PAUSA HUMANA 1** — revisar texto; escrever `continue` ou pedir alterações.
5. Upload/ingestão do `.pptx`.
6. Análise das imagens + adequação do roteiro + mapa slide/fala.
7. Codex revisão técnica #2.
8. **PAUSA HUMANA 2** — revisar imagens e texto; escrever `continue` ou pedir alterações.
9. ElevenLabs gera áudio.
10. Storyboard + Remotion monta o vídeo usando obrigatoriamente os slides.
11. QA audiovisual.
12. MP4 final em `dist/`.

Vídeos reutilizáveis de abertura e conclusão são configurados uma única vez na seção **Vídeos padrão** do Estúdio. Ao criar cada aula, o campo obrigatório **Próxima aula** define o texto variável do encerramento; ele ainda pode ser ajustado antes do render. Consulte `docs/WORKFLOW.md`.

O formulário **Nova aula** já permite selecionar Claude ou Codex separadamente para direção, pesquisa, roteiro, revisões, análise de slides, storyboard, voz, timing e QA audiovisual. As escolhas ficam salvas em `agent-config.json` dentro da pasta da aula e podem ser alteradas depois na etapa **Escolher agentes**.

## Estúdio local

No macOS, dê dois cliques em **OL Academy Studio.app** na raiz do projeto. O aplicativo inicia os serviços locais e abre o Estúdio no navegador, sem publicar nada externamente.

Para usar todo o fluxo por uma interface visual no notebook:

```bash
npm run studio
```

Depois, abra `http://localhost:3000`. O Estúdio OL Academy permite criar aulas, editar e aprovar textos, enviar PowerPoint e vídeos, chamar os agentes responsáveis, gerar voz, renderizar e acompanhar cada etapa. Claude Code, Codex, ElevenLabs, Node.js e FFmpeg precisam estar configurados para as etapas que dependem deles.

Comece por `docs/START-HERE.md`.
