# Research — Modelo OSI (fundamentos-01-modelo-osi)

Pesquisa fechada em 2026-07-29. Todo claim técnico aqui aponta para um `CLM-xxx` do
`evidence-ledger.md`. Este documento **não é o roteiro** — é o território que o roteirista pode usar.

---

## 1. O que o modelo OSI é, e o que ele não é

O OSI Basic Reference Model é uma **norma internacional em vigor**, publicada em texto idêntico como
ITU-T Rec. X.200 (07/94) e ISO/IEC 7498-1:1994 [CLM-002]. Ele define sete camadas [CLM-001].

O ponto que organiza toda a aula: o padrão é um **modelo de referência**, não uma especificação de
implementação. Ele descreve *responsabilidades* e *fronteiras de serviço*, e diz isso de si mesmo —
a Introdução afirma que o modelo não entra no nível de detalhe necessário para definir precisamente
serviços e protocolos, mas fornece um "conceptual and functional framework" para que equipes
internacionais trabalhem de forma produtiva e independente.

Consequência prática que o aluno precisa levar: **existe uma diferença entre o modelo OSI e a pilha
de protocolos OSI.** O modelo continua sendo a linguagem comum da indústria — o IEEE 802 se declara
explicitamente derivado dele [CLM-018]. A pilha de protocolos OSI é que não venceu comercialmente.
Dizer "OSI morreu" confunde as duas coisas e deve ser evitado.

## 2. A engrenagem conceitual (o que faz o modelo funcionar)

Três definições sustentam tudo o resto, e vale gastar tempo nelas antes de listar as sete camadas:

**Camada** é uma subdivisão da arquitetura formada por subsistemas do mesmo nível [CLM-003].

**Serviço ≠ protocolo.** O `(N)-service` é a capacidade da camada N *e das camadas abaixo dela*,
oferecida às entidades N+1 na fronteira entre as duas [CLM-003]. O `(N)-protocol` é o conjunto de
regras e formatos entre entidades pares — entidades da mesma camada, em máquinas diferentes
[CLM-003, CLM-004]. Essa distinção é o que permite trocar o protocolo sem trocar o serviço: é por
isso que a aplicação não muda quando a rede vira Wi-Fi em vez de cabo.

**Serviço é cumulativo.** As camadas 1 a 6, junto com o meio físico, fornecem um "step-by-step
enhancement of communication services", e a fronteira entre duas camadas é exatamente o estágio
onde um padrão de serviço é definido [CLM-011]. Modelo mental correto: cada camada não "faz sua
parte isolada" — ela **entrega um serviço melhor** do que recebeu da camada de baixo.

## 3. Dados: SDU, PCI e PDU — e o que realmente é encapsulamento

O padrão nomeia três coisas [CLM-005]:

- **PCI** (protocol-control-information): a informação que as entidades pares trocam para coordenar
  sua operação conjunta. É o "cabeçalho", em linguagem de campo.
- **SDU** (service-data-unit): a informação cuja identidade é preservada na travessia e que **não é
  interpretada** pelas entidades que a transportam. É a carga útil — e "não interpretada" é a
  definição formal dela.
- **PDU** (protocol-data-unit): a unidade especificada em um protocolo, consistindo em PCI e
  possivelmente user-data.

E o encapsulamento, na letra do padrão: "Within a layer, (N)-protocol-control-information is added
to the (N)-service-data-unit to form an (N)-protocol-data-unit" [CLM-006]. Depois, essa PDU da
camada N pode ser mapeada como SDU da camada N–1 — e o ciclo repete descendo a pilha.

Três precisões que separam esta aula do material comum:

1. **O padrão não diz que o cabeçalho vai na frente.** A Figura 9 tem uma nota explícita: a figura
   não implica nenhuma relação posicional entre PCI e user-data dentro da PDU [CLM-007]. Isso não é
   preciosismo: o FCS do Ethernet é um *trailer*, vem depois dos dados. Formulação correta na
   narração: "cada camada acrescenta sua informação de controle" — não "coloca um cabeçalho na
   frente".
2. **Nem sempre é 1 para 1.** O padrão prevê *segmenting* (uma SDU virando várias PDUs), *blocking*
   e *concatenation* [CLM-008]. A aula menciona só segmenting, porque é o que reaparece em
   fragmentação e MSS. Blocking e concatenation ficam para depois — decisão consciente, registrada.
3. **A SDU é opaca por definição.** É por isso que o switch não precisa entender HTTP.

## 4. As sete camadas, na letra do padrão

Todos os trechos verbatim estão em [CLM-010]. O que segue é a leitura para ensino.

