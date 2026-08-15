#!/usr/bin/env python3
"""Gera storyboard/scene-plan.json a partir de script/slide-map.json.

Decisao de desenho: UMA CENA POR SEGMENTO, mesmo quando varias cenas repetem o mesmo
slide. Motivo: remotion/src/Video.tsx aplica os overlays de uma cena pela duracao inteira
dela. Agrupar os 7 segmentos do slide 005 em uma cena unica daria ~2 min de quadro estatico,
contra a regra de 35s de brain/visual-language.md. Uma cena por segmento permite que o
destaque acompanhe a fala usando so o que o renderer ja implementa.

Overlays usam exclusivamente type='highlight', o unico tipo implementado hoje em Video.tsx.
Coordenadas sao normalizadas (0..1) e foram derivadas da geometria de
source/slide-build/gen_slides.py e conferidas nos PNGs rasterizados. Sao aproximadas:
conferir no render e ajustar na QA audiovisual da Fase 8.

uso: python3 storyboard/build-scene-plan.py   (a partir da pasta da aula)
"""
import json, pathlib, sys

LESSON = pathlib.Path(__file__).resolve().parent.parent
smap = json.loads((LESSON / "script" / "slide-map.json").read_text(encoding="utf-8"))

# Fase 8: se o audio ja existe, a duracao real substitui a estimativa. E o que
# CLAUDE.md item 25 pede. Sem audio, cai de volta na estimativa.
AUDIO = LESSON / "voice" / "audio-manifest.json"
REAL = {}
if AUDIO.exists():
    REAL = {x["id"]: x["durationSeconds"]
            for x in json.loads(AUDIO.read_text(encoding="utf-8"))["segments"]}

# --- geometria do slide 005: tabela de 7 linhas ---
T5_X, T5_W = 0.0625, 0.875
T5_TOP, T5_ROW = 0.1083, 0.0679          # linha 0 = camada 7


def row5(i, span=1):
    return {"type": "highlight", "x": T5_X, "y": round(T5_TOP + i * T5_ROW, 4),
            "w": T5_W, "h": round(T5_ROW * span, 4)}


# destaque por segmento. Ausente = slide limpo, sem overlay.
HL = {
    # slide 005 — o destaque desce e sobe junto com a enumeracao
    "SEG-012": row5(6, 1) | {"label": "Camada 1"},
    "SEG-013": row5(5, 1) | {"label": "Camada 2"},
    "SEG-014": row5(4, 1) | {"label": "Camada 3"},
    "SEG-015": row5(3, 1) | {"label": "Camada 4"},
    "SEG-016": row5(1, 2) | {"label": "Camadas 5 e 6"},
    "SEG-017": row5(0, 1) | {"label": "Camada 7"},
    # slide 008 — a barra DADOS|FCS, onde o controle vem depois dos dados
    "SEG-022": {"type": "highlight", "x": 0.521, "y": 0.412, "w": 0.396, "h": 0.116,
                "label": "Controle depois dos dados"},
    # slide 010 — o bloco da contagem, depois a faixa de procedencia
    "SEG-026": {"type": "highlight", "x": 0.0625, "y": 0.3037, "w": 0.875, "h": 0.2778},
    "SEG-027": {"type": "highlight", "x": 0.2656, "y": 0.602, "w": 0.672, "h": 0.085,
                "label": "A norma que define cada nome"},
    # slide 011 — a camada 5 sem contraparte
    "SEG-030": {"type": "highlight", "x": 0.09375, "y": 0.4407, "w": 0.198, "h": 0.0704,
                "label": "Sem camada separada"},
    # slide 012 — a ordem LLC sobre MAC
    "SEG-032": {"type": "highlight", "x": 0.094, "y": 0.343, "w": 0.37, "h": 0.194,
                "label": "LLC sobre MAC"},
    # slide 013 — o erro mais comum
    "SEG-035": {"type": "highlight", "x": 0.5885, "y": 0.547, "w": 0.328, "h": 0.1815},
}

