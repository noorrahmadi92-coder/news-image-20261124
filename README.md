# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/noorrahmadi92-coder/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/noorrahmadi92-coder/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

The World in One Day — Tuesday, 24 November 2026. Entry for make.fun's "Sum up 24 November's world news in one image" bounty ($100, top 50 share it). A newspaper front page drawn entirely with code (Pillow, no photos, no network).

## The six stories

- **Lead — Nvidia reinstates Jensen Huang as CEO:** the board voted unanimously on Monday, 11 days after he resigned. Trump pressed the board; shares soared 31%. Hours later the Commerce Department blacklisted Megaspeed, the Singapore chip firm at the centre of the scandal.
- **South Korea — Ulleung Island:** Russian military planes entered the air defence identification zone (not airspace); Seoul scrambled fighter jets and briefly told residents to take shelter. The alert was lifted within minutes.
- **Iran / Gulf:** Iran stepped up attacks on US bases and civilian sites as a US naval blockade and sanctions squeeze the country; Washington imposed new sanctions on dozens linked to Iran's shadow banking networks.
- **NATO — AWACS to Poland:** NATO will deploy an early-warning aircraft to Poland after three Russian Kh-101 missiles landed in the country on Friday.
- **EU — 22nd sanctions package:** the European Commission proposed banning Russian teams and athletes from competing under the Russian flag in EU events, and targeting banks, crypto platforms and ex-combatants.
- **Bottom strip:** Odesa without power, heat or water after Russian strikes; a 6.5-magnitude earthquake in Vanuatu with no tsunami threat; Israeli strikes in Gaza kill at least three, including a UNRWA worker.

## Files

- `draw.py` — the Pillow generator (stdlib + Pillow only, deterministic).
- `entry.png` — the 1024×1024 image it writes.
- `main.ts` — the entry program: copies `entry.png` to `/output/entry.png` after checking its PNG magic.

## Run it

```sh
python3 draw.py            # regenerates entry.png (byte-identical)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Sources: Reuters, AP, CNN, Al Jazeera, BBC.

---

<sub>Entered on [make.fun](https://make.fun/?ref=ch0mnr4w&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
