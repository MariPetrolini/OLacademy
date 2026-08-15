# Créditos e licença — fundamentos-01-modelo-osi

Aberto em 2026-07-29 em resposta ao achado TR2-003 da revisão técnica #2.
`brain/source-policy.md` exige confirmação de autoria e licença antes da publicação.

## Slides do vídeo — material próprio da escola

Os 15 slides que aparecem no vídeo foram **gerados por esta pipeline**, não obtidos de terceiro:

- Conteúdo textual: `script/on-screen-text.md`, escrito nesta produção a partir de
  `research/evidence-ledger.md`
- Composição: `source/slide-build/gen_slides.py`, escrito nesta produção
- Identidade visual: tokens de `brain/branding.md` (branco e `#771215`)
- Tipografia: famílias de sistema (Helvetica/Arial para leitura, Menlo para string técnica).
  **Nenhum arquivo de fonte foi incorporado**, conforme a exigência de `brain/branding.md` de só
  embutir fonte com licença registrada.
- Rasterização: Chrome headless, via `automation/slides/render-html-slides.mjs`

Não há logo de fabricante, captura de terceiro, nem imagem de banco. Nenhum ativo externo foi
incorporado.

## Deck original ingerido — PENDENTE DE CONFIRMAÇÃO DO RESPONSÁVEL

`source/original/deck.pptx` (`OSI_Architecture.pptx`) foi fornecido pelo responsável em 2026-07-29 e
**foi substituído**: nenhum pixel dele aparece no vídeo. Os PNGs derivados estão preservados apenas
para auditoria, em `source/superseded-notebooklm/`.

O que é verificável a partir do arquivo:

- Os 15 slides eram imagens full-bleed sem texto editável.
- O conteúdo reproduzia `script/on-screen-text.md`, ou seja, deriva de material desta produção.
- Cada slide trazia a marca `NotebookLM` no canto inferior direito, indicando geração pela
  ferramenta homônima do Google.

**O que precisa da sua confirmação, por escrito, antes do release:**

1. O deck foi gerado por você, a partir do texto desta aula? (é o que a evidência sugere)
2. A licença de uso da ferramenta permite uso comercial do material gerado?
3. Existe algum terceiro a creditar?

Enquanto isso não estiver respondido, este arquivo registra a pendência. **Não afirmei autoria em
seu nome** — a declaração é sua.

Se a resposta a (1) for sim e a (2) for sim, o risco é nulo na prática, já que o deck foi
substituído por reconstrução própria e não integra a entrega.

## Fontes técnicas citadas

Trechos curtos de norma são citados com atribuição, para fins de ensino. Nenhum documento é
redistribuído no repositório. Ver `research/sources.md` para a lista completa com data de acesso.

| Fonte | Organização | Uso nesta aula |
|---|---|---|
| ITU-T X.200 (07/94) / ISO/IEC 7498-1:1994 | ITU-T, ISO/IEC | Citações curtas de definição |
| RFC 1122 | IETF | Citações curtas |
| IEEE Std 802-2001 | IEEE | Citações curtas |
| RFC 791, RFC 9293, RFC 8446, RFC 3439 | IETF | Referência de terminologia |

## Sanitização

Não se aplica captura de laboratório: nenhuma existe nesta aula (OQ-001). Nenhum IP, MAC, serial,
credencial ou nome real aparece em slide ou narração — verificado no roteiro e nos 15 PNGs.
