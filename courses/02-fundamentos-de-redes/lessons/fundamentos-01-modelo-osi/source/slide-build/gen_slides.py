#!/usr/bin/env python3
# Gera os 15 slides da aula fundamentos-01-modelo-osi como HTML 1920x1080,
# na identidade de brain/branding.md. Rasterizacao por Chrome headless.
import pathlib, html

OUT = pathlib.Path(__file__).parent / "slides_html"
OUT.mkdir(exist_ok=True)

RED = "#771215"
N900 = "#333333"
N500 = "#B6B6B6"
N100 = "#F1F1F1"
W, H = 1920, 1080

CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;background:#fff;color:{N900};
  font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;
  -webkit-font-smoothing:antialiased}}
.slide{{position:relative;width:{W}px;height:{H}px;padding:70px 120px 64px;
  display:flex;flex-direction:column;overflow:hidden}}
.grid{{position:absolute;inset:0;pointer-events:none;
  background-image:linear-gradient(to right,rgba(51,51,51,.055) 1px,transparent 1px),
                   linear-gradient(to bottom,rgba(51,51,51,.055) 1px,transparent 1px);
  background-size:64px 64px}}
.eyebrow{{display:flex;align-items:center;gap:16px;font-family:Menlo,'SF Mono',Monaco,monospace;
  font-size:24px;letter-spacing:.22em;text-transform:uppercase;color:{N900};opacity:.85;
  margin-bottom:18px;position:relative;z-index:2}}
.eyebrow::before{{content:'';width:52px;height:6px;background:{RED};flex:none}}
h1{{font-size:82px;line-height:1.02;letter-spacing:-.022em;font-weight:700;
  margin-bottom:14px;position:relative;z-index:2}}
