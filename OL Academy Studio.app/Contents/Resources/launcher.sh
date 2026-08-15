#!/bin/zsh
set -u

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
RUNTIME_DIR="$PROJECT_ROOT/.studio-runtime"
LOG_FILE="$RUNTIME_DIR/studio.log"
PID_FILE="$RUNTIME_DIR/studio.pid"
FRONTEND_URL="http://localhost:3000"
API_URL="http://127.0.0.1:4318/api/health"

mkdir -p "$RUNTIME_DIR"

if /usr/bin/curl -fsS --max-time 1 "$API_URL" >/dev/null 2>&1 && /usr/bin/curl -fsS --max-time 1 "$FRONTEND_URL" >/dev/null 2>&1; then
  /usr/bin/open "$FRONTEND_URL"
  exit 0
fi

export OLACADEMY_PROJECT_ROOT="$PROJECT_ROOT"
/usr/bin/nohup /bin/zsh -lc 'cd "$OLACADEMY_PROJECT_ROOT" && npm run studio' >"$LOG_FILE" 2>&1 </dev/null &
echo $! >"$PID_FILE"

attempt=0
while [ "$attempt" -lt 60 ]; do
  if /usr/bin/curl -fsS --max-time 1 "$API_URL" >/dev/null 2>&1 && /usr/bin/curl -fsS --max-time 1 "$FRONTEND_URL" >/dev/null 2>&1; then
    /usr/bin/open "$FRONTEND_URL"
    exit 0
  fi
  attempt=$((attempt + 1))
  /bin/sleep 1
done

/usr/bin/osascript -e 'display alert "OL Academy Studio" message "Não foi possível iniciar o Estúdio. Consulte .studio-runtime/studio.log na pasta do projeto." as critical'
exit 1
