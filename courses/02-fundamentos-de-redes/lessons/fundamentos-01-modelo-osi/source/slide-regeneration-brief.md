# Brief de regeração dos slides — fundamentos-01-modelo-osi

Documento pronto para alimentar o gerador de imagens. Substitui o deck atual, que tem 3 divergências
HIGH e 2 MEDIUM documentadas em `source/slide-analysis.md`.

**15 slides. Formato 1920×1080. Sem marca d'água de terceiro.**

## Regras globais

- **Idioma:** português do Brasil. Conferir ortografia — o deck anterior trouxe "Camad" por "Camada".
- **Paleta:** branco `#FFFFFF` e vermelho escuro `#771215` como cores de identidade; cinzas
  `#333333`, `#B6B6B6`, `#F1F1F1` para estrutura. Nenhuma outra cor.
- **Tipografia:** Barlow para títulos e texto de leitura. Monoespaçada **apenas para string
  técnica** (sigla de norma, nome de sub-camada, número de RFC, rótulo de dado). Não usar mono para
  prosa corrida — quando tudo é mono, nada se destaca como dado técnico.
- **Eyebrow:** linha superior curta, maiúscula, mono, com barra vermelha à esquerda.
- **Densidade:** 1 a 3 focos por slide. Não colocar a narração inteira na tela.
- **Sem logo de fabricante** e sem marca d'água de ferramenta.

## As cinco correções obrigatórias

Cada uma corrige um erro do deck anterior. São o motivo desta regeração.

| # | Slide | O que estava errado | O que deve ser |
|---|---|---|---|
| C1 | 06 | Pilhas com 6 caixas: uma ponta sem a camada 5, a outra sem a camada 4 | **Sete camadas, 1 a 7, sem lacuna, idênticas nas duas pontas.** Só o relay é parcial (1–3) |
| C2 | 12 | MAC desenhado acima de LLC | **LLC acima, MAC abaixo** |
| C3 | 15 | Cartão 05: "aplicação cobre 5, 6 e 7" | "aplicação **combina 6 e 7**. Sessão sem contraparte" |
| C4 | 11 | Camadas 7, 6 e 5 agrupadas numa caixa ligada a "Aplicação" | **Só 6 e 7 no grupo.** Camada 5 isolada, sem chave e sem linha |
| C5 | 14 | Escada repetia o degrau 2 e omitia o 3 | Continuar em **4** e **5–7**. Sem repetir, sem omitir |

---

## Slide 01 — O problema

**EYEBROW:** O PROBLEMA · **TÍTULO:** Nada disso foi testado junto.

Diagrama: notebook → switch → roteador → servidor em rack, ligados por linha vermelha, todos em
traço fino monocromático. Abaixo, quatro blocos curtos: `Fabricantes diferentes.` ·
`Sistemas operacionais diferentes.` · `Nenhum teste conjunto.` · `E funciona.`

Caixa destacada à direita: **Sem ordem, tentativa e erro. Com ordem, método.**

## Slide 02 — A norma

**EYEBROW:** A NORMA · **TÍTULO:** Open Systems Interconnection

Topo direito, dois selos em mono: `ISO/IEC 7498-1` e `ITU-T X.200`, com a legenda
`Texto idêntico, duas designações`.

Três blocos: `Referência, não implementação.` · `Divide responsabilidades e define fronteiras.` ·
`Não diz como construir.`

Comparação em duas colunas:

| A pilha de protocolos OSI *(riscada)* | O modelo OSI *(em destaque)* |
|---|---|
| Não venceu comercialmente. Substituída pelo TCP/IP. | Em vigor. A linguagem comum da área. |

## Slide 03 — Serviço não é protocolo

**EYEBROW:** CONCEITO-CHAVE · **TÍTULO:** Serviço não é protocolo.

Duas caixas de camada lado a lado, uma em cada extremo. Seta **vertical** subindo da caixa
esquerda: `Serviço. Vertical. Para a camada de cima.` Seta **horizontal tracejada** ligando as duas:
`Protocolo. Horizontal. Com o par do outro lado.`

