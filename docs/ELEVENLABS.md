# ElevenLabs

A fábrica aceita dois modos:

## Modo recomendado para produção: API batch
Use `.env.local` e `npm run voice:generate -- <aula>`. É reproduzível e salva um MP3 por segmento.

## MCP oficial (opcional para Claude)
O projeto oficial é `elevenlabs/elevenlabs-mcp`. Ele permite TTS via Claude e outros clientes. Instale `uv`/`uvx` e configure a chave como variável de ambiente do servidor MCP. Para a fábrica, a API batch continua sendo o caminho principal porque os arquivos e nomes são determinísticos.
