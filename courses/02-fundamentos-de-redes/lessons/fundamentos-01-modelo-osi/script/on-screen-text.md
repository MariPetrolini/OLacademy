# Texto de tela — Modelo OSI

- Lesson ID: `fundamentos-01-modelo-osi`
- Passagem: **1 (antes do PowerPoint)** — proposta de texto, ainda não amarrada a slide
- Regras aplicadas de `brain/visual-language.md`: eyebrow mono em maiúscula; string técnica em
  monoespaçada, nunca em Barlow; máximo 8 blocos por cena; 1 a 3 focos simultâneos; **nunca exibir
  a narração inteira na tela**
- Nada aqui é falado. A narração está em `script/lesson-script.md`.

> Convenção deste arquivo: `[MONO]` marca o que precisa sair em fonte monoespaçada.

---

## Bloco 0 — Abertura obrigatória (SEG-000)

Nenhum texto de tela novo. A apresentação do instrutor é falada **sobre o slide de capa**, que já
está na tela desde o primeiro frame (`brain/opening-signature.md`). Sem overlay: nada deve competir
com a capa enquanto ele se apresenta.

---

## Bloco 1 — Abertura (SEG-001, SEG-002)

**EYEBROW:** O PROBLEMA
**TÍTULO:** Nada disso foi testado junto
**BLOCOS:**
- Fabricantes diferentes
- Sistemas operacionais diferentes
- Nenhum teste conjunto
- E funciona

**SEG-002 — segundo foco**
**TÍTULO:** Sem ordem, tentativa e erro. Com ordem, método.

---

## Bloco 2 — Modelo de referência (SEG-004 a SEG-006)

**EYEBROW:** A NORMA
**TÍTULO:** Open Systems Interconnection
**BLOCOS:**
- `[MONO]` ISO/IEC 7498-1
- `[MONO]` ITU-T X.200
- Texto idêntico, duas designações
- Em vigor

> O `visual-director` deve mostrar as duas designações lado a lado uma única vez. O aluno precisa
> reconhecer as duas na literatura, mas nenhuma delas é falada por extenso.

**SEG-005 — foco isolado**
**TÍTULO:** Referência, não implementação
**BLOCOS:**
- Divide responsabilidades
- Define fronteiras
- Não diz como construir

**SEG-006 — comparação binária (layout `split`)**
| O modelo OSI | A pilha de protocolos OSI |
|---|---|
| Em vigor | Não venceu comercialmente |
| Linguagem comum da área | Substituída pelo TCP/IP |

---

## Bloco 3 — A engrenagem (SEG-007 a SEG-010)

**EYEBROW:** CONCEITO-CHAVE
**TÍTULO:** Serviço não é protocolo
**BLOCOS (layout `split`):**
| Serviço | Protocolo |
|---|---|
| Para a camada de cima | Com o par do outro lado |
| Vertical | Horizontal |

**SEG-008 — entidades pares**
**TÍTULO:** Entidades pares
**BLOCOS:**
- Mesma camada, máquinas diferentes
- Camada 3 fala com camada 3
- Nunca camada 3 com camada 4

**SEG-010 — serviço cumulativo**
**TÍTULO:** Aprimoramento passo a passo
**NOTA:** O serviço de uma camada é a capacidade dela mais todas as de baixo.

---

## Bloco 4 — As sete camadas (SEG-011 a SEG-018)

**EYEBROW:** AS SETE CAMADAS
Pilha construída progressivamente, de baixo para cima, um nível por segmento. Número e nome
sempre visíveis; a camada em foco destacada.

| # | Nome na tela | Frase curta (máx. 1 linha) |
|---|---|---|
| 7 | Aplicação | Único acesso do processo à rede |
| 6 | Apresentação | Representação comum da informação |
| 5 | Sessão | Organiza e sincroniza o diálogo |
| 4 | Transporte | Transferência transparente |
| 3 | Rede | Independência de roteamento |
| 2 | Enlace de dados | Vizinhos diretos e erros do meio |
| 1 | Física | Bits no meio físico |

