# bigsplash.church

The Big Splash church page as its own site. GitHub Pages serves this folder at https://bigsplash.church.

## Where to edit

Until the old address (bigsplash.video/church) redirects here, edit the page in `~/Desktop/BigsplashWeb_VIdeoONLY/church` and run:

    python3 sync_from_main_site.py

Then commit and push this folder. After the redirect is on, edit the files here directly and delete the sync script.

## DNS (GoDaddy)

- A record, host `@`, value `185.199.108.153`
- A record, host `@`, value `185.199.109.153`
- A record, host `@`, value `185.199.110.153`
- A record, host `@`, value `185.199.111.153`
- CNAME record, host `www`, value `christopherlist-lab.github.io`

Remove GoDaddy's parked A record on `@` first.
