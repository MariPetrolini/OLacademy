# Evidence Ledger — fundamentos-01-modelo-osi

Cada claim que a aula fará está registrado aqui com fonte primária, localização exata e trecho
verbatim. Data de acesso de todas as verificações: **2026-07-29**.

Legenda de tipo: `FATO` = documentado em fonte primária · `INFERÊNCIA` = conclusão do pesquisador a
partir de fatos registrados · `EDITORIAL` = decisão didática da escola, não afirmação técnica.

---

## CLM-001 — O modelo contém sete camadas, nomeadas e numeradas
**Tipo:** FATO · **Fonte:** A1, cláusula 6.1.2
**Verbatim:**
> "6.1.2 The Reference Model contains seven layers:
> a) the Application Layer (layer 7);
> b) the Presentation Layer (layer 6);
> c) the Session Layer (layer 5);
> d) the Transport Layer (layer 4);
> e) the Network Layer (layer 3);
> f) the Data Link Layer (layer 2); and
> g) the Physical Layer (layer 1)."

Observação didática: o próprio padrão enumera de cima para baixo (7 → 1). A numeração 1–7 é do
padrão, não convenção posterior.

---

## CLM-002 — X.200 e ISO/IEC 7498-1 são o mesmo texto
**Tipo:** FATO · **Fonte:** A1, Foreword
**Verbatim:**
> "The text of ITU-T Recommendation X.200 was approved on 1st of July 1994. The identical text is also published as ISO/IEC International Standard 7498-1."

Consequência: citar "X.200" ou "ISO/IEC 7498-1" é citar a mesma norma. A aula deve mencionar as duas
designações uma vez, para o aluno reconhecer ambas na literatura.

---

## CLM-003 — Definições estruturais: camada, sub-camada, serviço, protocolo, SAP
**Tipo:** FATO · **Fonte:** A1, cláusula 5.2.1
**Verbatim:**
> "5.2.1.2 (N)-layer: A subdivision of the OSI architecture, constituted by subsystems of the same rank (N)."
> "5.2.1.4 sublayer: A subdivision of a layer."
> "5.2.1.5 (N)-service: A capability of the (N)-layer and the layers beneath it, which is provided to (N+1)-entities at the boundary between the (N)-layer and the (N+1)-layer."
> "5.2.1.8 (N)-service-access-point, (N)-SAP: The point at which (N)-services are provided by an (N)-entity to an (N+1)-entity."
> "5.2.1.9 (N)-protocol: A set of rules and formats [...]"

Ponto de ensino crítico: **serviço ≠ protocolo.** O serviço é a capacidade oferecida na fronteira
para cima; o protocolo é o conjunto de regras entre entidades pares. O padrão define os dois
separadamente, e a fronteira entre camadas é exatamente onde um padrão de serviço é definido
(ver CLM-011).

Ponto de ensino crítico 2: **"sublayer" é um conceito do próprio OSI** (5.2.1.4). Portanto dizer
que a camada 2 tem sub-camadas não viola o modelo — o modelo prevê isso.

---

## CLM-004 — Entidades pares são entidades da mesma camada
**Tipo:** FATO · **Fonte:** A1, cláusula 5.2.1.3
**Verbatim:**
> "5.2.1.3 peer-(N)-entities: Entities within the same (N)-layer."

---

## CLM-005 — PDU, SDU, PCI e user-data
**Tipo:** FATO · **Fonte:** A1, cláusula 5.6.1
**Verbatim:**
> "5.6.1.1 (N)-protocol-control information: Information exchanged between (N)-entities to co-ordinate their joint operation."
> "5.6.1.2 (N)-user-data: The data transferred between (N)-entities on behalf of the (N+1)-entities for whom the (N)-entities are providing services."
> "5.6.1.3 (N)-protocol-data-unit: A unit of data specified in an (N)-protocol and consisting of (N)-protocol-control-information and possibly (N)-user-data."
> "5.6.1.4 (N)-service-data-unit: An amount of information whose identity is preserved when transferred between peer-(N+1)-entities and which is not interpreted by the supporting (N)-entities."

Ponto de ensino: a SDU é definida por **não ser interpretada** pela camada que a transporta. Essa é
a definição formal de "carga útil opaca" — e é o que permite o modelo funcionar.

---

## CLM-006 — Encapsulamento, na definição do padrão
**Tipo:** FATO · **Fonte:** A1, cláusula 5.8.8.5.2
**Verbatim:**
> "Within a layer, (N)-protocol-control-information is added to the (N)-service-data-unit to form an (N)-protocol-data-unit when no segmenting or blocking is performed [see Figure 10 a)]."