> **Restrição obrigatória:** não colar ícone ou nome de protocolo nas caixas das camadas. Colar
> protocolo na figura ensina o modelo como implementação, que é justamente o erro que esta aula
> combate. Ver `research/research.md`, seção 9.

**SEG-014 — correção explícita (camada 3)**
**BLOCOS (layout `split`):**
| Errado | O que a norma diz |
|---|---|
| "A camada do IP" | Independência de roteamento e encaminhamento |

**SEG-018 — relay**
**TÍTULO:** Passagem, não destino
**NOTA:** Em um sistema de relay, só as camadas de baixo participam no encaminhamento daquele
tráfego. O equipamento continua tendo camadas altas, para ser gerenciado.

> **Restrição obrigatória — contagem de camadas nas pilhas.** Toda pilha de **sistema final**
> desenhada em qualquer slide precisa ter **as sete camadas, numeradas de 1 a 7, sem lacuna**, e as
> duas pontas precisam ser **idênticas** entre si. Só a pilha do **relay** aparece parcial, com as
> camadas 1, 2 e 3.
>
> Existe para impedir a regressão detectada em DIV-002, onde uma ponta omitiu a camada 5 e a outra
> omitiu a camada 4. Contradiz CLM-001, que é o claim mais básico da aula, e aparece logo depois do
> slide que enumera as sete camadas.
>
> Se por espaço a pilha precisar ser reduzida, ela deve ser rotulada como recorte — nunca
> apresentada como sistema final completo com menos de sete caixas.

---

## Bloco 5 — Encapsulamento (SEG-019 a SEG-023)

**EYEBROW:** PASSO 1 DE 3
**TÍTULO:** Três nomes que você vai usar sempre
**BLOCOS:**
- `[MONO]` PCI — informação de controle de protocolo
- `[MONO]` SDU — carga que a camada não interpreta
- `[MONO]` PDU — PCI + dados do usuário

**SEG-020 — a equação (foco único)**
**CENTRO:** `[MONO]` SDU + PCI = PDU
**NOTA:** A PDU de uma camada vira a carga da camada de baixo.

**SEG-022 — a correção mais importante da aula**
**EYEBROW:** ERRO COMUM
**TÍTULO:** O cabeçalho não vai necessariamente na frente
**BLOCOS (layout `split`):**
| O que se ouve | O que a norma registra |
|---|---|
| "Cabeçalho na frente dos dados" | Nenhuma relação de posição definida |
| — | `[MONO]` Ethernet: FCS no fim do quadro |

> **Restrição obrigatória para o diagrama de encapsulamento:** ao menos uma camada precisa mostrar
> informação de controle **depois** dos dados. Um diagrama que só empilha cabeçalhos à esquerda
> contradiz a narração deste segmento.

---

## Bloco 6 — Evidência (SEG-024)

**EYEBROW:** EVIDÊNCIA
**TÍTULO:** A mesma estrutura, em bytes
**BLOCOS:**
- Enlace
- Rede
- Transporte
- Carga não interpretada

> **Pendente de artefato (OQ-001).** Nenhum valor concreto — endereço, porta, byte — pode ser
> exibido até existir captura real e sanitizada. Enquanto isso, apenas a estrutura por camada.
> Proibido compor uma tela de analisador fictícia.

---

## Bloco 7 — Procedência dos nomes (SEG-025 a SEG-027)

**EYEBROW:** RIGOR DE FONTE
**TÍTULO:** Esses nomes não são do OSI

**SEG-026 — a contagem (layout `data`, foco central da aula)**
| Termo procurado no texto integral | Ocorrências |
|---|---|
| `[MONO]` packet | `[MONO]` 0 |
| `[MONO]` datagram | `[MONO]` 0 |
| `[MONO]` frame | `[MONO]` 8 — todas em "framework" |
| `[MONO]` segment | só a operação de segmentar |