| # | Camada | O que o padrão diz que ela faz | PDU no mundo real | Fonte do nome da PDU |
|---|---|---|---|---|
| 7 | Application | Único meio de o processo de aplicação acessar o ambiente OSI | mensagem / dados | — |
| 6 | Presentation | Representação da informação; representação comum entre entidades de aplicação | — | — |
| 5 | Session | Organizar e sincronizar o diálogo e gerenciar a troca de dados | — | — |
| 4 | Transport | Transferência **transparente** de dados, liberando as camadas de cima da preocupação com *como* a transferência confiável e econômica acontece | segment (TCP) | RFC 9293 [CLM-017] |
| 3 | Network | Meios para transmissão entre entidades de transporte, dando-lhes **independência de roteamento e relay** | datagram (IP) | RFC 791 [CLM-017] |
| 2 | Data Link | Meios para estabelecer/manter/liberar conexões de enlace e transferir SDUs de enlace; **detecta e possivelmente corrige** erros da camada física | frame | IEEE 802 [CLM-017] |
| 1 | Physical | Meios mecânicos, elétricos, funcionais e procedurais para ativar, manter e desativar conexões físicas para transmissão de bits | bit | — |

Duas leituras que valem a aula inteira:

- A camada 3 **não** é definida como "a camada do IP". Ela é definida como a camada que dá
  independência de roteamento. O IP é uma implementação dessa responsabilidade.
- A camada 4 **não** é definida como "a camada do TCP", e a palavra-chave do padrão é
  *transparente*: a camada 4 esconde da aplicação como a confiabilidade foi obtida.

Sobre relay: quando o meio físico não liga todos os sistemas diretamente, alguns sistemas atuam
apenas como *relay open systems*, e as funções que suportam o forwarding ficam **nas camadas
baixas** [CLM-012]. É a justificativa formal de por que switch e roteador não têm pilha completa —
e prepara as aulas 09 e 10.

## 5. A armadilha terminológica (ponto alto da aula)

A tabela popular "camada 2 = frame, 3 = packet, 4 = segment" é apresentada como se fosse
terminologia OSI. **Não é.** Contagem no texto integral do X.200 [CLM-009]:

- `packet`: **0 ocorrências**
- `datagram`: **0 ocorrências**
- `frame`: 8 ocorrências, **todas dentro de "framework"** — nenhuma como unidade de dados
- `segment`: aparece apenas como a *operação* de segmenting, nunca como nome da PDU da camada 4

O termo do padrão é `(N)-PDU`. Os nomes populares são corretos **cada um no escopo da sua norma**:
frame vem do IEEE 802, datagram do RFC 791, segment do RFC 9293 [CLM-017].

Como ensinar sem confundir o iniciante: não negar os nomes — o aluno vai encontrá-los em todo lugar
e precisa deles. A formulação certa é de **procedência**: "esses nomes são reais e você vai usá-los;
só não são do OSI. Cada um vem da norma do seu protocolo." Isso ensina o nome *e* o rigor de fonte
ao mesmo tempo.

## 6. OSI vs. o modelo real da Internet

RFC 1122 — Internet Standard, em vigor — define **quatro** camadas, com estes nomes exatos:
Application, Transport, Internet, Link [CLM-013]. Repare: "Internet Layer", não "Network"; "Link
Layer", não "Data Link".

O mapeamento não é 1:1, e o próprio RFC diz onde quebra: a camada de aplicação da suíte Internet
"essentially combines the functions of the top two layers -- Presentation and Application -- of the
OSI reference model", e a suíte **não subdivide** a camada de aplicação [CLM-014].

Precisão obrigatória (corrigida após TR1-001): a fonte atribui à camada de aplicação da Internet as
funções de **apresentação e aplicação** — as duas de cima, camadas 6 e 7. Ela **não** diz que a
camada de sessão foi absorvida ali. O que se pode afirmar sobre a sessão é apenas o que a
enumeração mostra: entre as quatro camadas do RFC 1122 [CLM-013], não existe camada de sessão.
A ausência de camada separada é o fato; tanto a absorção pela aplicação quanto a alegação de que nada cuida de sessão seriam inferências sem fonte.

A consequência direta é que afirmações do tipo "HTTPS é camada 6" não têm apoio em fonte primária.

O RFC 1122 também é explícito sobre o limite do próprio layering: "strict layering is an imperfect
model, both for the protocol suite and for recommended implementation approaches. Protocols in
different layers interact in complex and sometimes subtle ways" [CLM-015]. Vale citar: vem de quem
escreveu a norma da Internet, não de um crítico externo.

Vocabulário equivalente, útil quando o aluno lê documentação antiga: host ≡ "End-System";
gateway/router ≡ "Intermediate System" [CLM-016].

Se o roteirista quiser fechar a seção com uma nota de maturidade, existe crítica arquitetural
documentada na própria IETF — RFC 3439, seção 3, "Layering Considered Harmful" [CLM-019]. **Uma
frase, no máximo**, e com a ressalva de que é RFC Informational, não norma. Não transformar em tese:
o iniciante precisa primeiro do modelo para depois poder criticá-lo.

## 7. Casos que não caem em uma camada limpa

