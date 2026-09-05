"""
Hamza Abu Saleh — Portfolio v3.0
Monochrome, editorial, interactive Flask portfolio.

Self-contained: run `python portfolio_app.py` then open http://localhost:5000
"""
import os

from flask import (
    Flask, render_template, request, redirect, url_for, send_from_directory, abort
)

from projects_data import (
    get_all_projects, get_project, get_featured_projects,
    get_category_counts, CATEGORY_LABELS, CERTIFICATIONS,
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "hamza-portfolio-v3-secret")

# ==================== PERSONAL INFO (from CV) ====================
PERSONAL_INFO = {
    "name": "Hamza Abu Saleh",
    "role": "AI Engineer",
    "headline": "Data Science & AI student · Cloud AI Engineer @ LiverX · building production multi-agent systems on Google Cloud.",
    "location": "Amman, Jordan",
    "email": "hamzaabusaleh04@gmail.com",
    "phone": "+962 77 806 4473",
    "linkedin": "https://www.linkedin.com/in/hamza-abu-saleh-9572b7242/",
    "github": "#",
    "objective": (
        "Data Science & AI student and Cloud AI Engineer apprentice specializing in production "
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
        "period": "2022 – 2026 (Expected)",
        "gpa": "3.63 / 4.00",
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


# ==================== SEO / SEARCH CONSOLE ====================
@app.route("/googleee285dd89ce1ffed.html")
def google_verification():
    """Google Search Console verification file."""
    return "google-site-verification: googleee285dd89ce1ffed.html"


@app.route("/sitemap.xml")
def sitemap():
    """Sitemap for search engines."""
    response = send_from_directory(BASE_DIR, "sitemap.xml")
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route("/robots.txt")
def robots():
    """Robots.txt for search engines."""
    response = send_from_directory(BASE_DIR, "robots.txt")
    response.headers["Content-Type"] = "text/plain"
    return response


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
