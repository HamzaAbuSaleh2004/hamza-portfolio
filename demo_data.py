"""
Demo Data Module - Pre-computed CV Screening Results
Contains sample CVs and pre-computed analysis results for demo mode
No API calls needed - safe for public deployment
"""

# Sample vacancy data
DEMO_VACANCY = {
    'title': 'Senior Data Scientist',
    'description': '''
    We are seeking a Senior Data Scientist to join our growing AI team. 
    The ideal candidate will have strong experience in machine learning, Python, 
    and deploying ML models to production. You will work on cutting-edge projects 
    involving NLP, computer vision, and predictive analytics.
    
    Required Skills:
    - Python, TensorFlow, PyTorch, scikit-learn
    - Machine Learning & Deep Learning
    - SQL and data manipulation (pandas, numpy)
    - Cloud platforms (AWS, Azure, or GCP)
    - Strong communication and teamwork skills
    ''',
    'cleaned_text': 'senior data scientist growing ai team ideal candidate strong experience machine learning python deploying ml models production work cutting edge projects involving nlp computer vision predictive analytics required skills python tensorflow pytorch scikit learn machine learning deep learning sql data manipulation pandas numpy cloud platforms aws azure gcp strong communication teamwork skills',
    'keywords': [
        ('machine', 0.45),
        ('learning', 0.44),
        ('python', 0.38),
        ('data', 0.35),
        ('ml', 0.32),
        ('cloud', 0.28),
        ('skills', 0.25),
        ('deep', 0.23),
        ('tensorflow', 0.22),
        ('pytorch', 0.21)
    ]
}

