"""
Project data for the portfolio website (v3.0 — monochrome redesign)
Contains all information about Hamza's projects + certifications.
"""

PROJECTS = {
    # ==================== PRODUCTION / CLOUD & AGENTS ====================
    "rfp-system": {
        "id": "rfp-system",
        "title": "Multi-Agent Procurement / RFP System",
        "category": "Agents",
        "year": "2025",
        "tags": ["Multi-Agent", "Google ADK", "Cloud"],
        "one_liner": "A hierarchical agent system (1 director + 5 sub-agents) that automates the end-to-end enterprise procurement lifecycle.",
        "description": """
        A production hierarchical multi-agent system built on Google's Agent Development Kit (ADK) that
        automates the entire procurement and Request-for-Proposal (RFP) lifecycle for enterprise and
        public-sector bid teams. A single director agent orchestrates five specialised sub-agents —
        spanning RFP creation, evaluation, and assistance — over a ~64-endpoint FastAPI service.
        The platform ships print-ready bilingual (EN / AR) PDF documents and runs entirely on Google
        Cloud, deployed to Cloud Run with a managed PostgreSQL backend and registered as an
        Agentspace agent card.
        """,
        "tech_stack": ["Google ADK", "Gemini", "FastAPI", "Cloud Run", "PostgreSQL", "Vertex AI", "Python", "Agentspace"],
        "highlights": [
            "Hierarchical orchestration: 1 director agent coordinating 5 specialised sub-agents (Sequential / Parallel / Loop architectures)",
            "~64-endpoint FastAPI service on Cloud Run backed by managed PostgreSQL",
            "Print-ready bilingual (English / Arabic) PDF generation for formal bid documents",
            "Deployed and registered as an Agentspace agent card for enterprise discovery",
            "Sole developer — from architecture and prompt engineering through to production deployment"
        ],
        "impact": "Compresses a multi-week manual procurement workflow into an orchestrated, auditable agent pipeline for MENA enterprise and public-sector teams.",
        "github": "#",
        "demo": "#",
        "docs": "#",
        "screenshots": []
    },

    "naqla": {
        "id": "naqla",
        "title": "Naqla — Real-Time Delivery & Logistics Platform",
        "category": "Web",
        "year": "2025",
        "tags": ["PWA", "Firebase", "Arabic RTL"],
        "one_liner": "A production Arabic-first (RTL) last-mile logistics PWA serving merchants, drivers, and admins from one serverless codebase.",
        "description": """
        Naqla is a production, Arabic-first (right-to-left) last-mile logistics Progressive Web App that
        serves merchants, drivers, and administrators from a single serverless Firebase codebase.
        It delivers live order tracking across three role-gated portals and is powered by an
        order-derived accounting engine that handles settlement batches, partial-payment reconciliation,
        and per-merchant tariffs — plus SLA-based returns tracking with automated overdue flagging and
        a complete audit trail.
        """,
        "tech_stack": ["Firebase", "Firestore", "PWA", "JavaScript", "Cloud Functions", "RTL / i18n", "Real-time DB"],
        "highlights": [
            "Three role-gated portals (merchant / driver / admin) from a single serverless codebase",
            "Live, real-time order tracking across the full last-mile delivery flow",
            "Order-derived accounting engine: settlement batches, partial-payment reconciliation, per-merchant tariffs",
            "SLA-based returns tracking with automated overdue flagging and a full audit trail",
            "Arabic-first (RTL) UI built for real merchant and driver operations"
        ],
        "impact": "Runs real merchant and driver operations on one serverless codebase — turning raw orders into reconciled, auditable accounting automatically.",
        "github": "#",
        "demo": "#",
        "docs": "#",
        "screenshots": []
    },

    "civic-reporting": {
        "id": "civic-reporting",
        "title": "Civic-Issue Reporting Platform",
        "category": "Agents",
        "year": "2025",
        "tags": ["YOLOv8", "Vertex AI", "Web"],
        "one_liner": "A bilingual civic platform that lets residents report municipal issues, de-duplicating reports with YOLOv8 vision + geolocation.",
        "description": """
        A bilingual (English / Arabic, RTL) civic-engagement platform that lets residents report and track
        municipal problems. To keep the queue clean, the system cuts duplicate submissions using YOLOv8
        image detection served through Vertex AI, combined with Haversine geolocation matching to cluster
        reports that describe the same real-world issue. Built on React + FastAPI with a Google ADK agent
        layer and deployed to Cloud Run.
        """,
        "tech_stack": ["React", "FastAPI", "Google ADK", "YOLOv8", "Vertex AI", "Cloud Run", "Geolocation"],
        "highlights": [
            "Bilingual (EN / AR RTL) reporting and tracking interface for residents",
            "Duplicate-report suppression via YOLOv8 image detection served on Vertex AI",
            "Haversine geolocation matching to cluster reports of the same physical issue",
            "React + FastAPI + Google ADK agent layer, deployed to Cloud Run",
            "Turns unstructured citizen reports into a de-duplicated, trackable municipal queue"
        ],
        "impact": "Reduces duplicate municipal reports by fusing computer vision with geolocation, so agencies triage real issues instead of noise.",
        "github": "#",
        "demo": "#",
        "docs": "#",
        "screenshots": []
    },

    # ==================== ML / NLP / CV PORTFOLIO ====================
    "charging-portal": {
        "id": "charging-portal",
        "title": "Charging Intelligence Portal",
        "category": "ML",
        "year": "2024",
        "tags": ["ML", "XAI", "Fairness"],
        "one_liner": "An EV charging analytics platform fusing six AI methodologies — ML, RL, XAI, fairness, fuzzy logic, and anomaly detection.",
        "description": """
        A comprehensive full-stack web application that combines six advanced AI methodologies into one
        unified, interpretable, and fairness-aware EV charging decision system. The platform provides
        intelligent charging recommendations while ensuring transparency and fairness in every prediction.
        """,
        "tech_stack": ["Python", "Flask", "scikit-learn", "SHAP", "LIME", "pandas", "NumPy", "JavaScript"],
        "highlights": [
            "Random Forest models for cost/time prediction and long-session classification",
            "Explainability with SHAP / LIME plus plain-English explanations (10% rule)",
            "Fairness metrics (DIR, demographic parity, MPD, residual error parity) with mitigation strategies",
            "Q-Learning recommendations (wait / standard / fast charge) and a fuzzy decision system",
            "Isolation Forest anomaly detection with admin and user dashboards"
        ],
        "impact": "Combines 6 AI methodologies into one interpretable, fairness-aware EV charging decision system.",
        "github": "#",
        "demo": "#",
        "docs": "#",
        "screenshots": [
            "charging-portal/1.png", "charging-portal/2.png", "charging-portal/3.png",
            "charging-portal/4.png", "charging-portal/5.png", "charging-portal/6.png",
            "charging-portal/7.png", "charging-portal/8.png", "charging-portal/9.png",
            "charging-portal/10.png", "charging-portal/11.png", "charging-portal/12.png"
        ]
    },

    "cv-screening": {
        "id": "cv-screening",
        "title": "Advanced Recruitment Screening System",
        "category": "NLP",
        "year": "2024",
        "tags": ["NLP", "Graph Mining", "RAG"],
        "one_liner": "CV parsing + text/data/graph mining + a RAG chatbot for evidence-based, citable candidate Q&A.",
        "description": """
        An intelligent recruitment screening platform that automates the hiring process through advanced
        text mining, data analytics, and graph-based analysis. The system parses CVs, ranks candidates,
        identifies skill gaps, and provides an AI-powered chatbot for evidence-based candidate evaluation
        with citations back to the source CV.
        """,
        "tech_stack": ["Python", "Flask", "TF-IDF", "scikit-learn", "NetworkX", "Sentence Transformers", "Gemini API"],
        "highlights": [
            "PDF CV parsing (up to 10 CVs) with keyword extraction and evidence snippets with page numbers",
            "K-Means vacancy clustering with cosine-similarity ranking and skill-gap analysis",
            "Graph analytics (PageRank, degree / betweenness / closeness centrality) plus duplicate / outlier detection",
            "RAG chatbot with cited answers from CV chunks and interview-question generation"
        ],
        "impact": "Automates shortlist creation and makes hiring insights transparent with citations pulled from CV content.",
        "github": "#",
        "demo": "#",
        "docs": "#",
        "screenshots": ["Step1.png", "Step 2.png", "Step 3.png", "Results 1.png", "Results 2.png", "Results 3.png", "Rag1.png", "Rag2.png"]
    },

    "arabic-nlp": {
        "id": "arabic-nlp",
        "title": "Medical Specialty Classification (Arabic NLP)",
        "category": "NLP",
        "year": "2024",
        "tags": ["Deep Learning", "BERT", "Arabic"],
        "one_liner": "Classifies Arabic medical text into specialties using classical ML, deep learning, and BERT fine-tuning.",
        "description": """
        A comprehensive NLP pipeline designed for Arabic medical text classification. The system processes
        Arabic medical documents and classifies them into the appropriate medical specialties using
        state-of-the-art deep learning models including BERT, LSTM, and GRU architectures, benchmarked
        against classical baselines.
        """,
        "tech_stack": ["TensorFlow", "Keras", "BERT", "LSTM", "GRU", "Word2Vec", "TF-IDF", "pandas"],
        "highlights": [
            "Arabic normalization, tokenization, stopword filtering, and morphology-aware preprocessing",
            "Vectorization comparison: TF-IDF vs Word2Vec / Skip-gram vs BERT embeddings",
            "Model comparison: Naive Bayes vs RNN / LSTM / GRU vs BERT fine-tuning",
            "Scales to 13M+ records with batching and sampling strategies"
        ],
        "impact": "Demonstrates strong Arabic NLP pipeline design and modern transfer-learning capability at scale.",
        "github": "#",
        "demo": "#",
        "docs": "#",
        "screenshots": []
    },

    "vehicle-classification": {
        "id": "vehicle-classification",
        "title": "Automotive Image Classification",
        "category": "CV",
        "year": "2023",
        "tags": ["Computer Vision", "CNN", "PyTorch"],
        "one_liner": "A deep-learning image classifier that recognises vehicle types, comparing MLP vs CNN architectures.",
        "description": """
        A computer vision project that implements and compares different deep learning architectures for
        vehicle-type classification. Trained with PyTorch / TensorFlow using data preprocessing and
        augmentation, it demonstrates the effectiveness of CNNs over traditional MLPs, with robustness
        improved through iterative error analysis and optimisation.
        """,
        "tech_stack": ["PyTorch", "TensorFlow", "Keras", "CNN", "MLP", "Data Augmentation", "matplotlib"],
        "highlights": [
            "End-to-end image preprocessing pipeline with augmentation techniques",
            "Model training with early stopping and hyperparameter tuning",
            "Comprehensive evaluation: confusion matrix, per-class metrics, ROC curves",
            "Robustness improved through iterative error analysis and optimisation"
        ],
        "impact": "Establishes strong computer-vision foundations with a clear comparative study of architectures.",
        "github": "#",
        "demo": "#",
        "docs": "#",
        "screenshots": []
    },

    "ml-portfolio": {
        "id": "ml-portfolio",
        "title": "Machine Learning Implementations Portfolio",
        "category": "ML",
        "year": "2023",
        "tags": ["Supervised", "Unsupervised", "Evaluation"],
        "one_liner": "A broad collection of supervised / unsupervised ML pipelines with rigorous evaluation workflows.",
        "description": """
        A comprehensive collection of machine learning implementations covering the full spectrum of
        supervised and unsupervised learning algorithms. Each implementation includes proper evaluation
        workflows, model-selection techniques, and best practices in ML engineering.
        """,
        "tech_stack": ["scikit-learn", "pandas", "NumPy", "matplotlib", "statsmodels"],
        "highlights": [
            "Regression: linear / polynomial / Ridge / Lasso / ElasticNet / Random Forest / Gradient Boosting",
            "Classification: logistic regression / decision trees / RF / SVM / KNN / Naive Bayes",
            "Clustering: K-Means / Hierarchical / DBSCAN with silhouette / elbow / dendrogram analysis",
            "Model selection: cross-validation, GridSearchCV / RandomizedSearchCV, data-leakage prevention"
        ],
        "impact": "Demonstrates breadth across core ML algorithms and strong engineering practices.",
        "github": "#",
        "demo": "#",
        "docs": "#",
        "screenshots": []
    }
}

