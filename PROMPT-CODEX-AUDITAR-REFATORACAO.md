# Prompt para o Codex auditar esta V4

Analise profundamente este repositório como revisor de arquitetura. Leia `CLAUDE.md`, `AGENTS.md`, `CODEX.md`, `docs/*`, `agents/*`, `skills/*`, `automation/*` e `remotion/*`.

Objetivo do produto: fábrica de cursos em que Claude Code pesquisa e produz; especialistas de redes e research existentes permanecem intactos; Codex revisa fatos/fontes; há apenas duas pausas humanas por mensagem `continue`; PPTX é ingerido depois da primeira pausa e cada slide é obrigatório como imagem do vídeo; roteiro é readaptado e revisado; ElevenLabs gera a voz clonada; Remotion compõe slides + animações + áudio e entrega MP4.

Procure inconsistências, referências residuais a hashes/gates/PDF-first, bugs de automação, risco de segredo, caminhos quebrados, schema incompatível e qualquer ponto que possa permitir avançar sem revisão. Não altere os agentes especialistas preservados. Faça correções diretamente apenas em arquivos de orquestração/automação e documente tudo em `reports/codex-refactor-audit.md`.