# Sample CV data - representing 3 candidates
DEMO_CVS = {
    'CV_01': {
        'candidate_id': 'CV_01',
        'page_texts': {1: '''
        HAMZA ABU SALEH
        Data Science & AI Student | Machine Learning Engineer
        Email: hamza.example@email.com | Phone: +962 77 XXX XXXX
        
        EDUCATION
        Bachelor of Data Science & Artificial Intelligence
        Hussein Technical University (HTU) | GPA: 3.61 | 2022-2026
        
        SKILLS
        Programming: Python, SQL, MATLAB
        ML/AI: TensorFlow, PyTorch, scikit-learn, Deep Learning, Computer Vision
        Data: pandas, numpy, matplotlib, Power BI
        Cloud: Basic AWS experience
        
        EXPERIENCE
        ML Research Assistant | HTU | 2024-Present
        - Developed deep learning models for image classification using PyTorch
        - Implemented NLP pipelines for text analysis
        - Deployed models using Flask and Docker
        
        PROJECTS
        - Heart Disease Prediction: Built ML model with 92% accuracy
        - Computer Vision: Object detection using YOLO
        - NLP Chatbot: RAG-based chatbot using transformers
        '''},
        'full_text': 'HAMZA ABU SALEH Data Science AI Student Machine Learning Engineer Email hamza example email com Phone 962 77 XXX XXXX EDUCATION Bachelor Data Science Artificial Intelligence Hussein Technical University HTU GPA 3 61 2022 2026 SKILLS Programming Python SQL MATLAB ML AI TensorFlow PyTorch scikit learn Deep Learning Computer Vision Data pandas numpy matplotlib Power BI Cloud Basic AWS experience EXPERIENCE ML Research Assistant HTU 2024 Present Developed deep learning models image classification using PyTorch Implemented NLP pipelines text analysis Deployed models using Flask Docker PROJECTS Heart Disease Prediction Built ML model 92 accuracy Computer Vision Object detection using YOLO NLP Chatbot RAG based chatbot using transformers',
        'cleaned_text': 'hamza abu saleh data science ai student machine learning engineer email hamza example email com phone 962 77 xxx xxxx education bachelor data science artificial intelligence hussein technical university htu gpa 3 61 2022 2026 skills programming python sql matlab ml ai tensorflow pytorch scikit learn deep learning computer vision data pandas numpy matplotlib power bi cloud basic aws experience experience ml research assistant htu 2024 present developed deep learning models image classification using pytorch implemented nlp pipelines text analysis deployed models using flask docker projects heart disease prediction built ml model 92 accuracy computer vision object detection using yolo nlp chatbot rag based chatbot using transformers',
        'keywords': [
            ('learning', 0.52),
            ('machine', 0.51),
            ('deep', 0.48),
            ('python', 0.45),
            ('pytorch', 0.42),
            ('data', 0.41),
            ('nlp', 0.38),
            ('ml', 0.36),
            ('models', 0.34),
            ('tensorflow', 0.32),
            ('vision', 0.30),
            ('computer', 0.29),
            ('scikit', 0.28),
            ('aws', 0.22),
            ('flask', 0.20)
        ],
        'evidence_snippets': [
            {'keyword': 'learning', 'page': 1, 'snippet': '...Machine Learning Engineer...Deep Learning, Computer Vision...deep learning models...', 'score': 0.52},
            {'keyword': 'python', 'page': 1, 'snippet': '...Programming: Python, SQL, MATLAB...', 'score': 0.45},
            {'keyword': 'pytorch', 'page': 1, 'snippet': '...ML/AI: TensorFlow, PyTorch, scikit-learn...using PyTorch...', 'score': 0.42}
        ]
    },
    'CV_02': {
        'candidate_id': 'CV_02',
        'page_texts': {1: '''
        SARAH JOHNSON
        Senior ML Engineer | AI Specialist
        Email: sarah.j@email.com | LinkedIn: linkedin.com/in/sarahj
        
        EDUCATION
        M.S. Computer Science - AI Track | Stanford University | 2019
        B.S. Computer Science | MIT | 2017
        
        SKILLS
        Languages: Python, Java, C++, R
        ML Frameworks: TensorFlow, PyTorch, Keras, scikit-learn
        Deep Learning: CNNs, RNNs, Transformers, GANs
        Cloud: AWS (SageMaker, EC2, S3), Azure ML
        Tools: Docker, Kubernetes, Git, MLflow
        
        EXPERIENCE
        Senior Machine Learning Engineer | Tech Corp | 2020-Present
        - Lead ML team of 5 engineers building production recommendation systems
        - Deployed deep learning models serving 1M+ daily users
        - Optimized model inference reducing latency by 40%
        - Tech: Python, TensorFlow, PyTorch, AWS, Kubernetes
        
        ML Engineer | StartupAI | 2019-2020
        - Built NLP models for sentiment analysis and text classification
        - Implemented MLOps pipeline with CI/CD
        - Technologies: Python, spaCy, transformers, Docker
        
        PROJECTS
        - Large-scale Recommender System (TensorFlow, AWS)
        - Real-time Object Detection (PyTorch, YOLO)
        - Conversational AI (GPT fine-tuning, RAG)
        '''},
        'full_text': 'SARAH JOHNSON Senior ML Engineer AI Specialist Email sarah j email com LinkedIn linkedin com in sarahj EDUCATION M S Computer Science AI Track Stanford University 2019 B S Computer Science MIT 2017 SKILLS Languages Python Java C R ML Frameworks TensorFlow PyTorch Keras scikit learn Deep Learning CNNs RNNs Transformers GANs Cloud AWS SageMaker EC2 S3 Azure ML Tools Docker Kubernetes Git MLflow EXPERIENCE Senior Machine Learning Engineer Tech Corp 2020 Present Lead ML team 5 engineers building production recommendation systems Deployed deep learning models serving 1M daily users Optimized model inference reducing latency 40 Tech Python TensorFlow PyTorch AWS Kubernetes ML Engineer StartupAI 2019 2020 Built NLP models sentiment analysis text classification Implemented MLOps pipeline CI CD Technologies Python spaCy transformers Docker PROJECTS Large scale Recommender System TensorFlow AWS Real time Object Detection PyTorch YOLO Conversational AI GPT fine tuning RAG',
        'cleaned_text': 'sarah johnson senior ml engineer ai specialist email sarah j email com linkedin linkedin com in sarahj education m s computer science ai track stanford university 2019 b s computer science mit 2017 skills languages python java c r ml frameworks tensorflow pytorch keras scikit learn deep learning cnns rnns transformers gans cloud aws sagemaker ec2 s3 azure ml tools docker kubernetes git mlflow experience senior machine learning engineer tech corp 2020 present lead ml team 5 engineers building production recommendation systems deployed deep learning models serving 1m daily users optimized model inference reducing latency 40 tech python tensorflow pytorch aws kubernetes ml engineer startupai 2019 2020 built nlp models sentiment analysis text classification implemented mlops pipeline ci cd technologies python spacy transformers docker projects large scale recommender system tensorflow aws real time object detection pytorch yolo conversational ai gpt fine tuning rag',
        'keywords': [
            ('ml', 0.58),
            ('learning', 0.56),
            ('machine', 0.54),
            ('python', 0.52),
            ('tensorflow', 0.50),
            ('pytorch', 0.48),
            ('deep', 0.46),
            ('aws', 0.44),
            ('models', 0.42),
            ('cloud', 0.40),
            ('docker', 0.38),
            ('kubernetes', 0.35),
            ('nlp', 0.33),
            ('scikit', 0.30),
            ('transformers', 0.28)
        ],
        'evidence_snippets': [
            {'keyword': 'ml', 'page': 1, 'snippet': '...Senior ML Engineer...ML Frameworks...Lead ML team...', 'score': 0.58},
            {'keyword': 'python', 'page': 1, 'snippet': '...Languages: Python, Java, C++...Tech: Python, TensorFlow...', 'score': 0.52},
            {'keyword': 'tensorflow', 'page': 1, 'snippet': '...ML Frameworks: TensorFlow, PyTorch...Tech: Python, TensorFlow, PyTorch...', 'score': 0.50}
        ]
    },
    'CV_03': {
        'candidate_id': 'CV_03',
        'page_texts': {1: '''
        MICHAEL CHEN
        Data Analyst | Business Intelligence
        Email: m.chen@email.com | Phone: +1-555-0123
        
        EDUCATION
        B.S. Statistics | University of California | 2020
        
        SKILLS
        Analysis: SQL, Excel, Statistics, Data Visualization
        Programming: Python (pandas, numpy), R
        BI Tools: Tableau, Power BI, Looker
        Basic ML: scikit-learn, regression models
        Databases: MySQL, PostgreSQL
        
        EXPERIENCE
        Data Analyst | Marketing Analytics Co | 2021-Present
        - Analyze customer data and create dashboards using Tableau
        - Write SQL queries for data extraction and reporting
        - Build simple predictive models using Python and scikit-learn
        - Present insights to stakeholders
        
        Junior Analyst | Consulting Firm | 2020-2021
        - Created Excel reports and PowerPoint presentations
        - Performed statistical analysis using R
        - Assisted with data cleaning and preparation
        
        PROJECTS
        - Customer Churn Analysis (Python, scikit-learn, Tableau)
        - Sales Forecasting Dashboard (Power BI, SQL)
        - A/B Testing Framework (Python, statistics)
        '''},
        'full_text': 'MICHAEL CHEN Data Analyst Business Intelligence Email m chen email com Phone 1 555 0123 EDUCATION B S Statistics University California 2020 SKILLS Analysis SQL Excel Statistics Data Visualization Programming Python pandas numpy R BI Tools Tableau Power BI Looker Basic ML scikit learn regression models Databases MySQL PostgreSQL EXPERIENCE Data Analyst Marketing Analytics Co 2021 Present Analyze customer data create dashboards using Tableau Write SQL queries data extraction reporting Build simple predictive models using Python scikit learn Present insights stakeholders Junior Analyst Consulting Firm 2020 2021 Created Excel reports PowerPoint presentations Performed statistical analysis using R Assisted data cleaning preparation PROJECTS Customer Churn Analysis Python scikit learn Tableau Sales Forecasting Dashboard Power BI SQL A B Testing Framework Python statistics',
        'cleaned_text': 'michael chen data analyst business intelligence email m chen email com phone 1 555 0123 education b s statistics university california 2020 skills analysis sql excel statistics data visualization programming python pandas numpy r bi tools tableau power bi looker basic ml scikit learn regression models databases mysql postgresql experience data analyst marketing analytics co 2021 present analyze customer data create dashboards using tableau write sql queries data extraction reporting build simple predictive models using python scikit learn present insights stakeholders junior analyst consulting firm 2020 2021 created excel reports powerpoint presentations performed statistical analysis using r assisted data cleaning preparation projects customer churn analysis python scikit learn tableau sales forecasting dashboard power bi sql a b testing framework python statistics',
        'keywords': [
            ('data', 0.55),
            ('analysis', 0.48),
            ('python', 0.42),
            ('sql', 0.40),
            ('tableau', 0.38),
            ('analyst', 0.36),
            ('scikit', 0.32),
            ('learn', 0.30),
            ('power', 0.28),
            ('bi', 0.28),
            ('statistics', 0.26),
            ('models', 0.22),
            ('excel', 0.20),
            ('r', 0.18),
            ('ml', 0.15)
        ],
        'evidence_snippets': [
            {'keyword': 'data', 'page': 1, 'snippet': '...Data Analyst...customer data...Data Visualization...data extraction...', 'score': 0.55},
            {'keyword': 'python', 'page': 1, 'snippet': '...Programming: Python (pandas, numpy)...using Python and scikit-learn...', 'score': 0.42},
            {'keyword': 'sql', 'page': 1, 'snippet': '...Analysis: SQL, Excel...Write SQL queries...', 'score': 0.40}
        ]
    }
}