Composição: preencher a largura de forma equilibrada e manter os rótulos **na horizontal**. O slide
anterior deixou um vazio grande à direita e rotacionou o rótulo "Serviço" na vertical, o que
prejudicou a leitura.

## Slide 04 — Entidades pares

**EYEBROW:** A ENGRENAGEM · **TÍTULO:** Entidades pares e aprimoramento passo a passo.

Duas pilhas, `Machine A` e `Machine B`. Seta vermelha horizontal ligando a camada 3 de uma à camada
3 da outra. Seta vertical subindo pela pilha A.

Rótulo à direita: `Entidades pares: mesma camada, máquinas diferentes. Camada 3 fala com camada 3.
Nunca camada 3 com camada 4.` — **conferir a palavra "Camada".**

Rótulo à esquerda, com chave abrangendo a pilha: `Serviço cumulativo: o serviço de uma camada é a
capacidade dela mais todas as de baixo.`

> Se a pilha for reduzida para caber, **rotular como recorte**. Uma pilha de sistema final
> apresentada como completa precisa ter sete caixas.

## Slide 05 — As sete camadas

**EYEBROW:** AS SETE CAMADAS

Tabela de sete linhas, de 7 no topo a 1 na base:

| 7 | **Aplicação** | Único acesso do processo à rede. |
| 6 | **Apresentação** | Representação comum da informação. |
| 5 | **Sessão** | Organiza e sincroniza o diálogo. |
| 4 | **Transporte** | Transferência transparente. |
| 3 | **Rede** | Independência de roteamento. |
| 2 | **Enlace de dados** | Vizinhos diretos e erros do meio. |
| 1 | **Física** | Bits no meio físico. |

> **Nenhum ícone ou nome de protocolo dentro das caixas.** Colar protocolo na figura ensina o
> modelo como implementação, que é o erro central que esta aula combate.

*Este slide estava correto no deck anterior. Manter.*

## Slide 06 — Camada 3 e relay · **CORREÇÃO C1**

**EYEBROW:** DEFINIÇÃO EXATA

Comparação binária:

| Errado | O que a norma diz |
|---|---|
| A camada do IP | Independência de roteamento e encaminhamento. |

**Subtítulo:** Passagem, não destino.

Diagrama de relay: `Machine A` — `Relay Router` — `Machine B`.

> **C1, obrigatório.** `Machine A` e `Machine B` têm **as sete camadas, numeradas 1 a 7, sem
> nenhuma lacuna, e idênticas entre si**. O `Relay Router` tem apenas as camadas **1, 2 e 3**.
>
> No deck anterior, a Machine A pulou a camada 5 e a Machine B pulou a camada 4. Isso contradiz o
> slide 05, que acabou de enumerar as sete, e desmonta o claim mais básico da aula.

Rótulo: `Em um sistema de relay, só as camadas de baixo participam do encaminhamento daquele
tráfego. O equipamento continua tendo camadas altas, para ser gerenciado.`

Se couber melhor, dividir em dois slides: a comparação da camada 3 em um, o relay em outro.

## Slide 07 — Três nomes

**EYEBROW:** PASSO 1 DE 3 · **TÍTULO:** Três nomes que você vai usar sempre.

Centro, grande, em vermelho: `SDU + PCI = PDU`

Três colunas: `PCI` → Informação de controle de protocolo. · `SDU` → Carga que a camada não
interpreta. · `PDU` → PCI + dados do usuário. Desce para virar a SDU da camada inferior.

*Correto no deck anterior. Manter.*

## Slide 08 — O cabeçalho não vai na frente

**EYEBROW:** ERRO COMUM · **TÍTULO:** O cabeçalho não vai necessariamente na frente.

Esquerda, esmaecido e riscado: `O que se ouve:` Cabeçalho na frente dos dados. Barra
`HEADER | DATA` com um X cinza.

Direita, em destaque: `O que a norma registra:` Nenhuma relação de posição definida. Barra
`DADOS | FCS`, com o FCS em vermelho **no fim**, e balão: `Exemplo Ethernet: FCS no fim do quadro.`

