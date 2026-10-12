# bigsplash.church

The Big Splash church page as its own site. GitHub Pages serves this folder at https://bigsplash.church.

## Where to edit

Until the old address (bigsplash.video/church) redirects here, edit the page in `~/Desktop/BigsplashWeb_VIdeoONLY/church` and run:

    python3 sync_from_main_site.py

Then commit and push this folder. After the redirect is on, edit the files here directly and delete the sync script.

## DNS (GoDaddy)

- Delete every A record on `@` that GoDaddy put there (parking, shown as one row or two). If it refuses, turn off Forwarding first.
- A record, host `@`, value `185.199.108.153`
- A record, host `@`, value `185.199.109.153`
- A record, host `@`, value `185.199.110.153`
- A record, host `@`, value `185.199.111.153`
- Edit the existing `www` CNAME so its value is `christopherlist-lab.github.io`