# Pre-computed data mining results
DEMO_DATA_MINING_RESULTS = {
    'vacancy_cluster': {
        'cluster_id': 4,
        'cluster_label': 'AI & Machine Learning',
        'cluster_keywords': ['learning', 'machine', 'data', 'ml', 'ai', 'model', 'science', 'python', 'deep']
    },
    'ranked_candidates': [
        {
            'candidate_id': 'CV_02',
            'similarity_score': 0.87,
            'cv_data': DEMO_CVS['CV_02']
        },
        {
            'candidate_id': 'CV_01',
            'similarity_score': 0.81,
            'cv_data': DEMO_CVS['CV_01']
        },
        {
            'candidate_id': 'CV_03',
            'similarity_score': 0.52,
            'cv_data': DEMO_CVS['CV_03']
        }
    ],
    'shortlist': [
        {
            'candidate_id': 'CV_02',
            'similarity_score': 0.87,
            'matched_skills': ['python', 'machine learning', 'deep learning', 'tensorflow', 'pytorch', 'aws', 'docker'],
            'missing_skills': [],
            'match_percentage': 100.0,
            'keywords': DEMO_CVS['CV_02']['keywords']
        },
        {
            'candidate_id': 'CV_01',
            'similarity_score': 0.81,
            'matched_skills': ['python', 'machine learning', 'deep learning', 'tensorflow', 'pytorch', 'aws'],
            'missing_skills': ['docker'],
            'match_percentage': 85.7,
            'keywords': DEMO_CVS['CV_01']['keywords']
        },
        {
            'candidate_id': 'CV_03',
            'similarity_score': 0.52,
            'matched_skills': ['python', 'machine learning'],
            'missing_skills': ['deep learning', 'tensorflow', 'pytorch', 'aws', 'docker'],
            'match_percentage': 28.6,
            'keywords': DEMO_CVS['CV_03']['keywords']
        }
    ]
}

