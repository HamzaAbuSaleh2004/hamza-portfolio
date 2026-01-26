"""
Project data for the portfolio website
Contains all information about Hamza's projects
"""

PROJECTS = {
    "charging-portal": {
        "id": "charging-portal",
        "title": "Charging Intelligence Portal",
        "category": "Web",
        "tags": ["ML", "Flask", "XAI"],
        "one_liner": "EV charging analytics platform with ML, RL, XAI, fairness, fuzzy logic, and anomaly detection",
        "description": """
        A comprehensive full-stack web application that combines six advanced AI methodologies into one 
        unified, interpretable, and fairness-aware EV charging decision system. The platform provides 
        intelligent charging recommendations while ensuring transparency and fairness in predictions.
        """,
        "tech_stack": ["Python", "Flask", "pandas", "NumPy", "scikit-learn", "SHAP", "LIME", "matplotlib", "Bootstrap", "JavaScript"],
        "highlights": [
            "Random Forest models for cost/time prediction and long-session classification",
            "Explainability with SHAP/LIME plus plain-English explanations (10% rule)",
            "Fairness metrics (DIR, demographic parity, MPD, residual error parity) with mitigation strategies",
            "Q-Learning recommendations (wait/standard/fast charge) and fuzzy decision system",
            "Isolation Forest anomaly detection with admin/user dashboards"
        ],
        "impact": "Combines 6 AI methodologies into one interpretable, fairness-aware EV charging decision system.",
        "github": "#",
        "demo": "#",
        "docs": "#",
        "screenshots": []
    },
    
    "cv-screening": {
        "id": "cv-screening",
        "title": "Advanced Recruitment Screening System",
        "category": "CV",
        "tags": ["NLP", "Graph Mining", "RAG"],
        "one_liner": "CV parsing + text/data/graph mining + RAG chatbot for evidence-based candidate Q&A",
        "description": """
        An intelligent recruitment screening platform that automates the hiring process through advanced 
        text mining, data analytics, and graph-based analysis. The system parses CVs, ranks candidates, 
        identifies skill gaps, and provides an AI-powered chatbot for evidence-based candidate evaluation.
        """,
        "tech_stack": ["Python", "Flask", "TF-IDF", "scikit-learn", "NetworkX", "Sentence Transformers", "Gemini API", "Bootstrap"],
        "highlights": [
            "PDF CV parsing (up to 10 CVs) with keyword extraction and evidence snippets with page numbers",
            "K-Means vacancy clustering with cosine-similarity ranking and skill gap analysis",
            "Graph analytics (PageRank, degree/betweenness/closeness centrality) plus duplicate/outlier detection",
            "RAG chatbot with cited answers from CV chunks and interview question generation"
        ],
        "impact": "Automates shortlist creation and makes hiring insights transparent with citations from CV content.",
        "github": "#",
        "demo": "/cv-screening-demo",
        "docs": "#",
        "screenshots": ["Step1.png", "Step 2.png", "Step 3.png", "Results 1.png", "Results 2.png", "Results 3.png", "Rag1.png", "Rag2.png"]
    },
    
    "arabic-nlp": {
        "id": "arabic-nlp",
        "title": "Medical Specialty Classification (Arabic NLP)",
        "category": "NLP",
        "tags": ["Deep Learning", "BERT", "Arabic"],
        "one_liner": "Classifies Arabic medical text into specialties using ML + deep learning + BERT fine-tuning",
        "description": """
        A comprehensive NLP pipeline designed for Arabic medical text classification. The system processes 
        Arabic medical documents and classifies them into appropriate medical specialties using state-of-the-art 
        deep learning models including BERT, LSTM, and GRU architectures.
        """,
        "tech_stack": ["TensorFlow", "Keras", "BERT", "LSTM", "GRU", "RNN", "TF-IDF", "Word2Vec", "pandas", "NumPy"],
        "highlights": [
            "Arabic normalization, tokenization, stopword filtering, and morphology-aware preprocessing",
            "Vectorization comparison: TF-IDF vs Word2Vec/Skip-gram vs BERT embeddings",
            "Model comparison: Naive Bayes vs RNN/LSTM/GRU vs BERT fine-tuning",
            "Scales to 13M+ records with batching and sampling strategies"
        ],
        "impact": "Demonstrates strong Arabic NLP pipeline design and modern transfer-learning capability.",
        "github": "#",
        "demo": "#",
        "docs": "#",
        "screenshots": []
    },
    
    "vehicle-classification": {
        "id": "vehicle-classification",
        "title": "Vehicle Classification System",
        "category": "ML",
        "tags": ["Computer Vision", "CNN", "Deep Learning"],
        "one_liner": "Deep learning image classifier to recognize vehicle types (MLP vs CNN comparison)",
        "description": """
        A computer vision project that implements and compares different deep learning architectures for 
        vehicle type classification. The system demonstrates the effectiveness of CNNs over traditional 
        MLPs for image classification tasks with comprehensive evaluation metrics.
        """,
        "tech_stack": ["TensorFlow", "Keras", "PyTorch", "CNN", "MLP", "Data Augmentation", "matplotlib"],
        "highlights": [
            "End-to-end image preprocessing pipeline with augmentation techniques",
            "Model training with early stopping and hyperparameter tuning",
            "Comprehensive evaluation: confusion matrix, per-class metrics, ROC curves",
            "Real-time prediction capability on unseen images"
        ],
        "impact": "Establishes strong computer vision foundations with clear comparative study of architectures.",
        "github": "#",
        "demo": "#",
        "docs": "#",
        "screenshots": []
    },
    
    "ml-portfolio": {
        "id": "ml-portfolio",
        "title": "Machine Learning Implementations Portfolio",
        "category": "ML",
        "tags": ["Supervised Learning", "Unsupervised Learning", "Evaluation"],
        "one_liner": "Broad collection of supervised/unsupervised ML pipelines and evaluation workflows",
        "description": """
        A comprehensive collection of machine learning implementations covering the full spectrum of 
        supervised and unsupervised learning algorithms. Each implementation includes proper evaluation 
        workflows, model selection techniques, and best practices in ML engineering.
        """,
        "tech_stack": ["scikit-learn", "pandas", "NumPy", "matplotlib", "statsmodels"],
        "highlights": [
            "Regression: linear/polynomial/Ridge/Lasso/ElasticNet/Random Forest/Gradient Boosting",
            "Classification: logistic regression/decision trees/RF/SVM/KNN/Naive Bayes",
            "Clustering: K-Means/Hierarchical/DBSCAN with silhouette/elbow/dendrogram analysis",
            "Model selection: cross-validation, comprehensive metrics, GridSearchCV/RandomizedSearchCV, data leakage prevention"
        ],
        "impact": "Demonstrates breadth across core ML algorithms and strong engineering practices.",
        "github": "#",
        "demo": "#",
        "docs": "#",
        "screenshots": []
    }
}

# Category mapping for filtering
CATEGORIES = {
    "All": list(PROJECTS.keys()),
    "CV": ["cv-screening"],
    "NLP": ["arabic-nlp", "cv-screening"],
    "ML": ["charging-portal", "vehicle-classification", "ml-portfolio"],
    "Web": ["charging-portal", "cv-screening"]
}

def get_project(project_id):
    """Get a single project by ID"""
    return PROJECTS.get(project_id)

def get_all_projects():
    """Get all projects"""
    return PROJECTS

def get_projects_by_category(category):
    """Get projects filtered by category"""
    if category == "All":
        return PROJECTS
    
    project_ids = CATEGORIES.get(category, [])
    return {pid: PROJECTS[pid] for pid in project_ids if pid in PROJECTS}

def get_featured_projects(limit=3):
    """Get featured projects for home page"""
    featured = ["cv-screening", "charging-portal", "arabic-nlp"]
    return {pid: PROJECTS[pid] for pid in featured[:limit]}