Este é o claim central da aula. Note que o padrão descreve o mecanismo sem usar a palavra
"encapsulation" nesta cláusula: ele diz que o PCI *é adicionado* à SDU para *formar* a PDU.

---

## CLM-007 — O padrão NÃO diz que o cabeçalho vai na frente
**Tipo:** FATO · **Fonte:** A1, Figura 9, NOTE 2
**Verbatim:**
> "2 This figure does not imply any positional relationship between protocol-control-information and user-data in protocol-data-unit."

Ponto de ensino: por isso existe *trailer* no mundo real (o FCS do Ethernet vem depois dos dados).
A aula deve evitar afirmar "cada camada adiciona um cabeçalho na frente" como se fosse regra do
modelo. Formulação correta: cada camada adiciona sua informação de controle.

---

## CLM-008 — Segmenting, blocking e concatenation
**Tipo:** FATO · **Fonte:** A1, cláusulas 5.8.8.5.1 a 5.8.8.5.4
**Verbatim (recortes):**
> "It may be necessary to perform segmenting, i.e. to map an (N)-service-data-unit into more than one (N)-protocol-data-unit."
> "Blocking is the mechanism where several (N)-service-data-units with added (N)-protocol-control-information form an (N)-protocol-data-unit."
> "The Reference Model also permits concatenation where several (N)-protocol-data-units are concatenated into a single (N–1)-service-data-unit."

Escopo: a aula menciona apenas *segmenting* (uma SDU virando várias PDUs), porque é o que o aluno
verá em fragmentação e MSS. Blocking e concatenation ficam fora de escopo, mas registrados aqui
para o revisor confirmar que a simplificação foi consciente.

---

## CLM-009 — "Frame", "packet", "segment" e "datagram" NÃO são terminologia do OSI
**Tipo:** FATO (verificação por contagem em texto integral) · **Fonte:** A1, documento completo
**Método:** contagem de ocorrências no texto integral extraído do PDF oficial (63 páginas):

| Termo | Ocorrências em X.200 | Observação |
|---|---|---|
| `packet` / `Packet` | **0** | não aparece nenhuma vez |
| `datagram` / `Datagram` | **0** | não aparece nenhuma vez |
| `frame` | 8 | **todas as 8 dentro da palavra "framework"/"frameworks"** — nunca como unidade de dados |
| `segment` / `Segment` | 6 | somente no sentido da *operação* de segmenting (5.8.8.5), nunca como nome da PDU da camada 4 |

**Conclusão auditável:** a tabela popular "camada 2 = frame, camada 3 = packet, camada 4 = segment"
**não vem do ISO/IEC 7498-1**. O termo do padrão é `(N)-PDU`. Os nomes populares vêm de outras
normas, cada uma no seu escopo (CLM-017).

Este é um dos pontos de maior valor didático da aula e um erro presente em boa parte do material
de terceiros. O `powerpoint-visual-analyst` deve verificar especificamente se o slide da escola
comete esse erro.

---

## CLM-010 — Propósito de cada camada, na letra do padrão
**Tipo:** FATO · **Fonte:** A1, cláusulas 7.1.2 a 7.7.2
**Verbatim (recortes por camada):**

- **7 — Application** (7.1.2.1): "As the highest layer in the Reference Model of Open Systems Interconnection, the Application Layer provides the sole means for the application process to access the OSIE."
- **6 — Presentation** (7.2.2.1–7.2.2.2): "The Presentation Layer provides for the representation of information that application-entities either communicate or refer to in their communication." / "provides for common representation of the data transferred between application-entities."
- **5 — Session** (7.3.2.1): "The purpose of the Session Layer is to provide the means necessary for cooperating presentation-entities to organize and to synchronize their dialogue and to manage their data exchange."
- **4 — Transport** (7.4.2.1): "The transport-service provides transparent transfer of data between session-entities and relieves them from any concern with the detailed way in which reliable and cost effective transfer of data is achieved."
- **3 — Network** (7.5.2.1): "The Network Layer provides the functional and procedural means for connectionless-mode or connection-mode transmission among transport-entities and, therefore, provides to the transport-entities independence of routing and relay considerations."
- **2 — Data Link** (7.6.2.1–7.6.2.2): "The Data Link Layer provides functional and procedural means for connectionless-mode among network-entities, and for connection-mode for the establishment, maintenance, and release data-link-connections among network-entities and for the transfer of data-link-service-data-units." / "The Data Link Layer detects and possibly corrects errors which may occur in the Physical Layer."
- **1 — Physical** (7.7.2): "The Physical Layer provides the mechanical, electrical, functional and procedural means to activate, maintain, and de-activate physical-connections for bit transmission between data-link-entities."

