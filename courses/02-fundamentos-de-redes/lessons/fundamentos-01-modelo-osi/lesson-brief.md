# Lesson Brief

- Lesson ID: fundamentos-01-modelo-osi
- Tema: Modelo OSI — o modelo de referência de sete camadas e como usá-lo para diagnosticar
- Curso: 02-fundamentos-de-redes / Módulo 1 / Aula 01
- Público: Profissionais iniciantes de infraestrutura, incluindo quem vem de suporte/helpdesk e ainda não tem base formal de redes. Não se assume conhecimento prévio de protocolos.
- Pré-requisitos: Saber o que é um computador em rede, um cabo e um endereço IP em nível de usuário. Curso 01 (Preparação do Laboratório) é recomendado mas não exigido — a captura desta aula é apresentada, não executada pelo aluno.
- Objetivo de aprendizagem: Ao final, o aluno deve conseguir (1) nomear as sete camadas do modelo OSI e a função de cada uma; (2) explicar encapsulamento e desencapsulamento usando os termos corretos de PDU, SDU e PCI; (3) apontar onde a pilha TCP/IP real **não** corresponde às sete camadas, e dizer a procedência correta dos nomes quadro, datagrama e segmento; e (4) conduzir um diagnóstico camada a camada, dizendo qual pergunta fazer e qual evidência coletar em cada nível.
- Duração alvo: 14 minutos (faixa aceitável 12–16 min por decisão do responsável em 2026-07-29;
  ~2.000–2.300 palavras de narração)
- Escopo incluído:
  - O que é um modelo de referência e por que ele existe (interoperabilidade multi-fabricante)
  - Conceitos estruturais do OSI: camada, serviço, protocolo, entidade par, SDU/PDU
  - As sete camadas: a função de cada uma, na letra da norma
  - A procedência dos nomes de PDU: quadro, datagrama e segmento, e a norma que define cada um
  - Encapsulamento e desencapsulamento passo a passo
  - Evidência real: um pacote capturado, mostrando que os cabeçalhos das camadas existem de fato
  - Divergência honesta: OSI (ISO/IEC 7498-1 / ITU-T X.200) vs. modelo da Internet (RFC 1122)
  - Armadilhas de modelo mental: camada 2 tem sub-camadas (IEEE 802), TLS não cai em uma camada limpa
  - Diagnóstico camada a camada: a pergunta e a evidência de cada nível
- Fora de escopo:
  - **Nome de PDU para as camadas 5, 6 e 7** — não existe termo primário consagrado (OQ-004). A aula diz ao aluno que aqui a terminologia é frouxa, em vez de inventar uma tabela completa.
  - **VPN e tunelamento como tópico** — citados em uma oração em SEG-024, apenas para não prometer que a dissecação é sempre linear. Desenvolvimento fica para curso posterior.
  - **"Camada 8"** — excluído deliberadamente. Ver a tabela de claims rejeitados em `research/evidence-ledger.md`: a piada compete com o modelo que o aluno está formando na primeira aula.
  - Detalhe de formato de cabeçalho de qualquer protocolo específico (fica em Frames, IPv4, IPv6)
  - Ethernet, ARP, switching e MAC learning (aulas 03–05)
  - Configuração em CLI de qualquer fabricante
  - Modelo TCP/IP em profundidade (aula 02 dedicada)
  - Camadas OSI aplicadas a Wi-Fi/RF (curso 05)

## Progressão didática (problema -> modelo -> mecânica -> evidência -> erro -> diagnóstico -> resumo)

1. **Problema concreto.** Um notebook, um switch Aruba, um roteador Juniper e um servidor Linux nunca foram testados juntos — e funcionam. Por quê? E o outro lado do mesmo problema: quando *não* funciona, por onde começar?
2. **Modelo mental.** Camadas como divisão de responsabilidade e contrato: cada camada usa o serviço da de baixo e entrega serviço para a de cima. Serviço ≠ protocolo.
3. **As sete camadas.** Subida da 1 à 7, cada uma com função, PDU e exemplo.
4. **Mecânica: encapsulamento.** O dado descendo a pilha ganhando cabeçalhos; subindo, perdendo.
5. **Evidência.** A captura: os cabeçalhos que acabamos de descrever, visíveis em um pacote real.
6. **Erro comum.** OSI é referência, não implementação. O que a Internet realmente faz (RFC 1122) e onde o mapeamento 1:1 falha.
7. **Diagnóstico.** Camada a camada: pergunta, evidência, ferramenta.
8. **Recapitulação + exercício.**

## Especialistas acionados

- `official-docs-researcher` — obrigatório. Fonte primária de OSI (ITU-T X.200 / ISO/IEC 7498-1) e do modelo da Internet (RFC 1122).
- `packet-analysis-specialist` — a evidência de captura e a leitura correta da dissecação por camadas.
- `lab-and-evidence-engineer` — definição do artefato de captura sanitizado, se a captura for produzida internamente.

Não se aplicam nesta aula: `aruba-specialist`, `juniper-specialist`, `wifi-rf-specialist`, `datacenter-specialist` — tema vendor-neutro e anterior a qualquer fabricante.

## Decisões editoriais tomadas com o responsável (2026-07-29)

- Duração alvo 14 min, com seção de diagnóstico por camada incluída.
- Profundidade: conceitual + diagnóstico, com a divergência OSI vs TCP/IP explicitada — não ensinar OSI como se fosse implementação.
- Evidência: diagramas como veículo principal + uma captura real como prova de existência dos cabeçalhos.

## Risco aberto

A captura real ainda não existe no repositório. Ver `research/open-questions.md` (OQ-001). A aula **não** deve inventar bytes, IPs, MACs ou telas de Wireshark.
