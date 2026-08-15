# Política de fontes

## O deck de imagens é apoio, não evidência

A aula não começa por um PDF. Ela começa por pesquisa e evidência: o roteiro é escrito a partir
de fonte primária, revisado pelo Codex e aprovado pela pessoa responsável antes de existir
qualquer imagem. O deck é produzido depois, fora do repositório, e ingerido em `source/` em G6
para servir ao roteiro já aprovado.

Consequência prática: **nenhuma afirmação técnica se sustenta só porque está no slide.** Cada
claim exige fonte Nível A ou B no `evidence-ledger.md`, registrada em G2, antes de o deck
existir. Onde a imagem divergir da fonte oficial, prevalece a fonte oficial e a narração
corrige o slide. A página é registrada como o lugar onde o claim aparece, nunca como sua fonte.

Antes de ingerir, confirmar com o responsável:

- **Autoria e licença.** Material próprio da escola, material de terceiro com permissão
  escrita de uso, ou material sob licença que permita derivação. Deck de terceiro sem direito
  de uso não entra no repositório — nem como referência.
- **Créditos.** Quando o deck não é próprio, a autoria vai para `release/credits.md`.
- **Sanitização.** Nenhum IP público, MAC real, serial, credencial ou nome real pode entrar
  no material (`skills/sanitize-lab-artifacts.md`). Exigir reexportação em vez de editar o
  PDF ingerido, que é imutável.
- **Sem senha.** PDF protegido não é ingerível e não deve ser desprotegido para contornar o
  gate.

## Nível A
RFCs, padrões oficiais, documentação oficial do fabricante e notas de versão.

## Nível B
White papers oficiais, guias de desenho validados e documentação acadêmica primária.

## Nível C
Livros e cursos reconhecidos, usados para apoio didático, não para substituir o padrão.

## Nível D
Blogs, fóruns e vídeos: apenas descoberta ou evidência de comportamento não documentado, sempre marcados.

Cada fonte deve registrar data de acesso, versão e quais claims suporta.
