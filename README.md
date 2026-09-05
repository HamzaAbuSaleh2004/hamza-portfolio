# Hamza Abu Saleh — Portfolio v3.0

A monochrome, editorial, interactive portfolio. Near-black canvas, bone-white
type, a single electric-lime accent. Fullscreen video hero with auto-scroll,
custom cursor, cursor-following project previews, marquees, and live Credly
certification badges.

## Run locally

```bash
pip install -r requirements.txt
python portfolio_app.py
# open http://localhost:5000
```

## Structure

```
portfolio_app.py            Flask app + PERSONAL_INFO
projects_data.py            PROJECTS, CATEGORIES, CERTIFICATIONS (Credly badge IDs)
templates/
  portfolio_base.html       Shell: nav, preloader, footer
  portfolio_home.html       Hero, about, experience, work, skills, certs, contact
  portfolio_projects.html   Filterable project index
  portfolio_project_detail.html
static/
  css/portfolio.css         Monochrome design system
  js/portfolio.js           Motion engine (cursor, hero video, filters, lightbox)
  media/                    hero-1080.mp4 / hero-720.mp4 / hero-poster.jpg
  images/                   profile + project screenshots
```

## Notes
- The hero video was re-encoded from the source 4K/33 MB clip to 1080p (~4.8 MB)
  and 720p (~2.1 MB) with a JPG poster.
- Certification badges are live Credly embeds; the Digital Leader badge is shown
  first, followed by the Google Cloud skill badges.

## Work Showcase page (unlisted)

A page for sharing with employers and clients. **Nothing on the public site links to
it** — no nav item, no footer link, no sitemap entry.

```
/work-showcase
```

- Sends `noindex, nofollow, noarchive` as both a meta tag and an `X-Robots-Tag` header
- `robots.txt` disallows `/work-showcase`
- `Referrer-Policy: no-referrer`, so the URL doesn't leak through outbound clicks
- **No passcode, by design.** Anyone with the URL can open it and forward it.

Change the path with an env var if you ever want to:

```bash
REEL_SLUG=some-other-path
```

Contents: the 92-second showreel (feature, captioned, sound on) plus the two full
**narrated** walkthroughs — the RFP system (3:20) and Baladiya (2:59). Copy lives in
`portfolio_app.py` → `REEL`; layout in `templates/portfolio_reel.html`; styles in
`static/css/reel.css`.

## Deploy (Render)
Start command: `gunicorn portfolio_app:app`

⚠️ `static/media/` is now **~56 MB** (three demo videos). That's fine to serve, but
committing it to git will bloat the repo permanently. Consider Git LFS, or host the
three demo MP4s in a bucket / CDN and point the `src` values in `REEL` at those URLs.
