#!/usr/bin/env python3
"""Rebuild this standalone church site from the main Big Splash repo.

Until bigsplash.church is live, the church page is edited in
~/Desktop/BigsplashWeb_VIdeoONLY/church and this script copies it here with the
paths adjusted for a site that lives at the domain root.

    python3 sync_from_main_site.py

After the old address redirects here, edit the files in this folder directly
and delete this script.
"""
import re, shutil, sys
from pathlib import Path

SRC = Path.home() / 'Desktop' / 'BigsplashWeb_VIdeoONLY'
OUT = Path(__file__).resolve().parent
DOMAIN = 'https://bigsplash.church'

def must(text, old, new, label):
    if old not in text:
        sys.exit(f'sync: expected to find {label!r} in the source page')
    return text.replace(old, new)

# ---- home page ----
s = (SRC / 'church' / 'index.html').read_text()
s = s.replace('../assets/', 'assets/').replace('../js/intake.js', 'js/intake.js')
s = must(s, '<link rel="canonical" href="https://bigsplash.video/church/">', f'<link rel="canonical" href="{DOMAIN}/">', 'canonical')
s = must(s, '<meta property="og:url" content="https://bigsplash.video/church/">', f'<meta property="og:url" content="{DOMAIN}/">', 'og:url')
s = must(s, 'https://bigsplash.video/assets/images/og-image.jpg', f'{DOMAIN}/assets/images/og-image.jpg', 'og:image')
s = must(s, '"url": "https://bigsplash.video", "email"', f'"url": "{DOMAIN}", "email"', 'JSON-LD url')
(OUT / 'index.html').write_text(s)

# ---- thank-you page ----
t = (SRC / 'church' / 'thanks' / 'index.html').read_text()
t = t.replace('../../assets/', '../assets/')
(OUT / 'thanks').mkdir(exist_ok=True)
(OUT / 'thanks' / 'index.html').write_text(t)

# ---- shared script and the assets the two pages use ----
(OUT / 'js').mkdir(exist_ok=True)
shutil.copy2(SRC / 'js' / 'intake.js', OUT / 'js' / 'intake.js')
refs = set(re.findall(r'''(?:src|href)=["'](?:\.\./)?(assets/[^"'?#]+)''', s + t))
refs |= set(re.findall(r'''url\(['"]?(?:\.\./)?(assets/[^'")]+)''', s + t))
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
for name, text in (('index.html', s), ('thanks/index.html', t)):
    base = (OUT / name).parent
    for m in re.finditer(r'''(?:src|href)=["']([^"']+)["']''', text):
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
print(f'synced: index.html, thanks/index.html, js/intake.js, {len(refs)} assets')
