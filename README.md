# bigsplash.church

The Big Splash church page as its own site. GitHub Pages serves this folder at https://bigsplash.church.

## Where to edit

Edit the files in this folder, then commit and push. Since Nov 14, 2026, bigsplash.video/church/ (plus /church/thanks/ and /church/christmas/) redirects here, so the old sync script from the main site repo is gone. The `church/` folder in `~/Desktop/BigsplashWeb_VIdeoONLY` is no longer the source for these pages.

Keep `google3ec98a98707c1572.html` (Google Search Console verification) and `facd856bef3fa30b0cb9f77965374989.txt` (IndexNow key for Bing) at the root.

## DNS (GoDaddy)

- Delete every A record on `@` that GoDaddy put there (parking, shown as one row or two). If it refuses, turn off Forwarding first.
- A record, host `@`, value `185.199.108.153`
- A record, host `@`, value `185.199.109.153`
- A record, host `@`, value `185.199.110.153`
- A record, host `@`, value `185.199.111.153`
- Edit the existing `www` CNAME so its value is `christopherlist-lab.github.io`
