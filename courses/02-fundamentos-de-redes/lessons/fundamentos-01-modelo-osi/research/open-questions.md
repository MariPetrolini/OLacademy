# Perguntas abertas — fundamentos-01-modelo-osi

Status em 2026-07-29. Nenhuma delas bloqueia a escrita do roteiro; OQ-001 bloqueia a **produção
final do vídeo** se não for resolvida antes da Fase 8.

---

## OQ-001 — A captura real ainda não existe · BLOQUEIA VÍDEO
**Decisão do responsável (2026-07-29):** a aula usa diagramas como veículo principal + uma captura
real como prova de que os cabeçalhos existem de fato.

**Problema:** não há nenhum `.pcap` nem screenshot de Wireshark no repositório. O
`official-docs-researcher` e o `instructional-scriptwriter` estão **proibidos** de inventar bytes,
IPs, MACs, números de porta ou telas de análise (`agents/official-docs-researcher.md`, princípios
obrigatórios).

**Como o roteiro vai lidar com isso agora:** o segmento de evidência será escrito de forma
*referencial* — a narração descreve o que o aluno está vendo em termos estruturais ("aqui está o
cabeçalho de enlace, aqui o de rede, aqui o de transporte, e aqui a carga que nenhum deles
interpreta") sem citar nenhum valor concreto. Assim o texto sobrevive a qualquer captura que você
fornecer, e nada precisa ser reescrito quando o artefato chegar.

**Opções para resolver, escolha do responsável:**
- (a) Você fornece um `.pcap` ou screenshot já sanitizado.
- (b) Eu especifico o procedimento e você executa no seu lab; o `lab-and-evidence-engineer` valida e
  sanitiza conforme `skills/sanitize-lab-artifacts.md`.
- (c) A captura entra apenas como slide do PPTX na Fase 4, e o roteiro se adapta a ela na Fase 5.

Opção (c) é a que melhor se encaixa no workflow do projeto, já que o PPTX entra depois da Pausa 1 de
qualquer forma. **Requisito de sanitização em qualquer opção:** nenhum IP público, MAC real, serial,
credencial ou nome real (`brain/source-policy.md`).

---

## OQ-002 — Versão do IEEE Std 802 · resolvida com ressalva
A fonte A3 usada é **IEEE Std 802-2001**, obtida no domínio oficial `ieee802.org`. Existe revisão
posterior (IEEE Std 802-2014), que não está acessível gratuitamente com a mesma facilidade.

Os dois claims extraídos de A3 [CLM-018, CLM-017] são estruturais — a família 802 cobre as duas
camadas mais baixas do OSI, e a camada de enlace é estruturada como LLC sobre MAC — e não mudaram
entre revisões. **Risco avaliado como baixo.** Registrado para o Codex confirmar ou contestar.

Se você tiver acesso institucional ao IEEE Xplore, o upgrade da citação para 802-2014 fecha a
pendência.

---

## OQ-003 — Profundidade da menção ao RFC 3439 · decisão editorial pendente
[CLM-019] autoriza citar "Layering Considered Harmful" como crítica documentada dentro da própria
IETF. A recomendação da pesquisa é **uma frase**, com a ressalva de que é RFC Informational.

Risco se for além disso: o aluno iniciante sai da primeira aula do curso desconfiando do modelo que
ainda não aprendeu. **Recomendação: manter uma frase.** Se você quiser cortar completamente, o
roteiro não perde nada estrutural.

---

## OQ-004 — Nomenclatura de PDU das camadas 5, 6 e 7 · sem resposta em fonte primária
Não existe termo primário consagrado para a PDU das camadas 5, 6 e 7 comparável a frame/datagram/
segment. O X.200 chamaria de Application-PDU, Presentation-PDU, Session-PDU, mas esses termos não
circulam na prática.

**Tratamento no roteiro:** usar "mensagem" ou "dados" e **dizer ao aluno que aqui a terminologia é
frouxa** — o que é mais honesto do que inventar uma tabela completa. A tabela da seção 4 do
`research.md` deixa essas linhas em branco de propósito. Não preenchê-las.

---

## OQ-005 — Aula 01 do curso 02 assume Curso 01 feito? · decisão tomada
O currículo põe "01 - Preparação do Laboratório" antes de "02 - Fundamentos de Redes", e o Wireshark
está na aula 04 do curso 01. Mas na prática esta é a **primeira aula que a escola vai publicar**, e
muitos alunos vão chegar por ela.

**Decisão:** a aula não exige o curso 01. A captura é *apresentada*, não executada pelo aluno.
Registrado no `lesson-brief.md`. Consequência para a narração: nenhuma instrução do tipo "abra o
Wireshark e faça"; no máximo um convite ("se você já fez o curso de laboratório, vale repetir isso
por conta").

---

## OQ-009 — Vão na numeração de segmentos · decisão tomada, registrada

Os IDs saltam de `SEG-002` para `SEG-004`. Origem: fusão de dois segmentos durante a compressão de
duração da Fase 2.

Renumerar foi proposto ao responsável e **recusado**. Decisão: manter. Levantado também pelo Codex
como TR1-007, cuja recomendação é exatamente "manter se a estabilidade dos IDs for deliberada, mas
registrar a decisão".

Impacto verificado como nulo: `automation/elevenlabs/generate-voice.mjs` usa `s.id` como nome de
arquivo, e `automation/remotion/auto-storyboard.mjs` agrupa cenas por `slide-map.json`, não por
índice de segmento. IDs são identificadores, não índices.

---

## OQ-007 — `CLAUDE.md` e `brain/visual-language.md` se contradizem · DECISÃO SUA, afeta a Fase 8

Encontrado durante a Fase 2. Não afeta o roteiro; **afeta diretamente o que o Remotion renderiza.**

Os dois documentos dizem o oposto sobre o papel do PNG do slide:

- **`CLAUDE.md`, Fase 8, item 26:** "O PNG de cada slide é a **base visual obrigatória** da cena
  correspondente."
- **`brain/visual-language.md`, seção "Slide do PDF reconstruído":** "a página **nunca** é exibida
  como imagem, fundo ou textura. `source/slides/page-NNN.png` é material de leitura e revisão,
  **não asset de render**."

Não é ambiguidade — é conflito direto. Um manda exibir o PNG, o outro proíbe.

**Leitura provável:** a seção do `visual-language.md` é resíduo da V3, que era PDF-first. O próprio
`PROMPT-CODEX-AUDITAR-REFATORACAO.md` pede para procurar "referências residuais a
hashes/gates/PDF-first". Três indícios sustentam isso: a seção fala de **PDF** e de
**`page-NNN.png`**, enquanto o ingestor da V4 produz **`slide-NNN.png`** a partir de **PPTX**; e ela
manda usar `npm run storyboard:sync`, script que não existe no `package.json` (o existente é
`storyboard:auto`).

**Como está implementado hoje:** `remotion/src/Video.tsx` exibe o PNG em tela cheia com
`objectFit: contain` — ou seja, o código segue o `CLAUDE.md`, não o `visual-language.md`.

**Não decidi isso por conta própria.** As duas opções são:
- (a) `CLAUDE.md` prevalece: o PNG é a base da cena e os overlays enriquecem. É o que o código faz
  hoje e o caminho de menor esforço.
- (b) `visual-language.md` prevalece: cada slide é reconstruído nativamente na identidade da escola.
  Resultado visual muito superior, mas exige escrever componentes de cena por layout — trabalho
  bem maior no `remotion-engineer`, e hoje o renderer não tem nada disso.

Se você escolher (b), a seção da Fase 8 do `CLAUDE.md` precisa ser reescrita. Se escolher (a), a
seção "Slide do PDF reconstruído" do `visual-language.md` precisa sair ou ser marcada como
histórica.

---

## OQ-008 — Referências visuais citadas não existem no repositório

`brain/visual-language.md` manda todo agente visual consultar, antes de propor cena:
- `brain/references/design-reference.pdf`
- `brain/references/switch-mac-learning-reference.html`

**Nenhum dos dois existe.** O diretório `brain/references/` não está no repositório. O documento
faz referência a elementos específicos deles (`.switch-chassis`, `.mac-table`, `.recap-grid`,
"page 8", "page 21") como se fossem norma visual verificável.

Consequência para esta aula: as regras concretas que sobreviveram no texto (tipografia por função,
hierarquia de tamanhos, eyebrow, densidade, movimento) foram aplicadas em
`script/on-screen-text.md`. As que dependem de ver os arquivos não puderam ser verificadas.

Se os arquivos existem fora do repositório, vale adicioná-los. Se foram perdidos, vale remover as
referências para não obrigar agentes futuros a consultar algo inacessível.

---

## OQ-006 — PPTX desta aula ainda não existe · esperado, não é problema
O deck entra na Fase 4, depois da Pausa Humana 1, conforme `CLAUDE.md`. Nenhuma ação agora.

Quando ele chegar, o `powerpoint-visual-analyst` tem uma verificação **específica e obrigatória**
para esta aula: conferir se algum slide comete os erros já mapeados na pesquisa —
- tabela `frame/packet/segment` atribuída ao OSI [CLM-009],
- OSI e TCP/IP alinhados lado a lado em 1:1 [CLM-014],
- "cabeçalho sempre na frente" [CLM-007],
- TLS com número de camada cravado [CLM-020].

Se o slide contiver qualquer um deles, `CLAUDE.md` (Fase 5, item 16) manda **não absorver o erro**:
a narração corrige e a divergência é registrada em `script/slide-adaptation.md`.
