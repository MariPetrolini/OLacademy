# Roteiro falado — Modelo OSI

- Lesson ID: `fundamentos-01-modelo-osi`
- Passagem: **1 (antes do PowerPoint)**
- Meta de ritmo: 125–145 palavras por minuto (`skills/write-spoken-lesson.md`)
- Sem dêixis visual: o texto se sustenta sem imagem, conforme pipeline script-first
- IDs de claim aparecem apenas em comentários Markdown, nunca na fala

---

## Bloco 0 — Abertura obrigatória

<!-- texto canônico de brain/opening-signature.md; só a variável do assunto muda -->

**SEG-000**
Olá, eu sou André Brazioli, diretor de pós-vendas na O L Tecnologia e especialista em redes. Hoje falaremos sobre o modelo O S I. Vamos começar?

---

## Bloco 1 — Abertura pelo problema

**SEG-001**
Existe uma coisa que acontece todos os dias e que, se você parar para pensar, deveria ser impossível. Um notebook qualquer se conecta a um switch de um fabricante, que entrega o tráfego para um roteador de outro, que atravessa a rede de uma operadora e chega em um servidor com outro sistema operacional. Nada disso foi testado junto. E funciona.

**SEG-002**
Funciona porque, décadas atrás, um grupo de pessoas dividiu o problema. A solução não foi um protocolo: foi um jeito de dividir, e é esse jeito que a gente vai estudar. E tem um motivo mais imediato. Quando a rede não funciona, você precisa de uma ordem para investigar. Sem ordem, é tentativa e erro. Com ordem, é método.

---

## Bloco 2 — O que é um modelo de referência

<!-- CLM-001, CLM-002 -->

**SEG-004**
O nome completo é Modelo de Referência Básico para Interconexão de Sistemas Abertos. Em inglês, Open Systems Interconnection, que dá a sigla O S I. É uma norma internacional, publicada em texto idêntico pela I S O e pela União Internacional de Telecomunicações, e continua em vigor.

**SEG-005**
Guarde a palavra referência. Um modelo de referência não diz como construir nada. Ele divide responsabilidades e define fronteiras, para que times diferentes, em países diferentes, trabalhem de forma independente e o resultado ainda encaixe.

**SEG-006**
Isso desarma uma confusão comum. Existiu também uma família de protocolos O S I, feita para implementar o modelo, e ela não venceu comercialmente: quem venceu foi o TCP/IP. Mas o modelo continua sendo a linguagem comum da área. Quem diz que esse modelo morreu está falando dos protocolos.

---

## Bloco 3 — A engrenagem: serviço, protocolo, entidades pares

<!-- CLM-003, CLM-004, CLM-011 -->

**SEG-007**
O modelo tem sete camadas, mas antes de nomeá-las vale entender a engrenagem. Cada camada faz duas coisas, e a norma trata as duas separadamente. A primeira é oferecer um serviço para a camada de cima. A segunda é conversar com a camada de mesmo nível do outro lado, seguindo um protocolo. Serviço é o que você entrega para cima. Protocolo é como você combina com o seu par.

**SEG-009**
Essa separação é o que dá liberdade de engenharia. Se o serviço entregue para cima continua o mesmo, você troca o protocolo debaixo dele sem quebrar nada acima. É o que acontece quando você sai do cabo e entra no Wi-Fi. O navegador não muda uma linha.

**SEG-008**
A norma chama de entidades pares as que estão na mesma camada, em máquinas diferentes. A camada de rede do seu notebook conversa com a camada de rede do servidor. Não existe conversa direta entre a camada de rede de um lado e a de transporte do outro.

**SEG-010**
E um detalhe que muita explicação perde: o serviço de uma camada não é só o trabalho dela. A norma define o serviço como a capacidade daquela camada mais todas as de baixo. Cada camada entrega para cima um serviço melhor do que recebeu. A pilha é um aprimoramento passo a passo.

---

## Bloco 4 — As sete camadas

<!-- CLM-010, CLM-012 -->

