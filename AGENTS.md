# AGENTS.md — Contrato global

## Objetivo
Produzir cursos profissionais de redes com pesquisa confiável, fala natural, slides obrigatórios, animação didática e revisão independente.

## Orquestração
- Claude Code: maestro.
- Codex: revisor técnico independente.
- ElevenLabs: voz clonada.
- Remotion: composição/render final.

## Ordem padrão
1. `course-director`
2. `official-docs-researcher` + especialista(s) de domínio
3. `instructional-scriptwriter`
4. `technical-reviewer` via Codex — revisão #1
5. **PAUSA HUMANA 1**
6. `powerpoint-visual-analyst`
7. `instructional-scriptwriter` — adequação a slides
8. `visual-director` — storyboard inicial
9. `technical-reviewer` via Codex — revisão #2
10. **PAUSA HUMANA 2**
11. `voice-director`
12. `visual-director` — timing final
13. `remotion-engineer`
14. `audiovisual-qa`
15. `youtube-release-manager` (opcional)

## Abertura obrigatória
Toda aula abre com `SEG-000`, a apresentação padrão do instrutor definida em `brain/opening-signature.md`. É automática: nenhum agente espera pedido do usuário para incluí-la, e nenhum agente a reescreve — só a variável do assunto muda. Fica sobre o slide de capa, antes da narração da capa.

## Política técnica
Fontes primárias/oficiais vencem slides e material secundário. O PPT é obrigatório como insumo visual, mas nunca é a fonte de verdade técnica.

## Pausas humanas
Não usar hash. Não preencher “approved” automaticamente. Apenas parar e aguardar uma mensagem inequívoca do usuário para continuar.
