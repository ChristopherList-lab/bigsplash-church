# Reel Safe Zones

**Purpose:** Claude checks that the words on your Reel stay clear of the buttons and captions Instagram, TikTok and YouTube Shorts lay over your video.

From Big Splash (bigsplash.church). Free to use and share. Change it to fit your church. Our team gathered these numbers on Oct 20, 2026. Apps change their screens, so check again every few months.

## Set it up

1. Add this file to a Claude project.
2. Before you export a Reel, list the words on each text card and where each one sits on screen. Or attach a screenshot of each card.
3. Ask Claude to check them, and move anything it flags.
4. Watch the finished Reel full screen on a phone before you post. A person gives the final OK.

## The safe box

One box clears all three apps. On a 1080 x 1920 video (9:16):

- Keep text, logos, faces and buttons between x 140 and x 860, and between y 400 and y 1228.
- From y 820 down, also stay left of x 760. TikTok's buttons sit there.

The same box in percentages, for apps like Canva or CapCut:

- Leave the top 21% clear.
- Leave the bottom 36% clear.
- Leave 13% clear on the left.
- Leave 20% clear on the right, and 30% on the right from 43% of the way down to the bottom.

## The covered areas, app by app (1080 x 1920)

| App | Top | Bottom | Left and right edges | Buttons on the right |
|---|---|---|---|---|
| Instagram Reels | 269 px: status bar, Reels tabs, camera | 672 px: profile, caption, audio | 65 px each side | 160 px wide from y 720 down, 230 px from y 1152 down |
| TikTok | 240 px: tabs, search, LIVE | 660 px: username, caption, sound | 120 px each side (some phones crop) | 300 px wide from y 840 down |
| YouTube Shorts | 288 px in Google's ad guide, 380 px measured in the app | 672 px: channel, Subscribe, title | 48 to 60 px on the left | 192 to 201 px wide, full height |

Each app publishes numbers for ads only. We compared them with measurements of regular posts and kept the larger number on each edge.

Sources: Meta Ads Guide, Instagram Reels video specs. TikTok Ads Help, In-Feed ad templates. Google Ads Help, "Universal safe zones for video ads on YouTube." AdCheckLab, TikTok and YouTube Shorts measurements (2026). reelsafezone.com, Instagram button rail.

The box doesn't cover two cases:

- Paid extras. An Instagram ad with a disclaimer or a TikTok Shop card covers more of the bottom.
- Long captions. Every app spreads the caption over the video once someone taps "more."

## Covers in the profile grid

Your Reel cover is a 1080 x 1920 frame. Instagram's profile grid shows a 3:4 crop, about y 240 to 1680, and TikTok's grid comes close to that. Cover text inside the safe box survives both.

## Two more rules

- Don't shrink the video or add bars to make room for words. Instagram lists Reels that "contain borders" among the ones it shows less. Move the words or cut them.
- Post your original file to each app. A download from another app carries that app's watermark, and Instagram says it shows watermarked Reels less.

Source: Instagram, "Instagram Ranking Explained" (May 31, 2023), about.instagram.com/blog/announcements/instagram-ranking-explained

---

## Instructions for Claude

Check each text card in my Reel against the safe box and the app table above. I'll give you a list of cards with their positions, or screenshots.

- For each card, say Clear or Breaks. If it breaks, name the app and the part of the screen it runs into, like "TikTok's button column."
- Suggest a new spot inside the safe box, in pixels on a 1080 x 1920 frame and in plain words, like "move it up to the middle of the screen."
- Watch the lower right. From y 820 down, text must end left of x 760.
- Flag any card with more than 8 words.
- With screenshots, scale them to 1080 x 1920 first. Say your positions are estimates and tell me to confirm on a phone.
- Don't suggest shrinking the video or adding borders.

---

## Prompt to copy

> Using the safe zones in reel-safe-zones.md, check the text cards below for Instagram Reels, TikTok and YouTube Shorts. Flag any line under buttons or captions, and any card over 8 words. Suggest a new spot for each one that breaks. Cards: [paste each card's words and where it sits, or attach screenshots].

## Examples

Both came from a check of our own Reels.

> End card, mission line: Breaks. It ends at y 1300, which puts it 52 px into the caption area on Instagram and YouTube and 40 px into TikTok's. Move it up so it ends by y 1228.

> End card, "Link in bio": Breaks. It reaches x 780, 20 px into TikTok's button column. Move it left so it ends before x 760.