**SEG-011**
Com isso, as sete camadas. Vou de baixo para cima, porque é assim que o serviço cresce e é assim que você vai diagnosticar.

**SEG-012**
Camada um, física. Meios mecânicos, elétricos, funcionais e procedurais para ativar, manter e desativar conexões físicas, com um objetivo só: transmitir bits. Tensão, luz, conector, pinagem. Nada de endereço, nada de decisão.

**SEG-013**
Camada dois, enlace de dados. Ela organiza a conversa entre vizinhos diretos, os que compartilham o mesmo meio. Estabelece e libera conexões de enlace e, na letra da norma, detecta e possivelmente corrige os erros da camada física. Repare no possivelmente: corrigir é opcional.

**SEG-014**
Camada três, rede. A norma a define como a camada que dá às camadas de cima independência de roteamento e de encaminhamento. É a camada que faz você não precisar saber por onde o dado passou.

**SEG-015**
Camada quatro, transporte. A palavra-chave da norma é transparente: o transporte libera as camadas de cima da preocupação com o modo pelo qual a transferência foi conseguida. E cuidado com um atalho aqui: transporte não é sinônimo de T C P. Quando o protocolo oferece confiabilidade, como o T C P, ele usa retransmissão, ordenação e controle de fluxo, e a aplicação não vê nada disso. Mas nem todo transporte oferece essas garantias.

**SEG-016**
Camada cinco, sessão: organizar e sincronizar o diálogo entre as duas pontas. Camada seis, apresentação: a representação da informação. Dois sistemas podem guardar o mesmo texto de formas diferentes, e ela garante uma representação comum.

**SEG-017**
Camada sete, aplicação. É o único meio de acesso do processo de aplicação ao ambiente de rede. E não é o programa inteiro: é a parte dele que fala rede.

**SEG-018A**
<!-- Fase 5: correcao da camada 3 movida para ca, para casar com a comparacao "Errado /
     O que a norma diz" do slide 006. Enumerar as sete primeiro e so depois voltar na
     mais mal contada ensina melhor do que interromper a contagem. CLM-010. -->
Com as sete na mesa, vale voltar na camada três, porque é a que mais gente conta errado. Você vai ouvir que ela é a camada do I P. Não é: o I P é uma implementação daquela responsabilidade, não a definição dela.

**SEG-018**
E uma consequência antes de seguir. A norma diz que, quando o meio físico não liga todos os sistemas diretamente, alguns atuam apenas repassando dados, e que as funções desse repasse ficam nas camadas de baixo. É a explicação formal de por que um switch ou um roteador não precisa subir a pilha inteira para encaminhar aquele tráfego. Para o tráfego que ele repassa, ele é passagem, não destino. Isso não quer dizer que o equipamento não tenha camadas altas: ele tem, para ser gerenciado e configurado.

---

## Bloco 5 — Encapsulamento

<!-- CLM-005, CLM-006, CLM-007, CLM-008 -->

**SEG-019**
Agora a mecânica. Como é que um dado atravessa sete camadas sem se perder? A norma nomeia três coisas. A primeira é a informação de controle de protocolo: o que as entidades pares trocam para coordenar o trabalho. Em linguagem de campo, o cabeçalho. A segunda é a unidade de dados de serviço, S D U: a carga que a camada transporta e que, pela definição da norma, ela não interpreta. A terceira é a unidade de dados de protocolo, P D U: controle mais, possivelmente, os dados do usuário.

**SEG-020**
Encapsular é isso, e a norma descreve em uma frase: dentro de uma camada, a informação de controle é acrescentada à unidade de dados de serviço para formar a unidade de dados de protocolo. Depois essa P D U desce e passa a ser a carga da camada de baixo, que repete o processo. Na subida, cada camada remove a sua parte.

**SEG-021**
Repare no que a definição de S D U garante: quem transporta não interpreta a carga. É por isso que um switch não precisa entender nada de web para entregar uma página.

