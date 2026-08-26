import json, math

SITE = "https://spektric.com"
EMAIL = "info@spektric.com"
YEAR = "2026"

NAV = [
    ("/aba-services", "ABA Services"),
    ("/mental-health", "Mental Health"),
    ("/neurology", "Neurology"),
    ("/who-we-serve", "Who We Serve"),
    ("/about", "About"),
    ("/resources/", "Resources"),
    ("/contact", "Contact"),
]

ARROW = '<svg viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M4 10h11m-4-4 4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def btn(label, href, kind="primary", track=None, arrow=False, extra=""):
    cls = {"primary": "btn", "ghost": "btn btn-ghost", "light": "btn btn-light", "ghost-light": "btn btn-ghost-light"}[kind]
    t = f' data-track="{track}"' if track else ""
    a = ARROW if arrow else ""
    return f'<a class="{cls}{(" " + extra) if extra else ""}" href="{href}"{t}>{label}{a}</a>'


def eyebrow(text, c=None, tag="p"):
    dc = f' data-c="{c}"' if c else ""
    return f'<{tag} class="eyebrow"{dc}>{text}</{tag}>'


def section_head(eb, h2, lede=None, c=None, cls=""):
    l = f'<p class="lede">{lede}</p>' if lede else ""
    return f'<div class="section-head {cls}">{eyebrow(eb, c)}<h2>{h2}</h2>{l}</div>'


def ph(text):
    return f'<span class="ph">[{text}]</span>'


def ph_block(label, text):
    return f'<div class="ph-block"><strong>Placeholder — {label}</strong><p>{text}</p></div>'


def photo(shot, alt, c="aba", cls=""):
    return (f'<figure class="photo {cls}" data-c="{c}" role="img" aria-label="Photo placeholder: {alt}">'
            f'<p class="photo-note"><strong>Photo slot</strong>{shot}</p></figure>')


def notice(text, kind="", icon="i"):
    k = f" notice-{kind}" if kind else ""
    return f'<div class="notice{k}"><span class="notice-icon" aria-hidden="true">{icon}</span><p>{text}</p></div>'


EMERGENCY = ("<strong>If you are experiencing an emergency, call 911 or use the appropriate emergency resource.</strong> "
             "This website and its forms are not monitored for urgent needs.")


def faq(items, open_first=False):
    out = []
    for i, (q, a) in enumerate(items):
        o = " open" if (open_first and i == 0) else ""
        out.append(f'<details class="faq"{o}><summary>{q}<span class="faq-icon" aria-hidden="true"></span></summary><div class="faq-body">{a}</div></details>')
    return "".join(out)


def cta_band(h2="Let’s start with a conversation.",
             p="No pressure and no commitment — just a chance to talk through what you’re looking for and whether Spektric is the right fit.",
             primary=("Get Started", "/contact#schedule"), secondary=("Request Information", "/contact#request")):
    return (f'<section class="cta-band" aria-labelledby="cta-h"><div class="container"><div><h2 id="cta-h">{h2}</h2><p>{p}</p></div>'
            f'<div class="btn-row">{btn(primary[0], primary[1], "light", "cta_band_primary", arrow=True)}{btn(secondary[0], secondary[1], "ghost-light", "cta_band_secondary")}</div></div></section>')


def org_schema():
    return {
        "@context": "https://schema.org",
        "@type": "MedicalBusiness",
        "@id": SITE + "/#organization",
        "name": "Spektric LLC",
        "url": SITE + "/",
        "logo": SITE + "/assets/img/spektric-mark-512.png",
        "image": SITE + "/assets/img/og-image.png",
        "email": EMAIL,
        "description": "Evidence-based ABA, neuropsychological evaluation, and psychotherapy designed around the individual — for children, adolescents, and adults.",
        "medicalSpecialty": ["Psychiatric", "Neurologic"],
        "telephone": "[PLACEHOLDER_PHONE]",
        "address": {"@type": "PostalAddress", "streetAddress": "[PLACEHOLDER]", "addressLocality": "[PLACEHOLDER]", "addressRegion": "[PLACEHOLDER]", "postalCode": "[PLACEHOLDER]", "addressCountry": "US"},
        "sameAs": [],
        "employee": [
            {"@type": "Person", "name": "Alina Vitali", "honorificSuffix": "MSW, LMHC", "jobTitle": "Chief Executive Officer", "worksFor": {"@id": SITE + "/#organization"}, "image": SITE + "/assets/img/team/alina.jpg"},
            {"@type": "Person", "name": "Sheryl Mayoz", "honorificSuffix": "RN, MBA, LHRM, CHC, CCA", "jobTitle": "Chief Financial Officer", "worksFor": {"@id": SITE + "/#organization"}, "image": SITE + "/assets/img/team/sheryl.jpg"},
        ],
    }


