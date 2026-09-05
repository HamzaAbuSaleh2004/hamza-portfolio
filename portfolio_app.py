"""
Hamza Abu Saleh — Portfolio v3.0
Monochrome, editorial, interactive Flask portfolio.

Self-contained: run `python portfolio_app.py` then open http://localhost:5000
"""
import os

from flask import (
    Flask, render_template, request, redirect, url_for, send_from_directory, abort,
    Response
)

from projects_data import (
    get_all_projects, get_project, get_featured_projects,
    get_category_counts, CATEGORY_LABELS, CERTIFICATIONS,
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "hamza-portfolio-v3-secret")

# ==================== WORK SHOWCASE (unlisted) ====================
# Lives at /work-showcase. Nothing on the public site links here, the page sends
# noindex, and robots.txt disallows it. Deliberately no passcode: anyone holding
# the URL can open it and pass it on.
# Change the path with the REEL_SLUG env var if you ever want a different one.
REEL_SLUG = os.environ.get("REEL_SLUG", "work-showcase")

# Canonical origin, used for the sitemap reference in robots.txt.
SITE_ORIGIN = os.environ.get("SITE_ORIGIN", "https://hamza-portfolio-rk8n.onrender.com")

REEL = {
    "feature": {
        "title": "AI Engineering Showreel",
        "runtime": "1:32",
        "src": "media/showreel-v3.mp4",
        "poster": "media/poster-showreel.jpg",
        "blurb": (
            "A 90-second pass over the work: a live Gemini agent in production, an "
            "18-agent procurement system, computer vision routing municipal work orders, "
            "and the data-science layer underneath."
        ),
    },
    "demos": [
        {
            "num": "01",
            "title": "Multi-Agent Procurement / RFP System",
            "short": "Multi-Agent RFP System",   # fits the narrow player label
            "runtime": "3:20",
            "src": "media/rfp-demo.mp4",
            "poster": "media/poster-rfp.jpg",
            "tags": ["Google ADK", "Gemini", "FastAPI", "Cloud Run", "PostgreSQL", "MCP"],
            "blurb": (
                "The full walkthrough of the hierarchical agent system — 18 specialist "
                "agents across six teams, orchestrated by a director agent."
            ),
            "watch_for": [
                "Live agent handoff — the ACTIVE AGENT panel switches from RFP Director to "
                "RFP Creator, with the tool trace showing transfer_to_agent and read_local_templates",
                "The integrations rail: Firecrawl, FMP, Drive, Slack, PDF generation, P(Win) scoring",
                "Vendor scoring and the risk heatmap, ending in an award decision",
                "The agent answering live inside Gemini Enterprise",
            ],
        },
        {
            "num": "02",
            "title": "Baladiya — Civic Reporting with Vertex AI",
            "short": "Baladiya — Vertex AI Vision",   # fits the narrow player label
            "runtime": "2:59",
            "src": "media/baladiya-demo.mp4",
            "poster": "media/poster-baladiya.jpg",
            "tags": ["YOLOv8", "Vertex AI", "Gemini Vision", "React", "FastAPI", "Cloud Run"],
            "blurb": (
                "A resident photographs a municipal problem; the system reads the image, "
                "removes duplicates, and routes a work order to the right department."
            ),
            "watch_for": [
                "Photo to structured report — category, severity, and street extracted from the image alone",
                "The ticket routing itself to Roads & Infrastructure with an SLA date attached",
                "Role-scoped admin dashboards per department",
                "Geographic clustering across Doha, which is what suppresses duplicate reports",
            ],
        },
    ],
}

