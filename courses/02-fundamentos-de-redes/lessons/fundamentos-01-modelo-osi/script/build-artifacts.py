#!/usr/bin/env python3
"""Deriva voice/segments.json e script/slide-map.json de script/lesson-script.md.

Um unico mapa segmento->slide alimenta os dois arquivos, para que nao possam divergir.
Valida cobertura nos dois sentidos e monotonicidade da ordem dos slides.

uso: python3 script/build-artifacts.py   (a partir da pasta da aula)
"""
import json, re, sys, pathlib

LESSON = pathlib.Path(__file__).resolve().parent.parent
WPM = 135.0  # meta de skills/write-spoken-lesson.md (125-145)
SLIDE_COUNT = 15

# Mapa unico segmento -> slide. Fonte de verdade da Fase 5.
SEG2SLIDE = {
    "SEG-000": 1,                       # abertura obrigatoria, sobre o slide de capa
    "SEG-001": 1, "SEG-002": 1,
    "SEG-004": 2, "SEG-005": 2, "SEG-006": 2,
    "SEG-007": 3, "SEG-009": 3,
    "SEG-008": 4, "SEG-010": 4,
    "SEG-011": 5, "SEG-012": 5, "SEG-013": 5, "SEG-014": 5,
    "SEG-015": 5, "SEG-016": 5, "SEG-017": 5,
    "SEG-018A": 6, "SEG-018": 6,
    "SEG-019": 7, "SEG-020": 7, "SEG-021": 7,
    "SEG-022": 8, "SEG-023": 8,
    "SEG-024": 9,
    "SEG-025": 10, "SEG-026": 10, "SEG-027": 10,
    "SEG-028": 11, "SEG-029": 11, "SEG-030": 11, "SEG-031": 11,
    "SEG-032": 12,
    "SEG-033": 13, "SEG-034": 13, "SEG-035": 13,
    "SEG-036": 14, "SEG-037": 14,
    "SEG-038": 15, "SEG-039": 15, "SEG-040": 15,
}

src = (LESSON / "script" / "lesson-script.md").read_text(encoding="utf-8")
lines = src.split("\n")
block, segs, i = None, [], 0
while i < len(lines):
    mb = re.match(r"^## (Bloco \d+) — (.+)$", lines[i])
    if mb:
        block = f"{mb.group(1)} — {mb.group(2)}"
    ms = re.match(r"^\*\*(SEG-\d{3}[A-Z]?)\*\*$", lines[i].strip())
    if ms:
        body, j = [], i + 1
        while j < len(lines) and lines[j].strip():
            if lines[j].lstrip().startswith("<!--"):        # comentario de producao
                while j < len(lines) and "-->" not in lines[j]:
                    j += 1
                j += 1
                continue
            body.append(lines[j].strip())
            j += 1
        text = re.sub(r"\s+", " ", " ".join(body)).replace("‑", "-").strip()
        segs.append({"id": ms.group(1), "text": text, "block": block})
        i = j
        continue
    i += 1

errs = []
seen = set()
for s in segs:
    if s["id"] in seen:
        errs.append(f"{s['id']}: id duplicado")
    seen.add(s["id"])
    if re.search(r"[*_`#\[\]<>]", s["text"]):
        errs.append(f"{s['id']}: markdown residual no texto falado")
    if re.search(r"https?://|www\.|\.com\b|\.org\b", s["text"], re.I):
        errs.append(f"{s['id']}: URL na fala")
    s["words"] = len(s["text"].split())
    s["estimatedSeconds"] = round(s["words"] / WPM * 60.0, 1)
    if s["estimatedSeconds"] > 45:
        errs.append(f"{s['id']}: {s['estimatedSeconds']}s excede o limite de 45s")
    # risco de TTS: artigo/preposicao de uma letra colado numa sigla soletrada que comeca
    # com a mesma letra. "o O S I" sai como gagueira no clone.
    for m in re.finditer(r"\b([A-Za-z])\s+((?:[A-Z]\s){1,}[A-Z])\b", s["text"]):
        if m.group(1).upper() == m.group(2)[0]:
            errs.append(f"{s['id']}: colisao de pronuncia '{m.group(0)}' (artigo + sigla soletrada)")
    s["slide"] = SEG2SLIDE.get(s["id"])
    if s["slide"] is None:
        errs.append(f"{s['id']}: sem slide atribuido")

# cobertura inversa: todo slide precisa de narracao (CLAUDE.md Fase 4, item 14)
used = {s["slide"] for s in segs if s["slide"]}
for n in range(1, SLIDE_COUNT + 1):
    if n not in used:
        errs.append(f"slide {n}: nenhum segmento narra este slide")
extra = sorted(x for x in used if x and not 1 <= x <= SLIDE_COUNT)
for x in extra:
    errs.append(f"slide {x}: fora da faixa 1..{SLIDE_COUNT}")

# ids mapeados que nao existem no roteiro
for sid in SEG2SLIDE:
    if sid not in seen:
        errs.append(f"{sid}: mapeado mas ausente do roteiro")

# monotonicidade: slide nunca retrocede, senao o video pisca entre imagens
prev = 0
for s in segs:
    if s["slide"] and s["slide"] < prev:
        errs.append(f"{s['id']}: slide {s['slide']} retrocede depois do slide {prev}")
    prev = max(prev, s["slide"] or prev)

total_w = sum(s["words"] for s in segs)
total_s = sum(s["estimatedSeconds"] for s in segs)

(LESSON / "voice" / "segments.json").write_text(json.dumps({
    "lessonId": "fundamentos-01-modelo-osi",
    "generatedFrom": "script/lesson-script.md",
    "generatedBy": "script/build-artifacts.py",
    "wordsPerMinuteAssumed": WPM,
    "segments": [{
        "id": s["id"], "text": s["text"], "scriptRef": s["block"],
        "sourcePages": [s["slide"]], "estimatedSeconds": s["estimatedSeconds"],
    } for s in segs],
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

groups = []
for s in segs:
    if not groups or groups[-1]["slideNumber"] != s["slide"]:
        groups.append({"slideNumber": s["slide"], "segmentIds": []})
    groups[-1]["segmentIds"].append(s["id"])

(LESSON / "script" / "slide-map.json").write_text(json.dumps({
    "lessonId": "fundamentos-01-modelo-osi",
    "generatedBy": "script/build-artifacts.py",
    "slideCount": SLIDE_COUNT,
    "note": "Ordem dos slides monotonica. Todo slide narrado, todo segmento com slide.",
    "segments": [{"segmentId": s["id"], "slideNumber": s["slide"],
                  "estimatedSeconds": s["estimatedSeconds"]} for s in segs],
    "groups": groups,
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"segmentos : {len(segs)}")
print(f"palavras  : {total_w}")
print(f"duracao   : {total_s/60:.1f} min a {WPM:.0f} ppm")
print(f"slides    : {len(used)}/{SLIDE_COUNT} narrados | cenas: {len(groups)}")
print(f"maior seg : {max(s['estimatedSeconds'] for s in segs)}s")
print("ERROS: nenhum" if not errs else "ERROS:")
for e in errs:
    print("  -", e)
sys.exit(1 if errs else 0)