def page(path, title, desc, body, *, active=None, schema=None, body_class="", og_type="website", noindex=False, canonical=None, extra_head="", doc_title=None):
    """Wrap body in the site layout."""
    canonical = canonical or (SITE + ("/" if path == "/" else path))
    nav_links = "".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{l}</a></li>' for h, l in NAV)
    panel_links = "".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{l}</a></li>' for h, l in [("/", "Home")] + NAV)
    schemas = [org_schema()] + (schema if schema else [])
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    robots = '<meta name="robots" content="noindex, follow">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large">'
    bc = f' class="{body_class}"' if body_class else ""
    t = doc_title or title
    full_title = t if t.startswith("Spektric") else f"{t} | Spektric LLC"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
{robots}
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#0B0C12">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Spektric LLC">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/img/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{full_title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/assets/img/og-image.png">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png">
<link rel="icon" type="image/png" sizes="64x64" href="/assets/img/favicon-64.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT@9..144,400..600,0..100&family=Albert+Sans:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="/assets/css/styles.css">
{extra_head}{ld}
</head>
<body{bc}>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container nav">
    <a class="brand" href="/" aria-label="Spektric LLC — home">
      <img src="/assets/img/spektric-mark-160.png" alt="" width="42" height="42">
      <span class="brand-text"><span class="brand-word">Spektric<span class="llc">LLC</span></span><span class="brand-sub">ABA · Neurology · Psychotherapy</span></span>
    </a>
    <nav aria-label="Primary">
      <ul class="nav-links">{nav_links}</ul>
    </nav>
    <div class="nav-cta">
      {btn("Request Information", "/contact#request", "ghost", "nav_request_info", extra="btn-sm")}
      {btn("Get Started", "/contact#schedule", "primary", "nav_get_started", extra="btn-sm")}
    </div>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-panel"><span class="label">Menu</span><span class="bars" aria-hidden="true"></span></button>
  </div>
  <div class="nav-panel" id="nav-panel" aria-hidden="true">
    <nav aria-label="Mobile"><ul>{panel_links}</ul></nav>
    <div class="btn-row">{btn("Get Started", "/contact#schedule", "primary", "mobilenav_get_started", arrow=True)}{btn("Request Information", "/contact#request", "ghost", "mobilenav_request_info")}</div>
    <p class="panel-meta"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
  </div>
</header>
<main id="main" tabindex="-1">
{body}
</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="footer-brand" href="/" aria-label="Spektric LLC — home">
          <img src="/assets/img/spektric-mark-160.png" alt="" width="46" height="46">
          <span class="brand-text"><span class="brand-word">Spektric<span class="llc">LLC</span></span><span class="brand-sub">ABA · Neurology · Psychotherapy</span></span>
        </a>
        <p class="footer-tag">Care built around the individual — for children, adolescents, and adults, and the people who support them.</p>
      </div>
      <div>
        <h2>Services</h2>
        <ul><li><a href="/aba-services">ABA Services</a></li><li><a href="/mental-health">Mental Health</a></li><li><a href="/neurology">Neurology &amp; Evaluation</a></li><li><a href="/who-we-serve">Who We Serve</a></li></ul>
      </div>
      <div>
        <h2>Spektric</h2>
        <ul><li><a href="/about">About Spektric</a></li><li><a href="/resources/">Resources</a></li><li><a href="/faq">Questions &amp; Answers</a></li><li><a href="/contact">Contact</a></li></ul>
      </div>
      <div>
        <h2>Contact</h2>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{ph("PHONE NUMBER")}</li>
          <li>{ph("ADDRESS / SERVICE AREA")}</li>
          <li>{ph("HOURS OF OPERATION")}</li>
        </ul>
      </div>
    </div>
    <div class="footer-notice">
      <p>{EMERGENCY}</p>
      <p>Information on this website is educational and general in nature. It is not a substitute for individualized clinical assessment, diagnosis, or treatment.</p>
    </div>
    <div class="footer-bottom">
      <p>&copy; <span data-year>{YEAR}</span> Spektric LLC. All rights reserved.</p>
      <ul><li><a href="/privacy">Privacy Policy</a></li><li><a href="/terms">Terms of Use</a></li><li><a href="/accessibility">Accessibility</a></li><li>{ph("NOTICE OF PRIVACY PRACTICES LINK")}</li></ul>
    </div>
  </div>
</footer>
<div class="mobile-cta" aria-label="Quick actions">
  {btn("Request Information", "/contact#request", "ghost", "sticky_request_info")}
  {btn("Get Started", "/contact#schedule", "primary", "sticky_get_started")}
