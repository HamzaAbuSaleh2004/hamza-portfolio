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

## Deploy (Render)
Start command: `gunicorn portfolio_app:app`