**SEG-022**
E um detalhe em que quase todo material erra. É comum ouvir que cada camada coloca um cabeçalho na frente dos dados. A norma explicitamente não diz isso: ela registra que não existe relação de posição definida entre a informação de controle e os dados dentro da unidade de protocolo. E não é preciosismo. O Ethernet coloca a sequência de verificação de erro no fim do quadro, depois dos dados. O correto é dizer que cada camada acrescenta a sua informação de controle.

**SEG-023**
Também não é sempre um para um. A norma prevê que uma unidade de serviço seja mapeada em mais de uma unidade de protocolo, e isso é a segmentação. É o mecanismo que reaparece em fragmentação e em tamanho máximo de segmento.

---

## Bloco 6 — Evidência

<!-- CLM-017. OQ-001: referencial, sem citar nenhum valor concreto.
     Nenhum byte, endereco, porta ou tela inventados. -->

**SEG-024**
E nada disso é abstração. Em uma captura simples, o analisador de pacotes organiza a dissecação pelos encapsulamentos, e você reconhece a informação de enlace, depois a de rede, depois a de transporte, e por último os dados da aplicação. Os cabeçalhos estão ali, em bytes. Em tráfego com túnel a árvore fica mais funda do que isso, mas o princípio é o mesmo.

---

## Bloco 7 — De onde vêm os nomes das unidades de dados

<!-- CLM-009, CLM-017. Nucleo diferenciador da aula. Nao encolher. -->

**SEG-025**
Agora um assunto de rigor que vai te poupar constrangimento. Você já viu, ou vai ver, uma tabela dizendo que a camada dois usa quadro, a três usa pacote e a quatro usa segmento, apresentada como terminologia do O S I.

**SEG-026**
Não é. Eu procurei no texto integral da norma. As palavras pacote e datagrama não aparecem nenhuma vez. A palavra frame, quadro em inglês, aparece oito vezes, e todas as oito estão dentro da palavra framework, que quer dizer arcabouço. E segmento aparece só como nome da operação de segmentar, nunca como nome da unidade de dados da camada quatro. O termo do O S I é um só: P D U.

**SEG-027**
Isso não quer dizer que os nomes populares sejam errados. Eles são corretos, cada um dentro do escopo da norma que o define. Quadro vem dos padrões I E E E 802, os padrões de rede local. Datagrama vem da especificação do protocolo I P. Segmento vem da especificação do T C P. O erro não é usar os nomes: é dizer que eles vêm do O S I.

---

## Bloco 8 — O modelo real da Internet

<!-- CLM-013, CLM-014, CLM-015, CLM-016, CLM-019 -->

**SEG-028**
O que leva à pergunta que todo aluno faz: se o modelo tem sete camadas, por que tanta gente desenha quatro? Porque a arquitetura da Internet é definida em outro documento, um padrão da I E T F conhecido como R F C 1122, e ele define quatro camadas: aplicação, transporte, internet e enlace. Repare: camada internet, não camada de rede.

**SEG-029**
E o mapeamento não é um para um. O próprio R F C 1122 diz onde quebra: a camada de aplicação da Internet combina, essencialmente, as funções das duas camadas mais altas do O S I, apresentação e aplicação. E diz que a suíte da Internet não subdivide a camada de aplicação.

**SEG-030**
E repare no que o documento não diz. Ele junta apresentação e aplicação, e para a sessão não dá mapeamento explícito: na lista de quatro, sessão não aparece como camada separada. Isso não quer dizer que nada cuide de sessão na prática. Quer dizer que a arquitetura da Internet não reserva uma camada para ela. Então afirmar que um protocolo é camada seis não tem apoio no documento. E desenhar sete caixas alinhadas com quatro ensina uma correspondência que não existe.

**SEG-031**
E o próprio R F C 1122 é honesto sobre o limite do recurso: ele afirma que camadas estritas são um modelo imperfeito, e que protocolos de camadas diferentes interagem de formas complexas e sutis. Bússola, não lei da física.

---

## Bloco 9 — Casos que não caem em uma camada limpa

<!-- CLM-018, CLM-020, CLM-003. Bloco comprimido a um segmento na
     adequacao de duracao. Ambos os claims preservados. -->