# Enriquecimentos desejados que o renderer AINDA NAO suporta. Registrados aqui em vez de
# irem para overlays com type inexistente, que Video.tsx descartaria em silencio.
WANTED = {
    "SEG-001": "pan lento sobre a linha vermelha, do notebook ate o servidor",
    "SEG-006": "revelar o X sobre a coluna da pilha de protocolos no momento em que a fala diz que ela nao venceu",
    "SEG-007": "animar a seta vertical (servico) e depois a horizontal tracejada (protocolo)",
    "SEG-008": "pulsar as duas caixas da camada 3 em sincronia, para marcar a paridade",
    "SEG-018": "acender a pilha do relay apenas nas camadas 1 a 3",
    "SEG-020": "revelar SDU + PCI = PDU termo por termo",
    "SEG-024": "revelar as caixas aninhadas de fora para dentro, uma por camada citada",
    "SEG-029": "desenhar o colchete de 6-7 para Aplicacao, deixando a camada 5 por ultimo e sem ligacao",
    "SEG-034": "revelar os degraus 1, 2 e 3 na ordem da fala",
    "SEG-038": "revelar os seis cartoes de resumo na ordem em que sao citados",
}

scenes, errs = [], []
for i, item in enumerate(smap["segments"], start=1):
    sid, slide = item["segmentId"], item["slideNumber"]
    sc = {
        "id": f"SCN-{i:03d}",
        "slideNumber": slide,
        "segmentIds": [sid],
        "overlays": [HL[sid]] if sid in HL else [],
        "transition": "fade",
        "durationSeconds": REAL.get(sid, item["estimatedSeconds"]),
    }
    if sid in WANTED:
        sc["wantedMotion"] = WANTED[sid]
    scenes.append(sc)

for sid, o in HL.items():
    for k in ("x", "y", "w", "h"):
        if not 0 <= o[k] <= 1:
            errs.append(f"{sid}: {k}={o[k]} fora de 0..1")
    if o["y"] + o["h"] > 1.001 or o["x"] + o["w"] > 1.001:
        errs.append(f"{sid}: destaque sai do quadro")
    if o["type"] != "highlight":
        errs.append(f"{sid}: type '{o['type']}' nao e suportado por Video.tsx")

covered = {s["slideNumber"] for s in scenes}
for n in range(1, smap["slideCount"] + 1):
    if n not in covered:
        errs.append(f"slide {n}: ausente do storyboard")

plan = {
    "lessonId": smap["lessonId"],
    "generatedBy": "storyboard/build-scene-plan.py",
    "sceneStrategy": "one-scene-per-segment",
    "durationSource": "audio-manifest (medido por ffprobe)" if REAL else "estimativa 135 ppm",
    "note": ("NAO usar npm run storyboard:auto nesta aula: ele agrupa segmentos consecutivos do "
             "mesmo slide em uma cena unica, o que destruiria a estrategia de uma cena por "
             "segmento e descartaria os overlays. Overlays limitados a 'highlight', o unico tipo "
             "implementado em remotion/src/Video.tsx; ver wantedMotion para o resto."),
    "slideBaseDecision": ("PNG do slide como base visual obrigatoria, conforme CLAUDE.md Fase 8 "
                          "item 26. Conflita com brain/visual-language.md — ver OQ-007."),
    "sceneCount": len(scenes),
    "scenes": scenes,
}
(LESSON / "storyboard" / "scene-plan.json").write_text(
    json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"cenas          : {len(scenes)}")
print(f"slides cobertos: {len(covered)}/{smap['slideCount']}")
print(f"com destaque   : {sum(1 for s in scenes if s['overlays'])}")
print(f"com movimento desejado (nao implementado): {sum(1 for s in scenes if 'wantedMotion' in s)}")
print(f"duracao estimada: {sum(s['durationSeconds'] for s in scenes)/60:.1f} min")
print("ERROS: nenhum" if not errs else "ERROS:")
for e in errs:
    print("  -", e)
sys.exit(1 if errs else 0)