# ==================== PERSONAL INFO (from CV) ====================
PERSONAL_INFO = {
    "name": "Hamza Abu Saleh",
    "role": "AI Engineer",
    "headline": "B.Sc. Data Science & AI graduate · Cloud AI Engineer @ LiverX · building production multi-agent systems on Google Cloud.",
    "location": "Amman, Jordan",
    "email": "hamzaabusaleh04@gmail.com",
    "phone": "+962 77 806 4473",
    "linkedin": "https://www.linkedin.com/in/hamza-abu-saleh-9572b7242/",
    "github": "#",
    "objective": (
        "Data Science & AI graduate and Cloud AI Engineer specializing in production "
        "multi-agent systems, computer vision, and GCP deployments — building real-world, "
        "high-impact intelligent systems through research-driven engineering."
    ),
    "roles": [
        "AI Engineer",
        "Cloud AI Engineer @ LiverX",
        "Multi-Agent Systems",
        "Computer Vision & NLP",
        "Co-Founder — Madmoon (FinTech)",
        "Google Cloud Digital Leader",
    ],
    "education": {
        "degree": "B.Sc. Data Science & Artificial Intelligence",
        "institution": "Hussein Technical University (HTU)",
        "period": "2022 – 2026",
        "gpa": "3.63 / 4.00",
        "graduated": "Graduated Sept 2026",
        "note": "Excellence · Google Cloud Digital Leader — Certified",
    },
    "experience": [
        {
            "title": "Cloud AI Engineer Trainee",
            "organization": "LiverX — Google Cloud Partner",
            "period": "2025 – Present",
            "responsibilities": [
                "Built and deployed production multi-agent AI systems on Google Cloud (ADK + Gemini, Cloud Run, Vertex AI, PostgreSQL) as sole developer, shipping client-facing solutions for enterprise and public-sector users across the MENA region.",
                "Engineered a data-loss-prevention layer (Sensitive Data Protection + Model Armor) that blocks national-ID leakage via a custom 11-digit regex infoType, keeping AI responses compliance-ready.",
                "Packaged complex systems for non-technical audiences — producing bilingual technical documentation and a branded AI-generated video suite for a flagship cloud-technology summit booth.",
            ],
        },
        {
            "title": "Co-Founder & Team Lead",
            "organization": "Madmoon — FinTech Escrow (Rocket Pitch, INJAZ)",
            "period": "2025",
            "responsibilities": [
                "Co-founded a third-party escrow FinTech for secure online transactions, placing top 4 of 100+ teams and securing INJAZ incubation.",
                "Led the team through ideation, market research, and prototype development.",
            ],
        },
        {
            "title": "Volunteer Team Leader",
            "organization": "Invent for the Planet 2025 — HTU",
            "period": "Feb 2025",
            "responsibilities": [
                "Coordinated volunteer teams across a global innovation event spanning 24 countries and 51 universities.",
                "Liaised with mentors, faculty, and participants to ensure smooth end-to-end execution.",
            ],
        },
        {
            "title": "Student Volunteer & Gifted Student Support",
            "organization": "Deanship of Student Affairs — HTU",
            "period": "Feb 2025 – Jul 2025",
            "responsibilities": [
                "Supported student engagement and fostered leadership through club, team, and event coordination while balancing academic commitments.",
            ],
        },
    ],
    "skills": {
        "technical": [
            "Python", "PyTorch", "TensorFlow", "Google ADK", "Vertex AI", "Gemini API",
            "YOLOv8", "Computer Vision", "Machine Learning", "Deep Learning", "FastAPI",
            "React", "Firebase / Firestore", "Cloud Run", "Docker & CI/CD",
            "PostgreSQL / SQL", "JavaScript", "Tailwind", "HTML / CSS",
        ],
        "soft": [
            "Team Leadership", "Project Coordination", "Innovation & Problem-Solving",
            "Technical Documentation", "Adaptability",
        ],
    },
    "achievements": [
        "4th of 100+ teams — Rocket Pitch Startup Competition (2025); secured INJAZ incubation for Madmoon.",
        "Leadership recognition — Invent for the Planet 2025 (global, 24 countries).",
        "Google Cloud Digital Leader — Certified (2026).",
    ],
    "metrics": [
        {"value": "3.63", "unit": "GPA", "label": "Excellence @ HTU", "decimals": 2},
        {"value": "8", "unit": "+", "label": "AI / ML systems built", "decimals": 0},
        {"value": "4", "unit": "th", "label": "of 100+ startup teams", "decimals": 0, "prefix": ""},
        {"value": "24", "unit": "", "label": "countries — IFTP 2025", "decimals": 0},
    ],
}


# ==================== PORTFOLIO ROUTES ====================
@app.route("/")
def home():
    featured = get_featured_projects(3)
    return render_template(
        "portfolio_home.html",
        personal=PERSONAL_INFO,
        featured_projects=featured,
        certifications=CERTIFICATIONS,
    )


@app.route("/projects")
def projects():
    # Render every project; filtering is handled client-side for smooth motion.
    category = request.args.get("category", "All")
    return render_template(
        "portfolio_projects.html",
        personal=PERSONAL_INFO,
        projects=get_all_projects(),
        current_category=category if category in dict(CATEGORY_LABELS) else "All",
        category_labels=CATEGORY_LABELS,
        category_counts=get_category_counts(),
    )


@app.route("/projects/<project_id>")
def project_detail(project_id):
    project = get_project(project_id)
    if not project:
        return redirect(url_for("projects"))
    # simple prev/next for detail navigation
    ids = list(get_all_projects().keys())
    idx = ids.index(project_id)
    next_id = ids[(idx + 1) % len(ids)]
    next_project = get_project(next_id)
    return render_template(
        "portfolio_project_detail.html",
        personal=PERSONAL_INFO,
        project=project,
        next_project=next_project,
    )


@app.route(f"/{REEL_SLUG}")
def reel():
    """Unlisted work showcase. Not linked anywhere on the public site."""
    resp = Response(render_template(
        "portfolio_reel.html",
        personal=PERSONAL_INFO,
        reel=REEL,
    ))
    # belt and braces alongside the in-page noindex meta
    resp.headers["X-Robots-Tag"] = "noindex, nofollow, noarchive"
    resp.headers["Referrer-Policy"] = "no-referrer"
    return resp


@app.route("/robots.txt")
def robots():
    return Response(
        "User-agent: *\n"
        f"Disallow: /{REEL_SLUG}\n"
        "Allow: /\n"
        f"\nSitemap: {SITE_ORIGIN}/sitemap.xml\n",
        mimetype="text/plain",
    )


@app.route("/sitemap.xml")
def sitemap():
    """Sitemap for search engines. The reel is deliberately absent."""
    response = send_from_directory(BASE_DIR, "sitemap.xml")
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route("/googleee285dd89ce1ffed.html")
def google_verification():
    """Google Search Console verification. Live since March — do not rename."""
    return "google-site-verification: googleee285dd89ce1ffed.html"


@app.route("/cv")
def download_cv():
    """Serve the CV PDF for download, if present."""
    pdf = "Hamza_Abu_Saleh_CV.pdf"
    if os.path.exists(os.path.join(BASE_DIR, pdf)):
        return send_from_directory(BASE_DIR, pdf, as_attachment=False)
    abort(404)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("DEBUG", "True").lower() in ("1", "true", "yes")
    print(f"\n  Hamza Abu Saleh — Portfolio v3.0")
    print(f"  Running on http://localhost:{port}\n")
    app.run(host="0.0.0.0", port=port, debug=debug)