Ponto de ensino: repare que a camada 3 é definida como a que dá **independência de roteamento e
relay** — não como "a camada do IP". E a camada 4 como a que dá **transferência transparente**,
não como "a camada do TCP". O padrão descreve responsabilidade, não protocolo.

---

## CLM-011 — A fronteira entre camadas é onde um padrão de serviço é definido
**Tipo:** FATO · **Fonte:** A1, cláusula 6.1.5
**Verbatim:**
> "Layers 1 to 6, together with the physical media for OSI provide a step-by-step enhancement of communication services. The boundary between two layers identifies a stage in this enhancement of services at which an OSI service standard is defined while the functioning of the layers is governed by OSI protocol standards."

Ponto de ensino: "aprimoramento passo a passo do serviço" é o modelo mental correto — cada camada
entrega um serviço melhor que o da camada abaixo.

---

## CLM-012 — Sistemas de relay: o forwarding vive nas camadas baixas
**Tipo:** FATO · **Fonte:** A1, cláusula 6.1.6
**Verbatim:**
> "When the physical media for OSI do not link all open systems directly, some open systems act only as relay open systems, passing data to other open systems. The functions and protocols which support the forwarding of data are then provided in the lower layers."

Ponto de ensino: é isso que justifica switch e roteador não terem pilha completa. Fundamenta a
aula 09 (Switches) e 10 (Roteadores).

---

## CLM-013 — A arquitetura da Internet tem quatro camadas
**Tipo:** FATO · **Fonte:** A2, seção 1.1.3
**Verbatim:**
> "The protocol layers used in the Internet architecture are as follows [INTRO:4]:
> o Application Layer
> o Transport Layer
> o Internet Layer
> o Link Layer"

Note os nomes exatos: **Internet Layer** (não "Network") e **Link Layer** (não "Data Link"). A aula
deve usar os nomes corretos de cada modelo, sem misturar.

---

## CLM-014 — O mapeamento OSI ↔ Internet não é 1:1
**Tipo:** FATO · **Fonte:** A2, seção 1.1.3
**Verbatim:**
> "The application layer of the Internet suite essentially combines the functions of the top two layers -- Presentation and Application -- of the OSI reference model."
> "The Internet suite does not further subdivide the application layer, although some of the Internet application layer protocols do contain some internal sub-layering."

Consequência para a aula: a Internet real não tem camada 5 e 6 separadas. Dizer "HTTPS é camada 6"
não tem apoio em fonte primária.

---

## CLM-015 — A própria IETF diz que camadas estritas são um modelo imperfeito
**Tipo:** FATO · **Fonte:** A2, seção 1.3.1
**Verbatim:**
> "However, strict layering is an imperfect model, both for the protocol suite and for recommended implementation approaches. Protocols in different layers interact in complex and sometimes subtle ways, and particular functions often involve multiple layers. There are many design choices in an implementation, many of which involve creative 'breaking' of strict layering."

---

## CLM-016 — Vocabulário equivalente entre os dois mundos
**Tipo:** FATO · **Fonte:** A2, seção 1.1.1
**Verbatim:**
> "An Internet host corresponds to the concept of an 'End-System' used in the OSI protocol suite [INTRO:13]."
> "The networks are interconnected using packet-switching computers called 'gateways' or 'IP routers' by the Internet community, and 'Intermediate Systems' by the OSI world [INTRO:13]."

---

## CLM-017 — De onde vêm os nomes populares das PDUs
**Tipo:** FATO · **Fontes:** A3, A4, A5

| Nome popular | Fonte primária que realmente o define | Verbatim |
|---|---|---|
| frame | A3 — IEEE Std 802-2001, 3.1.4 | "canonical format: The format of a MAC data frame in which the octets of any MAC addresses conveyed in the MAC user data field have the same bit ordering as in the Hexadecimal Representation." |
| datagram | A5 — RFC 791, 1.1 e 1.2 | "The internet protocol provides for transmitting blocks of data called datagrams from sources to destinations." / "[...] to deliver a package of bits (an internet datagram) from a source to a destination over an interconnected system of networks." |
| segment | A4 — RFC 9293 | "The application byte-stream is conveyed over the network via TCP segments, with each TCP segment sent as an Internet Protocol (IP) datagram." |

Formulação correta para a narração: esses nomes são corretos **no escopo de cada norma**. O que é
incorreto é atribuí-los ao OSI. Ver CLM-009.

---

