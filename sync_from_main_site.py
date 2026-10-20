#!/usr/bin/env python3
"""Rebuild this standalone church site from the main Big Splash repo.

Until bigsplash.church is live, the church pages are edited in
~/Desktop/BigsplashWeb_VIdeoONLY/church and this script copies them here with the
paths adjusted for a site that lives at the domain root: the church page, the old
thanks page and the founding pages (church/founding/: checkout, terms, welcome).

    python3 sync_from_main_site.py

After the old address redirects here, edit the files in this folder directly
and delete this script.
"""
import re, shutil, sys
from pathlib import Path

SRC = Path.home() / 'Desktop' / 'BigsplashWeb_VIdeoONLY'
OUT = Path(__file__).resolve().parent
DOMAIN = 'https://bigsplash.church'
MAIN = 'https://bigsplash.video'

def must(text, old, new, label):
    if old not in text:
        sys.exit(f'sync: expected to find {label!r} in the source page')
    return text.replace(old, new)

def main_site_links(text):
    # /church/ is this site's home page. Other root-relative links (/frontdoor/, /privacy/)
    # live on the main site, so point them there.
    text = re.sub(r'''((?:src|href|poster)=["'])/church/''', rf'\1{DOMAIN}/', text)
    text = re.sub(r'''((?:src|href|poster)=["'])/(?!/)''', rf'\1{MAIN}/', text)
    return re.sub(r'''(content=["']\d+;\s*url=)/(?!/)''', rf'\1{MAIN}/', text)

# ---- home page ----
s = (SRC / 'church' / 'index.html').read_text()
s = main_site_links(s.replace('../assets/', 'assets/').replace('../ADs/', 'ADs/').replace('../js/intake.js', 'js/intake.js'))
# The source page may already point at bigsplash.church.
s = s.replace('<link rel="canonical" href="https://bigsplash.video/church/">', f'<link rel="canonical" href="{DOMAIN}/">')
if f'<link rel="canonical" href="{DOMAIN}/">' not in s:
    sys.exit('sync: expected a canonical link in the source page')
s = s.replace('<meta property="og:url" content="https://bigsplash.video/church/">', f'<meta property="og:url" content="{DOMAIN}/">')
s = must(s, 'https://bigsplash.video/assets/images/og-image.jpg', f'{DOMAIN}/assets/images/og-image.jpg', 'og:image')
s = must(s, '"url": "https://bigsplash.video", "email"', f'"url": "{DOMAIN}", "email"', 'JSON-LD url')
(OUT / 'index.html').write_text(s)

# ---- thank-you page ----
t = (SRC / 'church' / 'thanks' / 'index.html').read_text()
t = main_site_links(t.replace('../../assets/', '../assets/'))
(OUT / 'thanks').mkdir(exist_ok=True)
(OUT / 'thanks' / 'index.html').write_text(t)

# ---- founding church pages: checkout, terms and the welcome page after Stripe ----
# church/founding/ in the main repo becomes founding/ here, one folder closer to the root.
FOUNDING = ('founding/index.html', 'founding/terms/index.html', 'founding/welcome/index.html')
founding = {}
for name in FOUNDING:
    src = SRC / 'church' / name
    if not src.exists():
        sys.exit(f'sync: church/{name} is missing in the main repo')
    up = '../' * name.count('/')  # how far this page sits below the site root here
    f = src.read_text().replace(f'../{up}assets/', f'{up}assets/').replace(f'../{up}js/intake.js', f'{up}js/intake.js')
    f = main_site_links(f.replace('https://bigsplash.video/church/', f'{DOMAIN}/'))
    founding[name] = f
    (OUT / name).parent.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(f)

# Stripe sends the pastor back to <origin>/church/founding/... (the worker builds those links from the
# page's origin). These two stubs forward that path here to /founding/..., keeping ?session= and ?canceled=1.
STUB = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="robots" content="noindex"><title>Big Splash</title>
<script>location.replace('{to}' + location.search);</script>
<meta http-equiv="refresh" content="0;url={to}"></head>
<body style="background:#f8f5ee;font-family:sans-serif"><p><a href="{to}">Continue</a></p></body></html>
"""
for old, to in (('church/founding/index.html', '/founding/'), ('church/founding/welcome/index.html', '/founding/welcome/')):
    (OUT / old).parent.mkdir(parents=True, exist_ok=True)
    (OUT / old).write_text(STUB.replace('{to}', to))

# ---- shared script and the assets the pages use ----
(OUT / 'js').mkdir(exist_ok=True)
shutil.copy2(SRC / 'js' / 'intake.js', OUT / 'js' / 'intake.js')
pages = s + t + ''.join(founding.values())
refs = set(re.findall(r'''(?:src|href|poster)=["'](?:\.\./)*((?:assets|ADs)/[^"'?#]+)''', pages))
refs |= set(re.findall(r'''url\(['"]?(?:\.\./)*(assets/[^'")]+)''', pages))
refs.add('assets/images/og-image.jpg')
for r in sorted(refs):
    src = SRC / r
    if not src.exists():
        sys.exit(f'sync: {r} is referenced by the page but missing in the main repo')
    dst = OUT / r
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)

# ---- checks ----
problems = []
for name, text in [('index.html', s), ('thanks/index.html', t)] + list(founding.items()):
    base = (OUT / name).parent
    for m in re.finditer(r'''(?:src|href|poster)=["']([^"']+)["']''', text):
        u = m.group(1)
        if re.match(r'^(https?:|mailto:|tel:|#|data:|javascript:)', u) or u in ('./', '../'):
            continue
        target = (base / u.split('?')[0].split('#')[0]).resolve()
        if OUT not in target.parents and target != OUT:
            problems.append(f'{name}: {u} points outside the site')
        elif not target.exists():
            problems.append(f'{name}: {u} does not exist')
    if 'bigsplash.video/church' in text:
        problems.append(f'{name}: still mentions bigsplash.video/church')
if problems:
    sys.exit('sync: ' + '; '.join(problems))
print(f'synced: index.html, thanks/index.html, {", ".join(FOUNDING)}, js/intake.js, {len(refs)} assets')