# Category mapping for filtering (order defines the featured-first gallery order)
CATEGORIES = {
    "All": list(PROJECTS.keys()),
    "Agents": ["rfp-system", "civic-reporting"],
    "Web": ["naqla", "civic-reporting"],
    "CV": ["civic-reporting", "vehicle-classification"],
    "NLP": ["cv-screening", "arabic-nlp"],
    "ML": ["charging-portal", "ml-portfolio"],
}

# Human labels for the filter buttons on the projects page
CATEGORY_LABELS = [
    ("All", "All Work"),
    ("Agents", "AI Agents & Cloud"),
    ("CV", "Computer Vision"),
    ("NLP", "NLP"),
    ("ML", "Machine Learning"),
    ("Web", "Web"),
]

# Attach the set of filter-category keys each project belongs to (for the
# projects-page filter chips). Also records display order + a 1-based index.
for _i, (_pid, _proj) in enumerate(PROJECTS.items(), start=1):
    _proj["filters"] = [
        _cat for _cat, _ids in CATEGORIES.items()
        if _cat != "All" and _pid in _ids
    ]
    _proj["order"] = _i


def get_category_counts():
    """Number of projects per filter category (for the filter chips)."""
    counts = {"All": len(PROJECTS)}
    for _cat, _ids in CATEGORIES.items():
        if _cat != "All":
            counts[_cat] = len(_ids)
    return counts

