#!/usr/bin/env python3
"""Genere les panneaux SVG du README : une pile d'ecrans d'arcade, pas du markdown."""
import os

OUT = "/home/user/JunnB/assets"
W = 900

# Couleurs linguist de GitHub, celles utilisees par github-metrics.svg
GOLD, CYAN, RED, BLUE, DIM = "#ffd24a", "#7fe3ff", "#ff3b30", "#2f7fff", "#7c89a8"

DEFS = """
  <linearGradient id="gold" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#fffbe6"/><stop offset="28%" stop-color="#ffe066"/>
    <stop offset="52%" stop-color="#f9a825"/><stop offset="53%" stop-color="#e2681a"/>
    <stop offset="100%" stop-color="#a03306"/>
  </linearGradient>
  <linearGradient id="cab" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#141a34"/><stop offset="50%" stop-color="#0a0c1c"/>
    <stop offset="100%" stop-color="#16102a"/>
  </linearGradient>
  <linearGradient id="floor" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#3b1d6e" stop-opacity="0"/>
    <stop offset="100%" stop-color="#7b2ff7" stop-opacity="0.35"/>
  </linearGradient>
  <pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse">
    <rect width="4" height="2" fill="#000" opacity="0.30"/>
  </pattern>
  <radialGradient id="vig" cx="50%" cy="50%" r="72%">
    <stop offset="55%" stop-color="#000" stop-opacity="0"/>
    <stop offset="100%" stop-color="#000" stop-opacity="0.72"/>
  </radialGradient>
"""

CSS = """
  .mono  { font-family: ui-monospace,"SF Mono","Cascadia Mono","DejaVu Sans Mono",Menlo,Consolas,monospace; }
  .heavy { font-family: "Arial Black","Helvetica Neue",Impact,Arial,sans-serif; font-weight:900; }
  .ttl   { font-size:19px; letter-spacing:7px; fill:#7fe3ff; }
  .lbl   { font-size:12px; letter-spacing:2px; fill:#7c89a8; }
  .val   { font-size:13px; letter-spacing:1px; fill:#e6edf3; }
  .blink { animation: blink 1.1s steps(1) infinite; }
  .pulse { animation: pulse 1.4s ease-in-out infinite; }
  @keyframes blink { 0%,55%{opacity:1} 56%,100%{opacity:0} }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.45} }
  @media (prefers-reduced-motion: reduce) { .blink,.pulse { animation:none } }
"""


