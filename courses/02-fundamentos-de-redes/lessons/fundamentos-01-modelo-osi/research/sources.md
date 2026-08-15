# Fontes — fundamentos-01-modelo-osi

Política aplicada: `brain/source-policy.md`. Data de acesso de todas as fontes: **2026-07-29**.
Todas as fontes abaixo foram lidas em texto integral pelo pesquisador, não por resumo de terceiros.

## Nível A — padrões e especificações oficiais

### A1 — ITU-T Rec. X.200 (07/94) | ISO/IEC 7498-1:1994
- Título: *Information technology — Open Systems Interconnection — Basic Reference Model: The basic model*
- Organização: ITU-T (Setor de Padronização de Telecomunicações da UIT), em colaboração com ISO/IEC
- Versão/data: X.200 aprovada em 1 de julho de 1994; ISO/IEC 7498-1 segunda edição, 1994-11-15
- Status: em vigor
- URL primária (PDF livre): https://www.itu.int/rec/T-REC-X.200-199407-I
- Espelho oficial usado para extração de texto: https://www.ecma-international.org/wp-content/uploads/s020269e.pdf (ECMA International, mesma numeração `s020269` do ITTF/ISO)
- Extensão verificada: 63 páginas, ~194.000 caracteres extraídos e pesquisados integralmente
- **Equivalência confirmada verbatim** (Foreword): "The text of ITU-T Recommendation X.200 was approved on 1st of July 1994. The identical text is also published as ISO/IEC International Standard 7498-1."
- Sustenta: CLM-001 a CLM-012

> Nota de licença: o texto do padrão é citado nesta aula em trechos curtos, para fins de ensino e
> com atribuição. Nenhum trecho do PDF é redistribuído no repositório.

### A2 — RFC 1122
- Título: *Requirements for Internet Hosts — Communication Layers*
- Organização: IETF / Internet Engineering Task Force; editor R. Braden
- Data: outubro de 1989. Status: Internet Standard (STD 3)
- URL: https://www.rfc-editor.org/rfc/rfc1122.txt
- Sustenta: CLM-013, CLM-014, CLM-015, CLM-016

### A3 — IEEE Std 802-2001
- Título: *IEEE Standard for Local and Metropolitan Area Networks: Overview and Architecture*
- Organização: IEEE
- Data: aprovado 2001, copyright 2002
- URL: https://www.ieee802.org/secmail/pdfocSP2xXA6d.pdf (hospedado no domínio oficial do IEEE 802)
- Sustenta: CLM-017 (termo "frame"), CLM-018
- **Dependência de versão declarada:** existe revisão posterior (IEEE Std 802-2014). Os dois claims
  usados aqui — a família 802 cobre as duas camadas mais baixas do OSI, e a camada de enlace é
  estruturada como LLC sobre MAC — são estruturais e estáveis entre as revisões. Ver OQ-002.

### A4 — RFC 9293
- Título: *Transmission Control Protocol (TCP)*
- Organização: IETF. Data: agosto de 2022. Status: Internet Standard
- Obsoleta: RFC 793, 879, 2873, 6093, 6429, 6528, 6691
- URL: https://www.rfc-editor.org/rfc/rfc9293.html
- Sustenta: CLM-017 (termo "segment")

### A5 — RFC 791
- Título: *Internet Protocol — DARPA Internet Program Protocol Specification*
- Organização: IETF / USC Information Sciences Institute. Data: setembro de 1981. Status: Internet Standard
- URL: https://www.rfc-editor.org/rfc/rfc791.txt
- Sustenta: CLM-017 (termo "datagram")

### A6 — RFC 8446
- Título: *The Transport Layer Security (TLS) Protocol Version 1.3*
- Organização: IETF; autor E. Rescorla (Mozilla). Data: agosto de 2018. Status: Proposed Standard
- URL: https://www.rfc-editor.org/rfc/rfc8446.txt
- Sustenta: CLM-020

### A7 — RFC 3439
- Título: *Some Internet Architectural Guidelines and Philosophy*
- Organização: IETF; autores R. Bush, D. Meyer. Data: dezembro de 2002
- **Status: Informational** — não é Standards Track. Usada como posição arquitetural documentada da
  comunidade IETF, não como norma.
- URL: https://www.rfc-editor.org/rfc/rfc3439.txt
- Sustenta: CLM-019

## Nível B / C / D

Nenhuma fonte de nível B, C ou D foi necessária para sustentar claims desta aula. Todo o conteúdo
técnico do roteiro se apoia em A1–A7.

## Fontes deliberadamente NÃO usadas

- Páginas de fabricantes e blogs explicando "as 7 camadas do OSI": Nível D. Circulam com o erro
  recorrente de apresentar `frame/packet/segment` como terminologia do OSI (ver CLM-009) e de
  tratar o OSI como implementação. Não usadas nem para descoberta.
- Resultados de busca resumidos por mecanismo de busca: não usados como fonte. Toda citação
  desta aula vem do texto integral baixado.