**METRIC:** `[MONO]` PDU
**NOTA:** O único termo do OSI para unidade de dados.

**SEG-027 — a tabela de procedência**
| Nome | Norma que define o termo |
|---|---|
| quadro | `[MONO]` IEEE 802 |
| datagrama | `[MONO]` RFC 791 (IP) |
| segmento | `[MONO]` RFC 9293 (TCP) |

---

## Bloco 8 — O modelo real da Internet (SEG-028 a SEG-031)

**EYEBROW:** OSI × INTERNET
**TÍTULO:** Por que tanta gente desenha quatro
**BLOCOS:**
- `[MONO]` RFC 1122
- Aplicação
- Transporte
- Internet
- Enlace

**NOTA:** Camada *internet*, não "rede". Camada de *enlace*, não "enlace de dados".

**SEG-029 / SEG-030 — a comparação honesta**
> **Restrição obrigatória (corrigida após TR1-001):** o bloco Aplicação da Internet deve aparecer
> abrangendo **as camadas 6 e 7** do OSI — apresentação e aplicação — porque é isso, e só isso, que
> o RFC 1122 afirma. A camada 5, sessão, deve ser representada como **sem camada separada** no modelo
> da Internet: sem seta, sem correspondência, visualmente órfã. É a ausência que ensina.
>
> Proibido desenhar sete caixas alinhadas com quatro, lado a lado. E proibido fazer o bloco
> Aplicação cobrir 5, 6 e 7 — isso atribuiria à fonte uma afirmação que ela não faz.

**BLOCOS:**
- Aplicação da Internet = apresentação + aplicação do OSI
- Sessão: sem camada separada
- "É camada 6" não tem apoio no documento

**SEG-031 — limite do modelo**
**NOTA:** Camadas estritas são um modelo imperfeito. Bússola, não lei da física.

---

## Bloco 9 — Casos que não mapeiam (SEG-032)

**EYEBROW:** NEM TUDO TEM NÚMERO
**BLOCOS (layout `split`):**
| Camada 2 | TLS |
|---|---|
| Duas sub-camadas | Não se declara 5, 6 nem 7 |
| Sub-camada é conceito do próprio OSI | Exige fluxo confiável e em ordem |

> **Restrição obrigatória — ordem das sub-camadas.** No diagrama da camada 2, **`[MONO]` LLC fica
> ACIMA de `[MONO]` MAC**. Não é escolha estética. IEEE Std 802 [CLM-018]: *"the LLC sublayer
> operating over a MAC sublayer"* e *"The MAC sublayer [...] exists between the Physical layer and
> the LLC sublayer"*. Empilhar MAC em cima inverte a informação que o slide existe para transmitir.
>
> Ordem de cima para baixo: `LLC (Logical Link Control)` — linha divisória — `MAC (Medium Access
> Control)`. Abaixo do bloco, a camada física.
>
> No diagrama do TLS: `TLS` acima, `Transporte (ex.: TCP)` abaixo, **sem número de camada em
> nenhum dos dois**.

---

## Bloco 10 — Diagnóstico (SEG-033 a SEG-037)

**EYEBROW:** MÉTODO DA ESCOLA — NÃO É NORMA

> **Restrição obrigatória:** este eyebrow, ou equivalente, precisa estar presente em **todas** as
> cenas deste bloco. O claim de diagnóstico é EDITORIAL (CLM-021) e não pode aparecer com a mesma
> autoridade visual das cenas que citam a norma. Ver `research/evidence-ledger.md`.

**TÍTULO:** De baixo para cima

| # | A pergunta | A evidência |
|---|---|---|
| 1 | Existe enlace? | Estado da porta, erros, potência óptica |
| 2 | Os vizinhos se veem? | Tabela de endereços, resolução, VLAN da porta |
| 3 | Existe caminho? | Endereço, máscara, gateway, rotas |
| 4 | A porta aceita conexão? | Sessão, retransmissão |
| 5–7 | O serviço responde certo? | Nome, certificado, código, log |