Servem para vacinar o aluno contra a expectativa de que tudo tem um número.

- **TLS.** A RFC 8446 não se atribui número de camada nenhum. Ela diz que o único requisito do
  transporte abaixo é "a reliable, in-order data stream", e que protocolos de nível mais alto
  assentam sobre ela transparentemente [CLM-020]. Formulação segura: descrever a posição funcional
  (acima do transporte confiável, abaixo da aplicação) sem cravar um número.
- **Sub-camadas da camada 2.** A camada de enlace é estruturada como duas sub-camadas, LLC sobre
  MAC, e a família IEEE 802 cobre justamente as duas camadas mais baixas do OSI [CLM-018]. E isso
  **não** é uma violação do modelo: o próprio X.200 define "sublayer" como subdivisão de uma camada
  [CLM-003]. Sub-camada é uso previsto, não exceção.
- **VPN e tunelamento.** Encapsular uma pilha dentro de outra rompe a leitura linear "uma camada por
  nível". Mencionar como existência, sem detalhar — é assunto de curso posterior.

## 8. Diagnóstico camada a camada

**Atenção do revisor: esta seção é EDITORIAL [CLM-021].** A sequência abaixo não é prescrita por
nenhuma norma. É prática de campo e escolha pedagógica desta escola, derivada logicamente de
[CLM-011] — se cada camada depende do serviço da de baixo, verificar de baixo para cima elimina
causas na ordem em que elas se sustentam. A narração deve marcar isso linguisticamente ("uma forma
prática de organizar", "na prática, o que funciona é") e nunca dizer "o padrão determina".

| Camada | A pergunta | A evidência que responde |
|---|---|---|
| 1 — Física | O enlace existe eletricamente? | LED/estado da porta, contadores de erro, potência óptica |
| 2 — Enlace | Os vizinhos diretos se veem? | tabela MAC, ARP resolvido, VLAN correta na porta |
| 3 — Rede | Existe caminho de ida **e de volta**? | endereço/máscara, gateway, tabela de rotas, teste de alcance |
| 4 — Transporte | A porta do serviço aceita conexão? | teste de porta, retransmissão, sessão que abre e cai |
| 5–7 — Aplicação | O serviço responde corretamente? | nome resolvido, certificado válido, código de resposta, log do serviço |

Dois avisos honestos que valem mais que a tabela:

- **Assimetria.** A camada 3 pergunta por caminho de ida *e volta*. Falha de retorno é uma das
  causas mais comuns de "ping não funciona" e não aparece se você só pensa na ida.
- **O modelo é bússola, não algoritmo.** Camadas interagem de forma sutil [CLM-015]. O valor do
  método é ordenar hipóteses e evitar pular para a aplicação quando o problema é de cabo, não
  garantir que o problema esteja em uma camada só.

## 9. O que a aula deve mostrar visualmente

Insumo para o `visual-director` e o `powerpoint-visual-analyst`:

1. **A pilha de sete camadas**, com número e nome, sem ícones de protocolo colados nela (colar
   protocolos na figura induz o erro de tratar o modelo como implementação).
2. **Encapsulamento passo a passo**: a mesma SDU descendo, ganhando PCI a cada nível. Precisa mostrar
   PCI podendo aparecer **também depois** dos dados, para não contradizer [CLM-007].
3. **O par**: duas pilhas lado a lado, com a seta horizontal de protocolo par entre camadas de mesmo
   nível e as setas verticais de serviço — é a Figura 11 do padrão.
4. **Relay**: uma pilha do meio com só as camadas baixas ativas [CLM-012].
5. **Comparação honesta OSI × RFC 1122**: a camada Application da Internet abrangendo **6 e 7**, e
   a camada 5 (sessão) representada como sem camada separada — não alinhada lado a lado, e não coberta
   pela aplicação.
6. **A tabela de procedência dos nomes de PDU**, com a coluna "norma que define o termo".
7. **A tabela de diagnóstico**, visualmente marcada como método da escola e não como norma.

## 10. Verificação de escopo

- Território coberto: definição e status da norma, conceitos estruturais, unidades de dados,
  encapsulamento, as sete camadas, relay, terminologia de PDU, modelo da Internet, casos que não
  mapeiam, diagnóstico.
- Nenhuma transição técnica exigirá invenção do roteirista.
- Fora de escopo (aulas seguintes do módulo): formato de cabeçalho de qualquer protocolo, Ethernet,
  ARP, IPv4/IPv6, switching, MAC learning, TCP/IP em profundidade.
- Pendência única que afeta produção: a captura real (OQ-001).

---

**STATUS:** PASS_WITH_WARNINGS — todos os claims técnicos fecham em fonte primária Nível A. O aviso
é operacional, não factual: a evidência de captura (OQ-001) ainda não existe como artefato e o
roteiro precisa ser escrito de modo a não depender de bytes inventados.