**SEG-032**
Dois casos rápidos, para você não esperar que tudo tenha um número. Nos padrões de rede local, a camada dois é dividida em duas sub-camadas, e isso não viola o modelo, porque o próprio O S I define sub-camada como subdivisão de uma camada. E o T L S, que coloca o S no HTTPS, não se declara camada cinco, seis nem sete: a especificação diz que o único requisito da camada de baixo é um fluxo confiável e em ordem. Descrever a posição funcional é correto. Cravar um número é inventar.

---

## Bloco 10 — Diagnóstico camada a camada

<!-- CLM-021: EDITORIAL. Marcacao linguistica obrigatoria em SEG-033.
     Nenhuma norma prescreve esta ordem. -->

**SEG-033**
E agora o motivo pelo qual isso paga o seu salário: diagnóstico. Mas eu preciso ser explícito antes de começar: o que vem agora não está na norma. Nenhuma norma manda diagnosticar em ordem nenhuma. Isto é método de campo, a forma que esta escola ensina. A lógica sai do modelo: se cada camada depende do serviço da de baixo, verificar de baixo para cima elimina as causas na ordem em que elas se sustentam.

**SEG-034**
Camada um: o enlace existe eletricamente? Camada dois: os vizinhos diretos se veem? Camada três: existe caminho?

**SEG-035**
E na camada três está o erro mais comum na carreira de todo mundo. Existe caminho de ida e de volta. Falha de retorno se parece exatamente com falha de ida, e você passa a tarde investigando o lado errado. Sempre nas duas direções.

**SEG-036**
Camada quatro: a porta do serviço aceita conexão? Da cinco à sete: o serviço responde certo? Nome resolvido, certificado válido, código de resposta.

**SEG-037**
E o valor do método não é acertar a camada na primeira tentativa. É impedir que você investigue a aplicação quando o problema é um cabo.

---

## Bloco 11 — Recapitulação e exercício

**SEG-038**
Recapitulando. O modelo O S I está em vigor, tem sete camadas, e descreve responsabilidade, não implementação. Cada camada oferece um serviço para cima e fala um protocolo com o seu par do outro lado. Encapsular é acrescentar informação de controle a uma carga que a camada não interpreta.

**SEG-039**
Quadro, datagrama e segmento são nomes reais, mas vêm do I E E E, do I P e do T C P, não do O S I. A Internet real tem quatro camadas, e a camada de aplicação dela combina apresentação e aplicação do O S I. E o modelo é a sua ordem de investigação: de baixo para cima.

**SEG-040**
Seu exercício, e ele é observável: escolha uma coisa que você usa na rede hoje e escreva, com as suas palavras, qual responsabilidade de cada uma das sete camadas está sendo exercida para aquilo funcionar. Onde não conseguir preencher, você encontrou o seu próximo assunto de estudo.

---

## Notas de produção

- **Siglas escritas espaçadas** (`O S I`, `P D U`, `S D U`, `T C P`, `I P`, `T L S`, `I E E E`, `R F C`,
  `I E T F`, `I S O`) para o TTS soletrar em vez de tentar ler como palavra. Verificar no clone e
  registrar o resultado em `brain/pronunciation-dictionary.md`.
- **`Wi-Fi`** já está no dicionário de pronúncia como *uai-fai*.
- **`framework`** em SEG-026 precisa sair em inglês. Se o clone pronunciar mal, regenerar apenas
  esse segmento.
- **SEG-026** é o segmento de maior valor técnico da aula e o mais frágil na leitura. Prioridade na
  conferência de áudio.
- **Nenhuma URL nem citação bibliográfica falada.** `R F C 1122` é dito porque o aluno precisa
  conseguir buscar o documento.
- **Nenhum valor concreto de captura** (byte, endereço, porta) aparece na fala — OQ-001.
- **Duração:** ver `voice/segments.json`. A estimativa é modelo, não medição; a duração real só
  existe depois da Fase 7, e é ela que alimenta o storyboard.