</div>
<script src="/assets/js/config.js"></script>
<script src="/assets/js/main.js" defer></script>
</body>
</html>
"""


# ---------- Visual components ----------

SPECTRUM = ["#8B3FE4", "#E23C8F", "#F7744F", "#F5C83A", "#7AC142", "#17B39C", "#22B5E5", "#2B72D9"]


def hero_art(mobile=False):
    """Flowing spectrum ribbons with nodes — the home hero signature."""
    grad = "".join(f'<stop offset="{i/7:.3f}" stop-color="{c}"/>' for i, c in enumerate(SPECTRUM))
    # Starts below/left of the headline block, rises through the right half.
    base = "M -120 905 C 470 895, 780 740, 955 450 S 1250 130, 1580 235"
    ribbons = []
    spec = [(0, 48, .26, True), (0, 2.2, .95, False), (-28, 1.4, .55, False), (-56, 1, .35, False), (30, 1.4, .55, False), (60, 1, .32, False), (96, .8, .2, False), (-90, .8, .2, False)]
    for dy, w, op, blur in spec:
        f = ' filter="url(#glow)"' if blur else ""
        ribbons.append(f'<path d="{base}" transform="translate(0 {dy})" fill="none" stroke="url(#sp)" stroke-width="{w}" stroke-opacity="{op}" stroke-linecap="round"{f}/>')
    seg = ((-120, 905), (470, 895), (780, 740), (955, 450))
    seg2 = ((955, 450), (1130, 160), (1250, 130), (1580, 235))
    pts = []
    for t, r in [(.58, 4), (.72, 3.5), (.86, 6), (1.0, 4)]:
        x, y = bezier(*seg, t); pts.append((x, y, r))
    for t, r in [(.28, 4.5), (.55, 5.5), (.8, 3.5)]:
        x, y = bezier(*seg2, t); pts.append((x, y, r))
    nodes = "".join(f'<circle class="node" cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="#FBFAF6"/>' for x, y, r in pts)
    halos = "".join(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r*4}" fill="#FBFAF6" opacity=".06"/>' for x, y, r in pts)
    par = "xMidYMid meet" if mobile else "xMidYMid slice"
    uid = "m" if mobile else "d"
    return f'''<svg viewBox="0 0 1440 820" preserveAspectRatio="{par}" aria-hidden="true" focusable="false">
<defs><linearGradient id="sp-{uid}" x1="0" x2="1" y1="0" y2="0">{grad}</linearGradient>
<filter id="glow-{uid}" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="26"/></filter></defs>
<g class="drift">{ribbons[0].replace("url(#sp)", f"url(#sp-{uid})").replace("url(#glow)", f"url(#glow-{uid})")}</g>
<g class="drift drift-2">{"".join(ribbons[1:5]).replace("url(#sp)", f"url(#sp-{uid})")}</g>
<g class="drift drift-3">{"".join(ribbons[5:]).replace("url(#sp)", f"url(#sp-{uid})")}{halos}{nodes}</g>
</svg>'''


ORBIT_ITEMS = ["Strengths", "Communication", "Environment", "Relationships", "Emotional needs", "Developmental needs", "Functional skills", "Goals", "Family & support"]


def orbit():
    n = len(ORBIT_ITEMS)
    r = 37
    nodes, lines = [], []
    colors = SPECTRUM + [SPECTRUM[0]]
    for i, label in enumerate(ORBIT_ITEMS):
        ang = -math.pi / 2 + i * 2 * math.pi / n
        x, y = 50 + r * math.cos(ang), 50 + r * math.sin(ang)
        lines.append(f'<line x1="50" y1="50" x2="{x:.2f}" y2="{y:.2f}"/>')
        side = "is-left" if x < 45 else ("is-right" if x > 55 else "")
        nodes.append(f'<li class="orbit-node {side}" style="left:{x:.2f}%;top:{y:.2f}%;--c:{colors[i]}"><i aria-hidden="true"></i><span>{label}</span></li>')
    svg = f'<svg class="orbit-lines" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true"><g stroke="#CFCBC0" stroke-width=".35" vector-effect="non-scaling-stroke">{"".join(lines)}</g><circle cx="50" cy="50" r="{r}" fill="none" stroke="#DAD6CB" stroke-width=".3" stroke-dasharray="1 1.2"/></svg>'
    chips = "".join(f'<li class="chip" style="--c:{colors[i]}">{l}</li>' for i, l in enumerate(ORBIT_ITEMS))
    return (f'<div class="orbit" role="img" aria-label="The person at the center, surrounded by what we consider: {", ".join(ORBIT_ITEMS)}">'
            f'{svg}<ul>{"".join(nodes)}</ul><div class="orbit-center">The<br>person</div></div>'
            f'<div class="orbit-fallback"><p class="small" style="margin-bottom:.75rem"><strong>The person</strong>, understood through:</p><ul class="chips">{chips}</ul></div>')


def bezier(p0, p1, p2, p3, t):
    u = 1 - t
    return (u**3*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t**3*p3[0], u**3*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t**3*p3[1])


PATHWAY_STEPS = [("Assessment", "Understand the person, the context, and what matters"), ("Individualized plan", "Goals chosen with the family, not a checklist"),
                 ("Intervention", "Teaching that fits the learner and the setting"), ("Measurement", "Meaningful data, reviewed continuously"),
                 ("Adjustment", "Plans change when the data say they should"), ("Generalization", "Skills carried into real life and new settings"),
                 ("Progress", "Outcomes that matter to the person and family")]


def _wrap(text, width=26):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur: lines.append(cur)
    return lines[:2]


def pathway():
    """Gentle spectrum pathway with 7 nodes; labels alternate above/below and clear the curve (ABA page)."""
    seg1 = ((30, 175), (190, 110), (330, 110), (500, 160))
    seg2 = ((500, 160), (670, 210), (810, 210), (970, 135))
    def curve(t):
        return bezier(*seg1, t * 2) if t <= .5 else bezier(*seg2, (t - .5) * 2)
    samples = [curve(k / 400) for k in range(401)]
    d = f"M {seg1[0][0]} {seg1[0][1]} C {seg1[1][0]} {seg1[1][1]}, {seg1[2][0]} {seg1[2][1]}, {seg1[3][0]} {seg1[3][1]} C {seg2[1][0]} {seg2[1][1]}, {seg2[2][0]} {seg2[2][1]}, {seg2[3][0]} {seg2[3][1]}"
    grad = "".join(f'<stop offset="{i/7:.3f}" stop-color="{c}"/>' for i, c in enumerate(SPECTRUM))
    nodes = []
    n = len(PATHWAY_STEPS)
    for i, (title, sub) in enumerate(PATHWAY_STEPS):
        x, y = curve(i / (n - 1))
        above = i % 2 == 0
        anchor = "start" if i == 0 else ("end" if i == n - 1 else "middle")
        lines = _wrap(sub)
        w = max(len(title) * 10.5, max(len(l) for l in lines) * 6.4)
        x0, x1 = (x, x + w) if anchor == "start" else ((x - w, x) if anchor == "end" else (x - w / 2, x + w / 2))
        ys = [py for px, py in samples if x0 - 6 <= px <= x1 + 6] or [y]
        if above:
            bottom = min(ys) - 18
            sy = [bottom - 14 * (len(lines) - 1 - k) for k in range(len(lines))]
            ty = sy[0] - 21
        else:
            ty = max(ys) + 32
            sy = [ty + 19 + 14 * k for k in range(len(lines))]
        subs = "".join(f'<text x="{x:.1f}" y="{yy:.1f}" text-anchor="{anchor}" font-family="Albert Sans, system-ui, sans-serif" font-size="12" fill="#4F5566">{l}</text>' for yy, l in zip(sy, lines))
        nodes.append(f'<g class="path-node"><circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="#0B0C12" stroke="#FBFAF6" stroke-width="3"/>'
                     f'<text x="{x:.1f}" y="{ty:.1f}" text-anchor="{anchor}" font-family="Fraunces, Georgia, serif" font-size="19" font-weight="500" fill="#0B0C12">{title}</text>{subs}</g>')
    lst = "".join(f'<li>{t}<span>{s}</span></li>' for t, s in PATHWAY_STEPS)
    return (f'<svg class="pathway" viewBox="0 0 1000 330" aria-hidden="true" focusable="false"><defs><linearGradient id="pg" x1="0" x2="1" y1="0" y2="0">{grad}</linearGradient></defs>'
            f'<path class="path-line" d="{d}" fill="none" stroke="url(#pg)" stroke-width="3" stroke-linecap="round"/>{"".join(nodes)}</svg>'
            f'<div class="pathway-list"><ol>{lst}</ol></div>'
            f'<p class="visually-hidden">The pathway: {"; then ".join(t for t, _ in PATHWAY_STEPS)}.</p>')


def steps(items):
    out = []
    for i, (title, text) in enumerate(items, 1):
        out.append(f'<li class="step"><div class="step-num" aria-hidden="true">{i:02d}</div><h3>{title}</h3><p>{text}</p></li>')
    return f'<ol class="steps reveal-stagger">{"".join(out)}</ol>'