h1.sm{{font-size:66px}}
.rule{{width:132px;height:7px;background:{RED};margin-bottom:34px;position:relative;z-index:2}}
.body{{position:relative;z-index:2;flex:1;display:flex;flex-direction:column;min-height:0}}
.mono{{font-family:Menlo,'SF Mono',Monaco,monospace}}
.note{{font-size:30px;line-height:1.34;color:{N900};opacity:.86}}
/* blocos curtos em linha */
.blocks{{display:flex;gap:22px}}
.blk{{flex:1;border:3px solid {N900};padding:20px 22px;font-size:30px;line-height:1.26}}
.blk.dark{{background:{N900};color:#fff;border-color:{N900}}}
/* comparacao duas colunas */
.cmp{{display:flex;gap:26px;flex:1;min-height:0}}
.col{{flex:1;border:4px solid {N900};display:flex;flex-direction:column}}
.col.off{{border-color:{N500};color:{N500};background:{N100};position:relative}}
.col.on{{border-color:{RED}}}
.col .hd{{font-size:36px;font-weight:700;padding:18px 24px;border-bottom:4px solid currentColor}}
.col.on .hd{{color:{RED};border-bottom-color:{RED}}}
.col .bd{{padding:24px;font-size:32px;line-height:1.32;flex:1}}
.strike{{position:absolute;inset:0;width:100%;height:100%}}
/* tabela */
table{{width:100%;border-collapse:collapse;font-size:32px}}
th,td{{border:3px solid {N900};padding:16px 22px;text-align:left}}
th{{background:{N900};color:#fff;font-size:30px;letter-spacing:.02em}}
/* cartoes de resumo */
.cards{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}}
.card{{border:3px solid {N900};padding:20px 22px}}
.card .n{{font-family:Menlo,'SF Mono',Monaco,monospace;font-size:44px;color:{N500};
  font-weight:700;line-height:1}}
.card .t{{font-size:30px;font-weight:700;margin:8px 0 6px}}
.card .p{{font-size:26px;line-height:1.28;opacity:.88}}
.band{{background:{RED};color:#fff;padding:26px 30px;margin-top:20px}}
.band .k{{font-family:Menlo,'SF Mono',Monaco,monospace;font-size:22px;letter-spacing:.22em;
  opacity:.9;margin-bottom:8px}}
.band .t{{font-size:44px;font-weight:700;margin-bottom:10px}}
.band .p{{font-size:27px;line-height:1.32;opacity:.95}}
.callout{{border:4px solid {RED};background:#fff;padding:20px 24px;font-size:29px;line-height:1.3}}
.callout .k{{font-family:Menlo,'SF Mono',Monaco,monospace;font-size:21px;letter-spacing:.2em;
  color:{RED};font-weight:700;margin-bottom:8px}}
.center{{display:flex;align-items:center;justify-content:center;flex:1}}
.eq{{font-family:Menlo,'SF Mono',Monaco,monospace;font-size:150px;font-weight:700;color:{RED};
  letter-spacing:-.01em}}
"""

def page(inner, grid=True):
    return (f"<!doctype html><meta charset='utf-8'><style>{CSS}</style>"
            f"<div class='slide'>{'<div class=grid></div>' if grid else ''}{inner}</div>")

def head(eyebrow, title=None, small=False, rule=True):
    s = f"<div class='eyebrow'>{eyebrow}</div>" if eyebrow else ""
    if title:
        s += f"<h1{' class=sm' if small else ''}>{title}</h1>"
        if rule:
            s += "<div class='rule'></div>"
    return s

# ---------- helpers SVG ----------
def layer_stack(x, y, bw, bh, items, red_at=None, dim=(), label=None, fs=27):
    """items: lista de (numero, nome) de cima para baixo."""
    o = []
    for i, (num, name) in enumerate(items):
        yy = y + i * bh
        n = str(num)
        is_red = red_at is not None and n == str(red_at)
        fill = "#fff" if n not in dim else N100
        sw = 4 if is_red else 3
        col = RED if is_red else N900
        o.append(f"<rect x='{x}' y='{yy}' width='{bw}' height='{bh}' fill='{fill}' "
                 f"stroke='{col}' stroke-width='{sw}'/>")
        o.append(f"<line x1='{x+62}' y1='{yy}' x2='{x+62}' y2='{yy+bh}' stroke='{N900}' stroke-width='2'/>")
        o.append(f"<text x='{x+31}' y='{yy+bh/2+10}' font-size='{fs}' text-anchor='middle' "
                 f"font-family=\"Menlo,monospace\" fill='{col}'>{n}</text>")
        o.append(f"<text x='{x+80}' y='{yy+bh/2+10}' font-size='{fs}' fill='{col}'>{html.escape(name)}</text>")
    if label:
        o.append(f"<text x='{x+bw/2}' y='{y+len(items)*bh+40}' font-size='27' text-anchor='middle' "
                 f"font-family=\"Menlo,monospace\" fill='{N900}'>{html.escape(label)}</text>")
    return "".join(o)

def brace(x, y1, y2, d=22, col=None):
    """Colchete simples voltado para a direita. Geometria previsivel."""
    col = col or N900
    m = (y1 + y2) / 2
    return (f"<path d='M{x} {y1} L{x+d} {y1} L{x+d} {y2} L{x} {y2}' fill='none' "
            f"stroke='{col}' stroke-width='3'/>"
            f"<line x1='{x+d}' y1='{m}' x2='{x+d+14}' y2='{m}' stroke='{col}' stroke-width='3'/>")

SEVEN = [(7, "Aplicação"), (6, "Apresentação"), (5, "Sessão"), (4, "Transporte"),
         (3, "Rede"), (2, "Enlace de dados"), (1, "Física")]

slides = {}

# ---------------- 01 ----------------
def dev(x, y, w, h, kind):
    s = f"<g stroke='{N900}' stroke-width='3.5' fill='#fff' stroke-linejoin='round'>"
    if kind == "laptop":
        s += f"<rect x='{x+18}' y='{y}' width='{w-36}' height='{h*0.62}' rx='6'/>"
        s += f"<path d='M{x} {y+h*0.72} L{x+w} {y+h*0.72} L{x+w-14} {y+h*0.62} L{x+14} {y+h*0.62} Z'/>"
    elif kind == "switch":
        s += f"<rect x='{x}' y='{y+h*0.22}' width='{w}' height='{h*0.42}' rx='5'/>"
        for i in range(9):
            s += f"<rect x='{x+16+i*((w-38)/9)}' y='{y+h*0.34}' width='{(w-46)/9*0.72}' height='{h*0.17}' stroke-width='2.5'/>"
    elif kind == "router":
        s += f"<rect x='{x}' y='{y+h*0.34}' width='{w}' height='{h*0.34}' rx='7'/>"
        s += f"<line x1='{x+w*0.3}' y1='{y+h*0.34}' x2='{x+w*0.18}' y2='{y}'/>"
        s += f"<line x1='{x+w*0.7}' y1='{y+h*0.34}' x2='{x+w*0.84}' y2='{y}'/>"
        for i in range(4):
            s += f"<circle cx='{x+w*0.26+i*w*0.16}' cy='{y+h*0.51}' r='4' stroke-width='2.5'/>"
    else:  # server
        s += f"<rect x='{x}' y='{y}' width='{w}' height='{h*0.78}' rx='5'/>"
        for r in range(3):
            for c in range(3):
                s += (f"<rect x='{x+14+c*((w-28)/3)}' y='{y+12+r*((h*0.78-24)/3)}' "
                      f"width='{(w-34)/3*0.86}' height='{(h*0.78-30)/3*0.74}' stroke-width='2'/>")
    return s + "</g>"

s1 = head("O problema", "Nada disso foi<br>testado junto.")
s1 += f"""<div class='body'>
<svg width='1680' height='430' style='margin:-6px 0 18px'>
{dev(20,150,250,180,'laptop')}{dev(470,150,290,180,'switch')}
{dev(980,150,260,180,'router')}{dev(1420,140,250,190,'server')}
<path d='M270 268 L400 268 L400 205 L470 205' fill='none' stroke='{RED}' stroke-width='6'/>
<path d='M760 205 L880 205 L880 262 L980 262' fill='none' stroke='{RED}' stroke-width='6'/>
<path d='M1240 262 L1350 262 L1350 214 L1420 214' fill='none' stroke='{RED}' stroke-width='6'/>
</svg>
<div class='blocks'>
<div class='blk'>Fabricantes<br>diferentes.</div>
<div class='blk'>Sistemas operacionais<br>diferentes.</div>
<div class='blk'>Nenhum teste<br>conjunto.</div>
<div class='blk'>E funciona.</div>
<div class='blk dark'>Sem <b>ordem</b>, tentativa e erro.<br>Com <b>ordem</b>, método.</div>
</div></div>"""
slides[1] = s1

# ---------------- 02 ----------------
s2 = f"""<div class='eyebrow'>A norma</div>
<div style='display:flex;justify-content:space-between;align-items:flex-start;position:relative;z-index:2'>
<div><h1 class='sm'>Open Systems Interconnection</h1><div class='rule'></div></div>
<div style='text-align:right'>
<div style='display:flex;gap:14px'>
<div class='mono' style='border:3px solid {N900};padding:12px 18px;font-size:30px'>ISO/IEC 7498-1</div>
<div class='mono' style='border:3px solid {N900};padding:12px 18px;font-size:30px'>ITU-T X.200</div></div>
<div class='mono' style='font-size:22px;opacity:.75;margin-top:10px'>Texto idêntico, duas designações</div>
</div></div>
<div class='body'>
<div class='blocks' style='margin-bottom:28px'>
<div class='blk dark'>Referência, não implementação.</div>
<div class='blk dark'>Divide responsabilidades e define fronteiras.</div>
<div class='blk dark'>Não diz como construir.</div></div>
<div class='cmp'>
<div class='col off'><div class='hd'>A pilha de protocolos OSI</div>
<div class='bd'>Não venceu comercialmente.<br>Substituída pelo TCP/IP.</div>
<svg class='strike'><line x1='2%' y1='4%' x2='98%' y2='96%' stroke='{N500}' stroke-width='7'/>
<line x1='98%' y1='4%' x2='2%' y2='96%' stroke='{N500}' stroke-width='7'/></svg></div>
<div class='col on'><div class='hd'>O modelo OSI</div>
<div class='bd'>Em vigor.<br>A linguagem comum da área.</div></div>
</div></div>"""
slides[2] = s2

# ---------------- 03 ----------------
s3 = head("Conceito-chave", "Serviço não é protocolo.")
s3 += f"""<div class='body' style='justify-content:center'><svg width='1680' height='560'>
<rect x='90' y='300' width='330' height='190' fill='{N900}'/>
<text x='255' y='412' font-size='34' fill='#fff' text-anchor='middle'>Camada N</text>
<rect x='1260' y='300' width='330' height='190' fill='#fff' stroke='{N900}' stroke-width='5'/>
<text x='1425' y='412' font-size='34' fill='{N900}' text-anchor='middle'>Camada N</text>
<defs><marker id='ar' markerWidth='11' markerHeight='11' refX='8' refY='5.5' orient='auto'>
<path d='M0 0 L11 5.5 L0 11 z' fill='{RED}'/></marker></defs>
<line x1='255' y1='300' x2='255' y2='150' stroke='{RED}' stroke-width='8' marker-end='url(#ar)'/>
<text x='300' y='196' font-size='31' fill='{RED}' font-weight='bold'>Serviço.</text>
<text x='300' y='238' font-size='29' fill='{N900}'>Vertical. Para a camada de cima.</text>
<line x1='420' y1='395' x2='1250' y2='395' stroke='{RED}' stroke-width='8'
 stroke-dasharray='26 18' marker-end='url(#ar)'/>
<text x='835' y='355' font-size='31' fill='{RED}' font-weight='bold' text-anchor='middle'>Protocolo.</text>
<text x='835' y='464' font-size='29' fill='{N900}' text-anchor='middle'>Horizontal. Com o par do outro lado.</text>
</svg></div>"""
slides[3] = s3

# ---------------- 04 (7 camadas nas duas pontas) ----------------
BH, BW = 74, 330
s4 = head("A engrenagem", "Entidades pares e aprimoramento passo a passo.", small=True)
y0 = 70
LINE_Y = y0 + 4 * BH + BH / 2   # centro da camada 3
s4 += f"""<div class='body'><svg width='1680' height='680'>
{layer_stack(120,y0,BW,BH,SEVEN,red_at=3,label='Machine A')}
{layer_stack(1230,y0,BW,BH,SEVEN,red_at=3,label='Machine B')}
<line x1='450' y1='{LINE_Y}' x2='1230' y2='{LINE_Y}' stroke='{RED}' stroke-width='7'/>
{brace(80,y0,y0+7*BH,d=18)}
<text x='520' y='{LINE_Y-124}' font-size='26' fill='{RED}'>Entidades pares: mesma camada, máquinas</text>
<text x='520' y='{LINE_Y-88}' font-size='26' fill='{RED}'>diferentes. Camada 3 fala com camada 3.</text>
<text x='520' y='{LINE_Y-52}' font-size='26' fill='{RED}'>Nunca camada 3 com camada 4.</text>
<text x='520' y='{LINE_Y+62}' font-size='25' fill='{N900}'>Serviço cumulativo: o serviço de uma camada é a</text>
<text x='520' y='{LINE_Y+96}' font-size='25' fill='{N900}'>capacidade dela mais todas as de baixo.</text>
</svg></div>"""
slides[4] = s4

# ---------------- 05 ----------------
rows = "".join(
    f"<tr><td class='mono' style='width:80px;text-align:center'>{n}</td>"
    f"<td style='width:390px'><b>{nm}</b></td><td>{d}</td></tr>"
    for n, nm, d in [
        (7, "Aplicação", "Único acesso do processo à rede."),
        (6, "Apresentação", "Representação comum da informação."),
        (5, "Sessão", "Organiza e sincroniza o diálogo."),
        (4, "Transporte", "Transferência transparente."),
        (3, "Rede", "Independência de roteamento."),
        (2, "Enlace de dados", "Vizinhos diretos e erros do meio."),
        (1, "Física", "Bits no meio físico."),
    ])
slides[5] = head("As sete camadas") + f"<div class='body'><table>{rows}</table></div>"

# ---------------- 06 (CORRECAO C1) ----------------
RELAY = [(3, "Rede"), (2, "Enlace"), (1, "Física")]
s6 = head("Definição exata", None)
s6 += f"""<div class='body'>
<div class='cmp' style='flex:none;height:180px;margin-bottom:26px'>
<div class='col off'><div class='hd'>Errado</div><div class='bd'>A camada do IP</div></div>
<div class='col on'><div class='hd'>O que a norma diz</div>
<div class='bd'>Independência de roteamento e encaminhamento.</div></div></div>
<div style='font-size:44px;font-weight:700;margin-bottom:10px'>Passagem, não destino.</div>
<svg width='1680' height='600'>
{layer_stack(60,10,300,62,SEVEN,dim=('7','6','5','4'),label='Machine A',fs=25)}
{layer_stack(690,10+4*62,300,62,RELAY,label='Relay Router',fs=25)}
{layer_stack(1320,10,300,62,SEVEN,dim=('7','6','5','4'),label='Machine B',fs=25)}
<path d='M360 {10+6*62+31} L690 {10+6*62+31}' stroke='{RED}' stroke-width='6'/>
<path d='M990 {10+6*62+31} L1320 {10+6*62+31}' stroke='{RED}' stroke-width='6'/>
<text x='690' y='120' font-size='26' fill='{N900}'>Em um sistema de relay, só as camadas de baixo</text>
<text x='690' y='158' font-size='26' fill='{N900}'>participam do encaminhamento daquele tráfego.</text>
<text x='690' y='196' font-size='26' fill='{N900}'>O equipamento continua tendo camadas altas,</text>
<text x='690' y='234' font-size='26' fill='{N900}'>para ser gerenciado.</text>
</svg></div>"""
slides[6] = s6

# ---------------- 07 ----------------
s7 = head("Passo 1 de 3", "Três nomes que você vai usar sempre.", small=True)
s7 += f"""<div class='body'><div class='center' style='flex:none;margin:14px 0 34px'>
<div class='eq'>SDU + PCI = PDU</div></div>
<div class='blocks'>
<div class='blk'><div class='mono' style='font-size:34px;color:{RED};font-weight:700;margin-bottom:10px'>PCI</div>
Informação de controle de protocolo.</div>
<div class='blk'><div class='mono' style='font-size:34px;color:{RED};font-weight:700;margin-bottom:10px'>SDU</div>
Carga que a camada não interpreta.</div>
<div class='blk'><div class='mono' style='font-size:34px;color:{RED};font-weight:700;margin-bottom:10px'>PDU</div>
PCI + dados do usuário. Desce para virar a SDU da camada inferior.</div>
</div></div>"""
slides[7] = s7

# ---------------- 08 ----------------
s8 = head("Erro comum", "O cabeçalho não vai necessariamente na frente.", small=True)
s8 += f"""<div class='body'><div class='cmp'>
<div class='col off'><div class='hd'>O que se ouve</div>
<div class='bd'>Cabeçalho na frente dos dados.
<svg width='100%' height='210' style='margin-top:26px'>
<rect x='4' y='30' width='47%' height='120' fill='{N100}' stroke='{N500}' stroke-width='4'/>
<text x='25%' y='105' font-size='34' fill='{N500}' text-anchor='middle' font-family='Menlo,monospace'>HEADER</text>
<rect x='48%' y='30' width='47%' height='120' fill='{N100}' stroke='{N500}' stroke-width='4'/>
<text x='71%' y='105' font-size='34' fill='{N500}' text-anchor='middle' font-family='Menlo,monospace'>DATA</text>
<line x1='6%' y1='34' x2='92%' y2='146' stroke='{N500}' stroke-width='8'/>
<line x1='92%' y1='34' x2='6%' y2='146' stroke='{N500}' stroke-width='8'/></svg></div></div>
<div class='col on'><div class='hd'>O que a norma registra</div>
<div class='bd'>Nenhuma relação de posição definida.
<svg width='100%' height='210' style='margin-top:26px'>
<rect x='4' y='30' width='72%' height='120' fill='#fff' stroke='{N900}' stroke-width='4'/>
<text x='38%' y='105' font-size='36' fill='{N900}' text-anchor='middle'>DADOS</text>
<rect x='76%' y='30' width='22%' height='120' fill='{RED}' stroke='{RED}' stroke-width='4'/>
<text x='87%' y='105' font-size='34' fill='#fff' text-anchor='middle' font-family='Menlo,monospace'>FCS</text>
<text x='4' y='195' font-size='25' fill='{RED}' font-family='Menlo,monospace'>Exemplo Ethernet: FCS no fim do quadro.</text>
</svg></div></div></div></div>"""
slides[8] = s8

# ---------------- 09 ----------------
s9 = head("Evidência", "A mesma estrutura, em bytes.")
s9 += f"""<div class='body' style='justify-content:center'><svg width='1680' height='540'>
<rect x='10' y='40' width='1660' height='430' fill='#fff' stroke='{N900}' stroke-width='4'/>
<text x='60' y='268' font-size='31' font-family='Menlo,monospace' fill='{N900}'>Enlace</text>
<rect x='260' y='95' width='1380' height='320' fill='#fff' stroke='{N900}' stroke-width='4'/>
<text x='310' y='268' font-size='31' font-family='Menlo,monospace' fill='{N900}'>Rede</text>
<rect x='500' y='150' width='1110' height='210' fill='#fff' stroke='{N900}' stroke-width='4'/>
<text x='550' y='268' font-size='31' font-family='Menlo,monospace' fill='{N900}'>Transporte</text>
<rect x='820' y='196' width='760' height='120' fill='#fdf2f2' stroke='{RED}' stroke-width='5'/>
<text x='1200' y='268' font-size='31' font-family='Menlo,monospace' fill='{RED}' text-anchor='middle'>Carga não interpretada</text>
</svg></div>"""
slides[9] = s9

# ---------------- 10 ----------------
trs = "".join(f"<tr><td class='mono'>{t}</td><td class='mono' style='text-align:center'>{v}</td></tr>"
              for t, v in [("packet", f"<b style='color:{RED};font-size:36px'>0</b>"),
                           ("datagram", f"<b style='color:{RED};font-size:36px'>0</b>"),
                           ("frame", "8 &nbsp;(todas em &ldquo;framework&rdquo;)"),
                           ("segment", "só a operação de segmentar")])
s10 = head("Rigor de fonte", "Esses nomes não são do OSI.")
s10 += f"""<div class='body'>
<table><tr><th>Termo procurado no texto integral</th><th style='text-align:center;width:620px'>Ocorrências</th></tr>{trs}</table>
<div style='display:flex;gap:22px;margin-top:26px'>
<div class='callout' style='flex:none'>O único termo OSI: <b class='mono' style='color:{RED}'>PDU</b></div>
<div class='blk mono' style='font-size:27px'>Quadro = IEEE 802 &nbsp;|&nbsp; Datagrama = RFC 791 &nbsp;|&nbsp; Segmento = RFC 9293</div>
</div></div>"""
slides[10] = s10

# ---------------- 11 (CORRECAO C4) ----------------
BH2 = 76
s11 = head("OSI × Internet", "Por que tanta gente desenha quatro.", small=True)
top = 40
osi = layer_stack(60, top, 380, BH2, SEVEN, fs=26)
rfc = []
for i, (nm, span, oy) in enumerate([("Aplicação", 2, top), ("Transporte", 1, top + 2 * BH2),
                                    ("Internet", 1, top + 3 * BH2), ("Enlace", 2, top + 4 * BH2)]):
    # posiciona: Aplicacao alinha 7-6 ; Transporte->4 ; Internet->3 ; Enlace->2-1
    pass
# posicoes explicitas do lado RFC 1122
rfc_boxes = [("Aplicação", top, 2 * BH2), ("Transporte", top + 3 * BH2, BH2),
             ("Internet", top + 4 * BH2, BH2), ("Enlace", top + 5 * BH2, 2 * BH2)]
rsvg = ""
for nm, yy, hh in rfc_boxes:
    rsvg += (f"<rect x='1240' y='{yy}' width='380' height='{hh}' fill='#fff' stroke='{N900}' stroke-width='4'/>"
             f"<text x='1430' y='{yy+hh/2+10}' font-size='30' text-anchor='middle' fill='{N900}'>{nm}</text>")
conn = ""
# 7 e 6 -> Aplicacao
conn += brace(452, top, top + 2 * BH2, d=18)
conn += f"<path d='M492 {top+BH2} L1220 {top+BH2}' stroke='{N900}' stroke-width='3' stroke-dasharray='22 14'/>"
# 4 -> Transporte, 3 -> Internet
for src, dst in [(3, 3), (4, 4)]:
    yy = top + src * BH2 + BH2 / 2
    conn += f"<path d='M444 {yy} L1240 {top+dst*BH2+BH2/2}' stroke='{N900}' stroke-width='3' stroke-dasharray='22 14'/>"
# 2 e 1 -> Enlace
conn += brace(452, top + 5 * BH2, top + 7 * BH2, d=18)
conn += f"<path d='M492 {top+6*BH2} L1220 {top+6*BH2}' stroke='{N900}' stroke-width='3' stroke-dasharray='22 14'/>"
# camada 5 isolada: marcador vermelho, sem chave e sem linha
y5 = top + 2 * BH2
conn += f"<rect x='60' y='{y5}' width='380' height='{BH2}' fill='none' stroke='{RED}' stroke-width='5'/>"
s11 += f"""<div class='body' style='justify-content:center'><svg width='1680' height='650'>
<text x='250' y='24' font-size='26' font-family='Menlo,monospace' text-anchor='middle' fill='{N900}'>Modelo OSI</text>
<text x='1430' y='24' font-size='26' font-family='Menlo,monospace' text-anchor='middle' fill='{N900}'>RFC 1122</text>
{osi}{rsvg}{conn}
<g><rect x='520' y='{y5-4}' width='660' height='84' fill='{RED}'/>
<text x='550' y='{y5+28}' font-size='27' fill='#fff' font-family='Menlo,monospace'>Sessão: sem camada separada.</text>
<text x='550' y='{y5+64}' font-size='27' fill='#fff' font-family='Menlo,monospace'>“É camada 6” não tem apoio.</text></g>
</svg></div>"""
slides[11] = s11

# ---------------- 12 (CORRECAO C2: LLC acima de MAC) ----------------
s12 = head("Nem tudo tem número", None)
s12 += f"""<div class='body'><div class='cmp'>
<div class='col'><div class='hd'>Camada 2</div><div class='bd'>
<div style='font-size:29px;line-height:1.34;margin-bottom:22px'>
&#9642; Duas sub-camadas.<br>&#9642; Sub-camada é um conceito previsto e definido no próprio OSI.</div>
<svg width='100%' height='250'>
<rect x='4%' y='6' width='92%' height='104' fill='#fff' stroke='{N900}' stroke-width='4'/>
<text x='50%' y='68' font-size='30' text-anchor='middle' font-family='Menlo,monospace' fill='{N900}'>LLC (Logical Link Control)</text>
<rect x='4%' y='110' width='92%' height='104' fill='{N100}' stroke='{N900}' stroke-width='4'/>
<text x='50%' y='172' font-size='30' text-anchor='middle' font-family='Menlo,monospace' fill='{N900}'>MAC (Medium Access Control)</text>
</svg></div></div>
<div class='col'><div class='hd'>TLS</div><div class='bd'>
<div style='font-size:29px;line-height:1.34;margin-bottom:22px'>
&#9642; Não se declara 5, 6 nem 7.<br>&#9642; Exige apenas um fluxo confiável e em ordem da camada inferior.<br>
&#9642; Cravar um número é inventar.</div>
<svg width='100%' height='250'>
<rect x='16%' y='6' width='68%' height='96' fill='#fff' stroke='{RED}' stroke-width='4' stroke-dasharray='16 10'/>
<text x='50%' y='64' font-size='32' text-anchor='middle' font-family='Menlo,monospace' fill='{RED}'>TLS</text>
<rect x='4%' y='120' width='92%' height='96' fill='#fff' stroke='{N900}' stroke-width='4'/>
<text x='50%' y='178' font-size='29' text-anchor='middle' font-family='Menlo,monospace' fill='{N900}'>Transporte (ex.: TCP)</text>
</svg></div></div></div></div>"""
slides[12] = s12

# ---------------- 13 / 14 (CORRECAO C5) ----------------
def stair(steps):
    """Escada ascendente da esquerda para a direita. Caixa larga o bastante para a evidencia."""
    o, sw, sh, dx, dy = "", 660, 112, 168, 126
    n = len(steps)
    base = 60 + (n - 1) * dy      # base do degrau mais baixo
    for i, (lab, ev) in enumerate(steps):
        x = 40 + i * dx
        y = base - i * dy
        o += f"<rect x='{x}' y='{y}' width='{sw}' height='{sh}' fill='{N100}' stroke='{N900}' stroke-width='4'/>"
        o += (f"<text x='{x+24}' y='{y+45}' font-size='29' font-family='Menlo,monospace' "
              f"fill='{N900}'>{html.escape(lab)}</text>")
        o += (f"<text x='{x+24}' y='{y+85}' font-size='23' fill='{N900}' "
              f"opacity='.85'>{html.escape(ev)}</text>")
    return o

s13 = head("Método da escola — não é norma", "Diagnóstico: de baixo para cima.", small=True)
s13 += f"""<div class='body'><svg width='1680' height='560'>
{stair([("1: Existe enlace?", "Estado da porta, erros, potência óptica"),
        ("2: Os vizinhos se veem?", "Tabela de endereços, resolução, VLAN da porta"),
        ("3: Existe caminho?", "Endereço, máscara, gateway, rotas")])}
<g><rect x='1010' y='352' width='630' height='196' fill='{RED}'/>
<text x='1042' y='398' font-size='22' fill='#fff' font-family='Menlo,monospace' letter-spacing='4'>ERRO MAIS COMUM</text>
<text x='1042' y='446' font-size='26' fill='#fff'>Ida e volta. Falha de retorno se parece</text>
<text x='1042' y='482' font-size='26' fill='#fff'>exatamente com falha de ida.</text>
<text x='1042' y='518' font-size='26' fill='#fff'>Sempre teste as duas direções.</text></g>
</svg></div>"""
slides[13] = s13

s14 = head("Método da escola — não é norma", "Diagnóstico: subindo a pilha.", small=True)
s14 += f"""<div class='body'>
<div class='mono' style='font-size:24px;opacity:.7;margin:-8px 0 12px'>continuação dos degraus 1 a 3</div>
<svg width='1680' height='340'>
{stair([("4: A porta aceita conexão?", "Sessão, retransmissão"),
        ("5–7: O serviço responde certo?", "Nome, certificado, código de resposta, log")])}
</svg>
<div class='blk dark' style='flex:none;font-size:32px;line-height:1.34;margin-top:26px'>
O valor do método não é <b>acertar a camada</b> na primeira tentativa.
É impedir que você investigue a aplicação quando o problema é um cabo.</div></div>"""
slides[14] = s14

# ---------------- 15 (CORRECAO C3) ----------------
cards = [("01", "Referência", "Descreve responsabilidade, não implementação."),
         ("02", "Serviço e protocolo", "Um para cima, outro para o lado."),
         ("03", "Encapsulamento", "Controle acrescentado a uma carga não interpretada."),
         ("04", "Procedência", "Quadro, datagrama e segmento não são do OSI."),
         ("05", "Internet real", "Quatro camadas; aplicação combina 6 e 7. Sessão sem camada separada."),
         ("06", "Método", "De baixo para cima.")]
cs = "".join(f"<div class='card'><div class='n'>{n}</div><div class='t'>{t}</div><div class='p'>{p}</div></div>"
             for n, t, p in cards)
s15 = head("Resumo", None)
s15 += f"""<div class='body'><div class='cards'>{cs}</div>
<div class='band'><div class='k'>SEU EXERCÍCIO</div>
<div class='t'>Sete responsabilidades, uma coisa que você usa.</div>
<div class='p'>Escolha algo que você usa na rede. Escreva qual responsabilidade de cada uma das 7 camadas
está sendo exercida. Onde não conseguir preencher, você encontrou o seu próximo assunto de estudo.</div>
</div></div>"""
slides[15] = s15

for n in range(1, 16):
    (OUT / f"slide-{n:03d}.html").write_text(page(slides[n]), encoding="utf-8")
print(f"{len(slides)} slides HTML em {OUT}")