> **Restrição obrigatória — a escada não pode perder degrau.** Se a escada for dividida em dois
> quadros, o corte é: **primeiro quadro com os degraus 1, 2 e 3; segundo quadro com 4 e 5–7.**
> Nenhum degrau repetido entre os dois, nenhum degrau ausente, e a numeração sempre crescente.
>
> Existe para impedir a regressão de DIV-006, onde o segundo quadro repetiu o degrau 2 e omitiu o
> degrau 3 — justamente a camada onde está o erro mais comum que a aula destaca.
>
> Nenhuma faixa de texto pode cobrir um degrau. Se a frase de fechamento não couber, ela vai para um
> terceiro quadro.

**SEG-035 — destaque próprio, não é linha de tabela**
**EYEBROW:** ERRO MAIS COMUM
**TÍTULO:** Ida e volta
**NOTA:** Falha de retorno se parece exatamente com falha de ida.

**SEG-037**
**NOTA:** A ordem não acerta a camada de primeira. Ela ordena as hipóteses.

---

## Bloco 11 — Recapitulação (SEG-038 a SEG-040)

**EYEBROW:** RESUMO
Grade de cartões numerados, conforme `brain/visual-language.md`.

| Nº | Título | Frase |
|---|---|---|
| 01 | Referência | Descreve responsabilidade, não implementação |
| 02 | Serviço e protocolo | Um para cima, outro para o lado |
| 03 | Encapsulamento | Controle acrescentado a uma carga não interpretada |
| 04 | Procedência | Quadro, datagrama e segmento não são do OSI |
| 05 | Internet real | Quatro camadas; aplicação combina 6 e 7. Sessão sem camada separada |
| 06 | Método | De baixo para cima |

**SEG-040 — exercício**
**EYEBROW:** SEU EXERCÍCIO
**TÍTULO:** Sete responsabilidades, uma coisa que você usa
**NOTA:** Onde não conseguir preencher, achou o próximo assunto de estudo.

---

## Restrições visuais consolidadas (para o `visual-director` e o Codex #2)

Cada item abaixo existe porque a narração afirma o contrário do erro comum. Um visual que viole
qualquer um deles **contradiz a fala** e deve ser barrado na revisão.

1. Nenhum ícone ou nome de protocolo dentro das caixas das sete camadas.
2. O diagrama de encapsulamento precisa mostrar controle **depois** dos dados em ao menos uma camada.
3. A comparação OSI × Internet precisa mostrar Aplicação abrangendo **6 e 7**, com a camada 5
   (sessão) explicitamente sem camada separada — nunca 7 caixas alinhadas com 4, e nunca Aplicação
   cobrindo 5, 6 e 7.
4. Nenhum valor concreto de captura enquanto OQ-001 estiver aberta. Nenhuma tela de analisador
   fictícia.
5. Toda cena do bloco 10 marcada visualmente como método da escola, não como norma.
6. Nenhuma tabela de PDU que atribua quadro/pacote/segmento ao OSI.
7. Toda pilha de sistema final tem as **sete** camadas, 1 a 7, sem lacuna, e as duas pontas são
   idênticas. Só o relay aparece parcial (1 a 3).
8. Na camada 2, **LLC acima de MAC**. Nunca o inverso.
9. A escada de diagnóstico não repete nem omite degrau: 1–2–3 no primeiro quadro, 4 e 5–7 no
   segundo. Nenhuma faixa de texto cobrindo degrau.

> As restrições 7, 8 e 9 foram acrescentadas em 2026-07-29 após a análise do primeiro deck
> (`source/slide-analysis.md`). Cada uma corresponde a um erro factual que ocorreu por **omissão
> deste documento**: ele não especificava contagem de camadas, ordem das sub-camadas nem o corte da
> escada. O gerador não errou por conta própria — ele preencheu lacunas da especificação.
