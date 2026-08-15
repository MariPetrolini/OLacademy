# Production Plan — fundamentos-01-modelo-osi

Emitido pelo `course-director` em 2026-07-29.

## Alvo
Vídeo de ~14 min, 1920×1080, narração ElevenLabs com voz clonada, base visual obrigatória nos slides
do PPTX, entrega em `dist/fundamentos-01-modelo-osi.mp4`.

## Estrutura prevista do roteiro (Fase 2)

| Bloco | Conteúdo | Tempo alvo | Claims |
|---|---|---|---|
| 1 | Abertura pelo problema: equipamentos que nunca se viram e funcionam | 1:00 | — |
| 2 | O que é um modelo de referência; status da norma | 1:00 | CLM-001, CLM-002 |
| 3 | Engrenagem: camada, serviço ≠ protocolo, entidades pares, serviço cumulativo | 2:00 | CLM-003, CLM-004, CLM-011 |
| 4 | As sete camadas, de baixo para cima | 3:00 | CLM-010, CLM-012 |
| 5 | Encapsulamento: SDU + PCI = PDU | 2:00 | CLM-005, CLM-006, CLM-007, CLM-008 |
| 6 | Evidência: a captura (escrita de forma referencial — ver OQ-001) | 1:00 | CLM-017 |
| 7 | Procedência dos nomes: frame/packet/segment não são do OSI | 1:15 | CLM-009, CLM-017 |
| 8 | O modelo real da Internet e onde o mapeamento quebra | 1:30 | CLM-013, CLM-014, CLM-015, CLM-016, CLM-019 |
| 9 | Casos que não mapeiam limpo: TLS, sub-camadas, túnel | 0:45 | CLM-018, CLM-020, CLM-003 |
| 10 | Diagnóstico camada a camada (marcado como método, não norma) | 2:00 | CLM-021 |
| 11 | Recapitulação + exercício | 0:30 | — |

Total: ~16:00 de conteúdo planejado para um alvo de 14:00. **O roteirista deve comprimir**, com
prioridade de corte nesta ordem: bloco 9 → bloco 2 → bloco 10 (reduzir a tabela, não eliminar).
Blocos 5, 7 e 8 são o núcleo diferenciador da aula e não devem encolher.

## Regras específicas desta aula, herdadas da pesquisa

1. Nunca atribuir `frame`/`packet`/`segment`/`datagram` ao OSI. Sempre nomear a norma de origem.
2. Nunca dizer "cabeçalho na frente". Dizer "acrescenta sua informação de controle".
3. Nunca dar número de camada ao TLS.
4. Nunca alinhar OSI e TCP/IP 1:1.
5. A seção de diagnóstico precisa de marcação linguística de que é método, não norma.
6. Nenhum byte, IP, MAC ou porta concreto na narração até OQ-001 estar resolvida.
7. Definir cada sigla na primeira ocorrência (`brain/teaching-style.md`).

## Sequência restante

| Fase | Ator | Saída |
|---|---|---|
| 2 | `instructional-scriptwriter` | `script/lesson-script.md`, `script/on-screen-text.md`, `voice/segments.json` |
| 3 | Codex (`CODEX.md` revisão #1) | `qa/technical-review-1.md` |
| — | **PAUSA HUMANA 1** | `AGUARDANDO_CONTINUE_1` |
| 4 | ingestão do PPTX + `powerpoint-visual-analyst` | `source/slides/*.png`, `source/slide-analysis.md` |
| 5 | `instructional-scriptwriter` + `visual-director` | roteiro adaptado, `script/slide-map.json`, `storyboard/scene-plan.json` |
| 6 | Codex revisão #2 | `qa/technical-review-2.md` → **PAUSA HUMANA 2** |
| 7 | `voice-director` | `voice/generated/*.mp3`, `voice/audio-manifest.json` |
| 8 | `visual-director` + `remotion-engineer` + `audiovisual-qa` | `dist/fundamentos-01-modelo-osi.mp4` |

## Pendências de ambiente a resolver antes das fases indicadas

| Pendência | Bloqueia | Comando |
|---|---|---|
| LibreOffice ausente | Fase 4 | `brew install --cask libreoffice` |
| Poppler ausente | Fase 4 | `brew install poppler` |
| `.env.local` ausente | Fase 7 | `cp .env.example .env.local` + preencher chave e voice ID |
| `npm install` não rodado em `remotion/` | Fase 8 | `npm --prefix remotion install` |