# ==================== CERTIFICATIONS (Credly badges) ====================
# The Google Cloud Digital Leader badge is listed first, followed by the
# four Google Cloud skill badges (rendered as Credly embeds).
CERTIFICATIONS = [
    {"badge_id": "c818b3f9-1fc8-43eb-a36a-d945ce79814b", "label": "Google Cloud Digital Leader"},
    {"badge_id": "53076f1f-f9d3-4af8-9886-715240db39de", "label": "Google Cloud Skill Badge"},
    {"badge_id": "2b2109e5-929f-4f9f-90bd-71d272b28eb4", "label": "Google Cloud Skill Badge"},
    {"badge_id": "4c50aff6-1012-41a4-8e19-7ee36a03eed7", "label": "Google Cloud Skill Badge"},
    {"badge_id": "5b1ef703-4ea5-4dc0-b5f2-cc842b39aee5", "label": "Google Cloud Skill Badge"},
]


def get_project(project_id):
    """Get a single project by ID."""
    return PROJECTS.get(project_id)


def get_all_projects():
    """Get all projects."""
    return PROJECTS


def get_projects_by_category(category):
    """Get projects filtered by category."""
    if category == "All":
        return PROJECTS
    project_ids = CATEGORIES.get(category, [])
    return {pid: PROJECTS[pid] for pid in project_ids if pid in PROJECTS}


def get_featured_projects(limit=3):
    """Get featured projects for the home page."""
    featured = ["rfp-system", "naqla", "civic-reporting", "cv-screening"]
    return {pid: PROJECTS[pid] for pid in featured[:limit]}