def head(h, title, extra_css=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" role="img" aria-label="{title}">
  <title>{title}</title>
  <defs>{DEFS}
    <clipPath id="screen"><rect x="14" y="14" width="{W-28}" height="{h-28}" rx="18"/></clipPath>
    <style>{CSS}{extra_css}</style>
  </defs>
  <rect width="{W}" height="{h}" rx="22" fill="#05060d"/>
  <rect x="6" y="6" width="{W-12}" height="{h-12}" rx="20" fill="none" stroke="{RED}" stroke-width="2" opacity="0.55"/>
  <rect x="10" y="10" width="{W-20}" height="{h-20}" rx="19" fill="none" stroke="{BLUE}" stroke-width="2" opacity="0.45"/>
  <g clip-path="url(#screen)">
    <rect x="14" y="14" width="{W-28}" height="{h-28}" fill="url(#cab)"/>'''


def foot(h):
    return f'''    <rect x="14" y="14" width="{W-28}" height="{h-28}" fill="url(#scan)"/>
    <rect x="14" y="14" width="{W-28}" height="{h-28}" fill="url(#vig)"/>
  </g>
</svg>
'''


def titlebar(y, left, right=""):
    """Bandeau de titre facon borne : filet + libelle."""
    s = f'<text class="heavy ttl" x="52" y="{y}">{left}</text>'
    if right:
        s += f'<text class="mono lbl" x="{W-52}" y="{y}" text-anchor="end">{right}</text>'
    s += f'<path d="M52 {y+12} H{W-52}" stroke="{GOLD}" stroke-width="2" opacity="0.55"/>'
    return s


def write(name, body):
    p = os.path.join(OUT, name)
    open(p, "w", encoding="utf-8").write(body)
    print("ecrit:", name, len(body), "octets")


# ══ 01 MARQUEE ═══════════════════════════════════════════════════════════════
def marquee():
    h = 300
    s = head(h, "JUNN II - TURBO EDITION", """
  .logo{font-size:104px;letter-spacing:5px}
  .sub{font-size:21px;letter-spacing:9px;fill:#7fe3ff}
  .tag{font-size:14px;letter-spacing:3px;fill:#a8bcdd}
  .coin{font-size:17px;letter-spacing:4px;fill:#ff4d4d}
  .cred{font-size:13px;letter-spacing:2px;fill:#6c7a94}
  .site{font-size:13px;letter-spacing:2px;fill:#7fe3ff}
  .vs{font-size:34px;fill:#ff3b30}""")
    s += f'''
    <g stroke="#7b2ff7" stroke-width="1" opacity="0.34">
      <path d="M14 252 H886"/><path d="M14 264 H886"/><path d="M14 286 H886"/>
      <path d="M450 244 L450 286"/><path d="M450 244 L330 286"/><path d="M450 244 L570 286"/>
      <path d="M450 244 L170 286"/><path d="M450 244 L730 286"/>
      <path d="M450 244 L-40 286"/><path d="M450 244 L940 286"/>
    </g>
    <rect x="14" y="244" width="872" height="42" fill="url(#floor)"/>
    <rect x="14" y="250" width="872" height="30" fill="#05060d" opacity="0.72"/>
    <g>
      <rect x="60" y="42" width="304" height="20" rx="3" fill="#101426" stroke="#4a5578" stroke-width="2"/>
      <rect x="62" y="44" width="300" height="16" rx="2" fill="{GOLD}"/>
      <rect x="536" y="42" width="304" height="20" rx="3" fill="#101426" stroke="#4a5578" stroke-width="2"/>
      <rect x="538" y="44" width="74" height="16" rx="2" fill="#e2503c"/>
      <text class="mono" style="font-size:13px;letter-spacing:2px;fill:{GOLD}" x="60" y="34">P1  JUNN</text>
      <text class="mono" style="font-size:13px;letter-spacing:2px;fill:{GOLD}" x="840" y="34" text-anchor="end">P2  LE BUG</text>
      <text class="heavy vs pulse" x="450" y="60" text-anchor="middle">VS</text>
    </g>
    <g transform="translate(450 168)"><g transform="skewX(-7)" text-anchor="middle">
      <text class="heavy logo" x="7" y="7" fill="#2b0a4d">JUNN</text>
      <text class="heavy logo" x="4" y="4" fill="#2b0a4d">JUNN</text>
      <text class="heavy logo" x="0" y="0" fill="none" stroke="#1b0730" stroke-width="9" stroke-linejoin="round">JUNN</text>
      <text class="heavy logo" x="0" y="0" fill="url(#gold)">JUNN</text>
    </g></g>
    <text class="heavy sub" x="450" y="207" text-anchor="middle">II &#183; TURBO EDITION</text>
    <text class="mono tag" x="450" y="234" text-anchor="middle">CTO &#183; ARCHITECTE IT &#183; LEAD DEV FULL-STACK</text>
    <text class="mono coin blink" x="450" y="270" text-anchor="middle">INSERT COIN &#8212; PRESS START</text>
    <text class="mono cred" x="60" y="270">CREDITS 00</text>
    <text class="mono site" x="840" y="270" text-anchor="end">BETTERFOLIO.TECH</text>
'''
    write("01-marquee.svg", s + foot(h))


# ══ 02 CHARACTER SELECT ══════════════════════════════════════════════════════
# (monogramme, nom, couleur de bordure linguist, couleur de texte lisible sur fond sombre)
ROSTER = [
    ("TS", "TYPESCRIPT", "#3178c6", "#6ea8e8"), ("NX", "NEXT.JS", "#c9d1d9", "#e6edf3"),
    ("RE", "REACT", "#61dafb", "#61dafb"), ("JS", "JAVASCRIPT", "#f1e05a", "#f1e05a"),
    ("VC", "VERCEL", "#e6edf3", "#e6edf3"), ("PG", "POSTGRES", "#336790", "#7fb3d9"),
    ("HT", "HTML", "#e34c26", "#ff8a65"), ("CS", "CSS", "#663399", "#b18cd9"),
    ("SQ", "PLPGSQL", "#336790", "#7fb3d9"), ("GD", "GODOT", "#478cbf", "#7fc0ec"),
    ("GS", "GDSCRIPT", "#355570", "#8aa9c9"), ("RB", "RUBY", "#701516", "#e57373"),
    ("HM", "HAML", "#ece2a9", "#ece2a9"), ("RA", "RAILS", "#cc0000", "#ff6b6b"),
    ("?",  "LOCKED", "#3a4462", "#5d6a8f"),
]


def character_select():
    # 88 (haut de grille) + 3*84 + 2*22 = 384 de contenu, + la ligne du bas
    h = 440
    s = head(h, "Character select - la stack", """
  .mono2{font-size:11px;letter-spacing:1px}
  .mg{font-size:26px;font-weight:900}""")
    s += titlebar(58, "CHARACTER SELECT", "14 FIGHTERS + 1 ???")
    cw, ch, gx, gy = 156, 84, 52, 88
    for i, (mg, name, col, txt) in enumerate(ROSTER):
        r, c = divmod(i, 5)
        x, y = gx + c * (cw + 12), gy + r * (ch + 22)
        sel = (i == 0)
        s += f'''
    <g>
      <rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="6" fill="#0f1426" stroke="{col}" stroke-width="2" opacity="0.95"/>
      <rect x="{x}" y="{y}" width="{cw}" height="26" rx="6" fill="{col}" opacity="0.18"/>
      <text class="heavy mg" x="{x+cw/2}" y="{y+46}" text-anchor="middle" fill="{txt}">{mg}</text>
      <text class="mono mono2" x="{x+cw/2}" y="{y+70}" text-anchor="middle" fill="#c8d3e8">{name}</text>'''
        if sel:
            s += f'''
      <g stroke="{GOLD}" stroke-width="4" fill="none" class="pulse">
        <path d="M{x-5} {y+14} V{y-5} H{x+16}"/><path d="M{x+cw-16} {y-5} H{x+cw+5} V{y+14}"/>
        <path d="M{x+cw+5} {y+ch-14} V{y+ch+5} H{x+cw-16}"/><path d="M{x+16} {y+ch+5} H{x-5} V{y+ch-14}"/>
      </g>'''
        s += "\n    </g>"
    s += f'''
    <text class="mono blink" style="font-size:13px;letter-spacing:4px;fill:{GOLD}" x="450" y="{h-22}" text-anchor="middle">P1  SELECT YOUR FIGHTER</text>
'''
    write("02-character-select.svg", s + foot(h))


# ══ 03 VS SCREEN / STATS ═════════════════════════════════════════════════════
LANGS = [("TYPESCRIPT", 83.3, "#3178c6"), ("HTML", 3.5, "#e34c26"),
         ("HAML", 3.4, "#ece2a9"), ("RUBY", 3.0, "#701516"),
         ("CSS", 2.8, "#663399"), ("JAVASCRIPT", 2.1, "#f1e05a"),
         ("GDSCRIPT", 1.3, "#355570"), ("PLPGSQL", 0.6, "#336790")]

SCORES = [("1 829", "COMMITS"), ("223", "PULL REQUESTS"),
          ("84", "COMMENTAIRES"), ("52", "ISSUES")]


def stats():
    h = 430
    s = head(h, "High scores et repartition des langages", """
  .big{font-size:38px;fill:url(#gold)}
  .cap{font-size:11px;letter-spacing:2px;fill:#7c89a8}
  .lg{font-size:12px;letter-spacing:1px;fill:#c8d3e8}
  .pc{font-size:12px;fill:#8fa0bf}""")
    s += titlebar(58, "HIGH SCORES", "DEPUIS 2016")
    # Bloc des 4 gros compteurs
    for i, (v, cap) in enumerate(SCORES):
        x = 52 + i * 200
        s += f'''
    <rect x="{x}" y="80" width="180" height="86" rx="6" fill="#0f1426" stroke="#2b3554" stroke-width="2"/>
    <text class="heavy big" x="{x+90}" y="122" text-anchor="middle">{v}</text>
    <text class="mono cap" x="{x+90}" y="146" text-anchor="middle">{cap}</text>'''
    # Barres de vie des langages
    s += titlebar(210, "LIFE BARS", "MOST USED LANGUAGES")
    bx, bw = 190, 560
    for i, (name, pct, col) in enumerate(LANGS):
        y = 236 + i * 22
        fill = max(3, bw * pct / 100)
        s += f'''
    <text class="mono lg" x="{bx-12}" y="{y+11}" text-anchor="end">{name}</text>
    <rect x="{bx}" y="{y}" width="{bw}" height="14" rx="2" fill="#101426" stroke="#2b3554" stroke-width="1"/>
    <rect x="{bx+1}" y="{y+1}" width="{fill:.1f}" height="12" rx="1" fill="{col}"/>
    <text class="mono pc" x="{bx+bw+12}" y="{y+11}">{pct} %</text>'''
    write("03-high-scores.svg", s + foot(h))


# ══ 04 STAGE SELECT / BOSS ═══════════════════════════════════════════════════
def stage_select():
    h = 420
    s = head(h, "Stage select - betterfolio.tech et portfolio", """
  .boss{font-size:26px;fill:url(#gold)}
  .pf{font-size:26px;fill:#7fe3ff}
  .st{font-size:13px;letter-spacing:1px;fill:#c8d3e8}
  .sm{font-size:11px;letter-spacing:2px;fill:#7c89a8}""")
    s += titlebar(58, "STAGE SELECT", "2 STAGES / 16 LOCKED")

    # Carte 1 : betterfolio, le boss
    s += f'''
    <rect x="52" y="80" width="396" height="170" rx="8" fill="#0f1426" stroke="{GOLD}" stroke-width="2"/>
    <rect x="52" y="80" width="396" height="30" rx="8" fill="{GOLD}" opacity="0.16"/>
    <text class="mono sm" x="70" y="100" fill="{GOLD}">FINAL STAGE &#8212; BOSS BATTLE</text>
    <text class="heavy boss" x="70" y="146">BETTERFOLIO.TECH</text>
    <text class="mono st" x="70" y="172">Ma plateforme principale.</text>
    <text class="mono sm" x="70" y="200">TYPESCRIPT &#183; NEXT.JS &#183; VERCEL</text>
    <text class="mono sm" x="70" y="222">STATUS  <tspan fill="#4ade80">EN LIGNE</tspan></text>
    <text class="mono sm blink" x="428" y="236" text-anchor="end" fill="{RED}">&#9654; PLAY</text>'''

    # Carte 2 : le portfolio
    s += f'''
    <rect x="464" y="80" width="384" height="170" rx="8" fill="#0f1426" stroke="{CYAN}" stroke-width="2"/>
    <rect x="464" y="80" width="384" height="30" rx="8" fill="{CYAN}" opacity="0.14"/>
    <text class="mono sm" x="482" y="100" fill="{CYAN}">STAGE 02 &#8212; PLAYER PROFILE</text>
    <text class="heavy pf" x="482" y="146">PORTFOLIO</text>
    <text class="mono st" x="482" y="172">CTO &#183; Architecte IT &#183; Lead dev</text>
    <text class="mono sm" x="482" y="200">12 ANS D&#39;EXP&#201;RIENCE</text>
    <text class="mono sm" x="482" y="222">STATUS  <tspan fill="#4ade80">EN LIGNE</tspan></text>
    <text class="mono sm blink" x="828" y="236" text-anchor="end" fill="{RED}">&#9654; PLAY</text>'''

    # Rangee du bas : le depot public recent, puis les verrouilles
    s += f'''
    <rect x="52" y="272" width="396" height="56" rx="6" fill="#0f1426" stroke="#2b3554" stroke-width="2"/>
    <text class="mono st" x="70" y="296">liste-noel</text>
    <text class="mono sm" x="70" y="316">OPEN &#183; TYPESCRIPT &#183; 2025</text>'''
    for i in range(2):
        x = 464 + i * 200
        s += f'''
    <rect x="{x}" y="272" width="184" height="56" rx="6" fill="#0b0f1e" stroke="#232c47" stroke-width="2"/>
    <text class="heavy" style="font-size:18px;fill:#3a4462" x="{x+20}" y="{306}">?</text>
    <text class="mono sm" x="{x+44}" y="{304}">LOCKED</text>
    <text class="mono sm" x="{x+44}" y="{320}">D&#201;P&#212;T PRIV&#201;</text>'''
    s += f'''
    <text class="mono sm" x="52" y="{h-38}">15 autres d&#233;p&#244;ts verrouill&#233;s. Le vrai boss fight se joue en priv&#233;.</text>'''
    write("04-stage-select.svg", s + foot(h))


marquee()
character_select()
stats()
stage_select()