# Pre-computed graph mining results (base64 visualization generated separately)
DEMO_GRAPH_MINING_RESULTS = {
    'centrality_metrics': {
        'CV_02': {
            'pagerank': 0.42,
            'degree_centrality': 1.0,
            'betweenness': 0.5,
            'closeness': 1.0
        },
        'CV_01': {
            'pagerank': 0.35,
            'degree_centrality': 1.0,
            'betweenness': 0.5,
            'closeness': 1.0
        },
        'CV_03': {
            'pagerank': 0.23,
            'degree_centrality': 1.0,
            'betweenness': 0.0,
            'closeness': 1.0
        }
    },
    'duplicates': [],  # No duplicates in sample data
    'outliers': [],  # All candidates are connected
    'visualization': None  # Will be generated if needed, or can add base64 image here
}

def get_demo_results():
    """
    Returns complete demo results for CV screening
    This simulates the entire CV processing pipeline without making any API calls
    
    IMPORTANT: Transforms data to match template expectations
    """
    # Transform text results to match template structure
    transformed_text_results = {}
    for cv_name, cv_data in DEMO_CVS.items():
        transformed_text_results[cv_name] = {
            **cv_data,
            # Extract just the keyword strings (not tuples with scores) for display
            'keywords': [kw[0] for kw in cv_data['keywords']],
            # Rename evidence_snippets to evidence and extract just the snippet text
            'evidence': [ev['snippet'] for ev in cv_data.get('evidence_snippets', [])]
        }
    
    # Transform data mining results to match template structure
    transformed_data_results = {
        'vacancy_cluster': DEMO_DATA_MINING_RESULTS['vacancy_cluster'],
        # Template expects 'rankings' with 'name' and 'score' fields
        'rankings': [
            {
                'name': rc['candidate_id'],
                'score': rc['similarity_score']
            }
            for rc in DEMO_DATA_MINING_RESULTS['ranked_candidates']
        ],
        # Add shortlist if needed
        'shortlist': DEMO_DATA_MINING_RESULTS['shortlist']
    }
    
    # Transform graph mining results to match template structure  
    transformed_graph_results = {
        'centrality_metrics': DEMO_GRAPH_MINING_RESULTS['centrality_metrics'],
        # Template expects 'pagerank' as a separate dict
        'pagerank': {
            cv_name: metrics['pagerank']
            for cv_name, metrics in DEMO_GRAPH_MINING_RESULTS['centrality_metrics'].items()
        },
        'duplicates': DEMO_GRAPH_MINING_RESULTS['duplicates'],
        'outliers': DEMO_GRAPH_MINING_RESULTS['outliers'],
        'visualization': DEMO_GRAPH_MINING_RESULTS['visualization']
    }
    
    return {
        'text_results': transformed_text_results,
        'data_results': transformed_data_results,
        'graph_results': transformed_graph_results,
        'vacancy': DEMO_VACANCY
    }

