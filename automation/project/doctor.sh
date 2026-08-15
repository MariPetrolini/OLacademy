#!/usr/bin/env bash
set -u
check(){ if command -v "$1" >/dev/null 2>&1; then echo "✅ $2: $(command -v "$1")"; else echo "❌ $2"; fi; }
echo "=== Fábrica de Cursos V4 ==="
check node Node
check npm npm
check git Git
check ffmpeg FFmpeg
check ffprobe FFprobe
check claude "Claude Code"
check codex Codex
check soffice LibreOffice
check pdftoppm Poppler
check unzip unzip
if [ -f .env.local ]; then echo "✅ .env.local existe (conteúdo não exibido)"; else echo "⚠️ .env.local ausente"; fi