*Correto no deck anterior, e é o slide que melhor cumpre a intenção da aula. Manter.*

## Slide 09 — Evidência

**EYEBROW:** EVIDÊNCIA · **TÍTULO:** A mesma estrutura, em bytes.

Caixas aninhadas, de fora para dentro: `Enlace` ⊃ `Rede` ⊃ `Transporte` ⊃ `Carga não interpretada`,
esta última destacada em vermelho.

> **Proibido** exibir endereço, porta, byte ou tela de analisador. Não existe captura sanitizada no
> repositório (OQ-001) e nada pode ser inventado. Apenas a estrutura.

*Correto no deck anterior. Manter.*

## Slide 10 — Rigor de fonte

**EYEBROW:** RIGOR DE FONTE · **TÍTULO:** Esses nomes não são do OSI.

| Termo procurado no texto integral | Ocorrências |
|---|---|
| `packet` | **0** |
| `datagram` | **0** |
| `frame` | 8 (todas em "framework") |
| `segment` | só a operação de segmentar |

Destaque: `O único termo OSI: PDU.`
Faixa de procedência: `Quadro = IEEE 802 | Datagrama = RFC 791 | Segmento = RFC 9293`

*Correto no deck anterior. Manter.*

## Slide 11 — OSI × Internet · **CORREÇÃO C4**

**EYEBROW:** OSI × INTERNET · **TÍTULO:** Por que tanta gente desenha quatro.

Esquerda, `Modelo OSI`, sete caixas numeradas. Direita, `RFC 1122`, quatro caixas: `Aplicação`,
`Transporte`, `Internet`, `Enlace`.

> **C4, obrigatório.** A chave que liga ao bloco `Aplicação` do RFC 1122 abrange **apenas as
> camadas 6 e 7**. A camada **5 (Sessão) fica isolada: sem chave, sem linha tracejada, sem
> destino** — visualmente órfã.
>
> No deck anterior, 7, 6 e 5 estavam agrupadas numa única caixa ligada a "Aplicação", o que
> contradizia o próprio rótulo do slide. A fonte (RFC 1122) atribui à aplicação da Internet apenas
> apresentação e aplicação; sobre a sessão ela nada diz.

Ligações restantes: camada 4 → `Transporte`; camada 3 → `Internet`; camadas 2 e 1 → `Enlace`.

Callout vermelho: `Sessão: sem contraparte. "É camada 6" não tem apoio no documento.`

## Slide 12 — Nem tudo tem número · **CORREÇÃO C2**

**EYEBROW:** NEM TUDO TEM NÚMERO

Duas colunas.

**Camada 2** — `Duas sub-camadas.` · `Sub-camada é um conceito previsto e definido no próprio OSI.`

> **C2, obrigatório.** Empilhar, de cima para baixo: `LLC (Logical Link Control)`, linha divisória,
> `MAC (Medium Access Control)`. **LLC em cima.**
>
> O deck anterior desenhou MAC acima de LLC. IEEE Std 802: *"the LLC sublayer operating over a MAC
> sublayer"*, e o MAC existe *"between the Physical layer and the LLC sublayer"*. A ordem é a única
> informação que este diagrama transmite; invertida, ele ensina o oposto.

**TLS** — `Não se declara 5, 6 nem 7.` · `A especificação exige apenas um fluxo confiável e em ordem
da camada inferior.` · `Cravar um número é inventar.`

Diagrama: `TLS` em caixa tracejada, acima de `Transporte (ex.: TCP)`. **Sem número de camada em
nenhum dos dois.**

## Slide 13 — Diagnóstico, parte 1 · **CORREÇÃO C5**

**EYEBROW:** MÉTODO DA ESCOLA — NÃO É NORMA · **TÍTULO:** Diagnóstico: de baixo para cima.

Escada ascendente com **os degraus 1, 2 e 3**:

- `1: Existe enlace?` (Estado da porta, erros, potência óptica)
- `2: Os vizinhos se veem?` (Tabela de endereços, resolução, VLAN da porta)
- `3: Existe caminho?` (Endereço, máscara, gateway, rotas)

