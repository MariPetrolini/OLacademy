# Comece aqui

## 1. Instalar dependências do projeto
Na raiz:
```bash
npm install
npm --prefix remotion install
```

Para ingestão PPT no macOS:
```bash
brew install --cask libreoffice
brew install poppler
```

## 2. Credenciais ElevenLabs
```bash
cp .env.example .env.local
```
Edite apenas localmente:
```env
ELEVENLABS_API_KEY=...
ELEVENLABS_VOICE_ID=...
```
Nunca commite `.env.local`.

## 3. Criar aula
```bash
npm run lesson:new -- fundamentos-redes mac-learning "Como um switch aprende endereços MAC"
```

## 4. Abrir Claude Code
```bash
claude
```
Prompt inicial:
> Leia CLAUDE.md e AGENTS.md. Produza a aula `courses/fundamentos-redes/lessons/mac-learning` seguindo o workflow. Comece pela pesquisa e pare obrigatoriamente nas duas pausas humanas.

## 5. Codex
Quando o Claude pedir revisão, abra outro terminal na raiz:
```bash
codex
```
E peça:
> Revise `courses/.../lesson` seguindo CODEX.md. Não altere silenciosamente o roteiro; escreva o relatório exigido.

## 6. PPT
Após a primeira pausa humana e `continue`:
```bash
npm run slides:ingest -- courses/.../lesson --pptx "/caminho/aula.pptx"
```

## 7. Voz
Após a segunda pausa humana e `continue`:
```bash
npm run voice:generate -- courses/.../lesson
```

## 8. Vídeo
```bash
npm run storyboard:auto -- courses/.../lesson
npm run video:render -- courses/.../lesson
```