## CLM-018 — A camada 2 tem sub-camadas: LLC sobre MAC
**Tipo:** FATO · **Fonte:** A3, cláusulas 6.1 e 6.2
**Verbatim:**
> "The IEEE 802 Standards encompass the functionality of the lowest two layers of the OSI/RM (i.e., Physical layer and Data Link layer) and the higher layers as they relate to LAN management."
> "For the mandatory packet services supported by all LANs and MANs, the Data Link layer is structured as two sublayers, with the LLC sublayer operating over a MAC sublayer."
> "The applicable part of the OSI/RM consists of the lowest two layers: the Data Link layer and the Physical layer. These map onto the same two layers in the IEEE LAN&MAN/RM. The MAC sublayer of the LAN&MAN/RM exists between the Physical layer and the LLC sublayer to provide a common service for the LLC sublayer."

Combinado com CLM-003 (o OSI define "sublayer"), isso mostra que sub-camadas não são exceção ao
modelo: são uso previsto dele.

---

## CLM-019 — Existe crítica arquitetural documentada ao layering
**Tipo:** FATO · **Fonte:** A7, seção 3
**Verbatim:** RFC 3439, seção 3, intitulada "Layering Considered Harmful", argumenta entre outros
pontos que "increased layering frequently increases complexity" e que operações de multiplexação e
segmentação "hide vital information that lower layers may need to optimize their performance".

**Restrição de uso:** RFC 3439 é **Informational**. A aula pode citá-la como "existe crítica
documentada na própria IETF", nunca como norma. Uso recomendado: uma frase, no fecho da seção de
divergência. Não transformar em tese da aula — o aluno iniciante precisa primeiro do modelo.

---

## CLM-020 — TLS não recebe número de camada em sua própria especificação
**Tipo:** FATO · **Fonte:** A6, seção 1
**Verbatim:**
> "The primary goal of TLS is to provide a secure channel between two communicating peers; the only requirement from the underlying transport is a reliable, in-order data stream."
> "TLS is application protocol independent; higher-level protocols can layer on top of TLS transparently."

Verificação negativa: RFC 8446 **não atribui** a si nenhum número de camada OSI.
Formulação segura para a narração: "a especificação do TLS não se declara camada 5, 6 ou 7 — ela
diz que exige um transporte confiável e ordenado embaixo, e que protocolos de nível mais alto
assentam sobre ela." Qualquer afirmação categórica do tipo "TLS é camada 6" está **sem fonte** e
não deve entrar no roteiro.

---

## CLM-021 — Roteiro de diagnóstico camada a camada
**Tipo:** EDITORIAL · **Fonte:** nenhuma — é decisão didática da escola
A sequência de diagnóstico ("subir a pilha": link → endereçamento → alcance → porta/serviço →
aplicação) **não** é prescrita por A1 nem A2. É prática de campo consolidada e escolha pedagógica
desta escola, derivada logicamente de CLM-011 (cada camada depende do serviço da de baixo).

A narração deve apresentá-la como **método de trabalho**, com marcação linguística explícita
("uma forma prática de organizar o diagnóstico", "na prática, o que funciona é"), nunca como
"o padrão determina". O revisor deve barrar qualquer formulação que faça o método parecer norma.

---

## Claims que a aula NÃO fará (armadilhas rejeitadas na pesquisa)

| Afirmação comum | Por que foi rejeitada |
|---|---|
| "OSI tem 7 camadas, TCP/IP tem 4, e elas se alinham lado a lado" | Contraria CLM-014. Alinhamento limpo não existe: a Application da Internet cobre 5, 6 e 7. |
| "Camada 2 = frame, 3 = packet, 4 = segment (terminologia OSI)" | Contraria CLM-009. Nenhum desses termos existe no X.200 como nome de PDU. |
| "Cada camada adiciona um cabeçalho na frente dos dados" | Contraria CLM-007. O padrão nega relação posicional; FCS do Ethernet é trailer. |
| "TLS/SSL é a camada 6" ou "camada 5" | Sem fonte. Ver CLM-020. |
| "A camada de sessão é onde ficam os cookies/login" | Sem fonte. 7.3.2.1 define sessão como organização e sincronização de diálogo entre entidades de apresentação. |
| "Existe camada 8 (usuário)" | Piada de indústria. Não entra nem como brincadeira, para não competir com o modelo que o aluno está formando. |
| "O modelo OSI foi abandonado / não serve mais" | Contraria o status de A1 (em vigor) e o uso normativo em A3. O modelo é referência viva; o que não se implementa é a **pilha** de protocolos OSI. Distinção obrigatória na narração. |

---

## Resumo

- **21 claims registrados.** 20 são FATO com fonte primária Nível A verificada em texto integral.
  1 é EDITORIAL, explicitamente marcado (CLM-021).
- **0 claims sustentados apenas em fonte secundária.**
- **0 conflitos de fonte não resolvidos.**
- **1 dependência de versão declarada** (A3, IEEE 802-2001 vs 802-2014 — OQ-002).