Caixa vermelha: **ERRO MAIS COMUM** — `Ida e volta. Falha de retorno se parece exatamente com falha
de ida. Sempre teste as duas direções.`

> O eyebrow "MÉTODO DA ESCOLA — NÃO É NORMA" é **obrigatório**. Este conteúdo é editorial
> (CLM-021), não prescrição de norma, e não pode ter a mesma autoridade visual dos slides que citam
> a fonte.

## Slide 14 — Diagnóstico, parte 2 · **CORREÇÃO C5**

**EYEBROW:** MÉTODO DA ESCOLA — NÃO É NORMA

Continuação da escada, **apenas os degraus 4 e 5–7**:

- `4: A porta aceita conexão?` (Sessão, retransmissão)
- `5–7: O serviço responde certo?` (Nome, certificado, código de resposta, log)

> **C5, obrigatório.** Não repetir o degrau 2 e não omitir o 3 — o deck anterior fez as duas coisas,
> e perdeu justamente a camada 3, onde está o erro que o slide 13 destaca. A numeração é crescente e
> continua de onde o slide 13 parou.
>
> **Nenhuma faixa de texto pode cobrir um degrau.** No deck anterior a faixa inferior cobriu o
> primeiro degrau. Se a frase de fechamento não couber, ela vai para um slide próprio.

Fechamento: `O valor do método não é acertar a camada na primeira tentativa. É impedir que você
investigue a aplicação quando o problema é um cabo.`

## Slide 15 — Resumo e exercício · **CORREÇÃO C3**

**EYEBROW:** RESUMO — grade de seis cartões numerados.

| Nº | Título | Frase |
|---|---|---|
| 01 | Referência | Descreve responsabilidade, não implementação. |
| 02 | Serviço e protocolo | Um para cima, outro para o lado. |
| 03 | Encapsulamento | Controle acrescentado a uma carga não interpretada. |
| 04 | Procedência | Quadro, datagrama e segmento não são do OSI. |
| 05 | Internet real | Quatro camadas; aplicação **combina 6 e 7**. Sessão sem contraparte. |
| 06 | Método | De baixo para cima. |

> **C3, obrigatório.** O cartão 05 dizia "aplicação cobre 5, 6 e 7". É o erro que a revisão técnica
> classificou como HIGH (TR1-001) e que já foi corrigido na narração. Se voltar, o aluno lê no slide
> o oposto do que ouve.

Faixa inferior vermelha: **SEU EXERCÍCIO** — `Sete responsabilidades, uma coisa que você usa.`
`Escolha algo que você usa na rede. Escreva qual responsabilidade de cada uma das 7 camadas está
sendo exercida. Onde não conseguir preencher, você encontrou o seu próximo assunto de estudo.`

---

## Checklist de conferência antes de reingerir

- [ ] 15 slides, 1920×1080 ou superior
- [ ] Sem marca d'água de terceiro
- [ ] **C1** slide 06: sete camadas nas duas pontas, sem lacuna; relay com 1–3
- [ ] **C2** slide 12: LLC acima de MAC
- [ ] **C3** slide 15: cartão 05 sem "cobre 5, 6 e 7"
- [ ] **C4** slide 11: camada 5 isolada, sem chave
- [ ] **C5** slides 13/14: degraus 1-2-3 e 4-5–7, sem repetir nem omitir, sem faixa cobrindo degrau
- [ ] Slide 04: "Camada", não "Camad"
- [ ] Slides 13 e 14 com o eyebrow "MÉTODO DA ESCOLA — NÃO É NORMA"
- [ ] Slide 05 sem ícone de protocolo nas caixas
- [ ] Slide 09 sem valor concreto de captura
- [ ] Mono só em string técnica

## Como reingerir

```bash
npm run slides:ingest-images -- courses/02-fundamentos-de-redes/lessons/fundamentos-01-modelo-osi --pptx <novo-deck.pptx>
```

Se o novo material vier como PNGs soltos em vez de PPTX, avise — o ingestor atual espera um `.pptx`
com uma imagem full-bleed por slide.
