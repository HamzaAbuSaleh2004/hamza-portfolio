"""
Interactive Flask Portfolio Website for Hamza Abu Saleh
Features: Personal info pages, project showcase, CV screening demo
"""
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os
import sys
from projects_data import get_all_projects, get_project, get_projects_by_category, get_featured_projects
import config
from demo_data import get_demo_results, DEMO_VACANCY

# Add Task3 to path for CV screening imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Task3'))

# Initialize CV screening based on mode
if config.DEMO_MODE:
    # Demo mode - no engines needed, uses pre-computed data
    print("[INFO] Running in DEMO MODE - using pre-computed sample data")
    cv_screening_available = True
    text_engine = None
    data_engine = None
    graph_engine = None
    rag_chatbot = None
else:
    # Live mode - initialize real engines with API
    print("[INFO] Running in LIVE MODE - initializing engines")
    try:
        from Task3.modules.text_mining import TextMiningEngine
        from Task3.modules.data_mining import DataMiningEngine
        from Task3.modules.graph_mining import GraphMiningEngine
        from Task3.modules.rag_chatbot import RAGChatbot
        import pickle
        
        # Load models for CV screening
        data_dir = os.path.join(os.path.dirname(__file__), 'Data')
        tfidf_path = os.path.join(data_dir, 'tfidf_vectorizer.pkl')
        kmeans_path = os.path.join(data_dir, 'kmeans_model.pkl')
        
        tfidf_vectorizer = None
        kmeans_model = None
        
        if os.path.exists(tfidf_path):
            with open(tfidf_path, 'rb') as f:
                tfidf_vectorizer = pickle.load(f)
            print("[INFO] TF-IDF vectorizer loaded successfully")
        
        if os.path.exists(kmeans_path):
            with open(kmeans_path, 'rb') as f:
                kmeans_model = pickle.load(f)
            print("[INFO] K-Means model loaded successfully")
        
        # Initialize engines
        text_engine = TextMiningEngine(tfidf_vectorizer) if tfidf_vectorizer else None
        data_engine = DataMiningEngine(kmeans_model, tfidf_vectorizer) if kmeans_model and tfidf_vectorizer else None
        graph_engine = GraphMiningEngine(tfidf_vectorizer) if tfidf_vectorizer else None
        rag_chatbot = RAGChatbot()
        
        cv_screening_available = True
        print("[INFO] CV screening engines initialized successfully")
        
    except Exception as e:
        print(f"[WARNING] CV screening modules not available: {e}")
        cv_screening_available = False
        text_engine = None
        data_engine = None
        graph_engine = None
        rag_chatbot = None

app = Flask(__name__)
app.secret_key = 'hamza-portfolio-secret-key-2026'
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Global storage for CV screening session data
session_data = {}

# Personal information
PERSONAL_INFO = {
    "name": "Hamza Abu Saleh",
    "headline": "Aspiring Data Scientist | Data Science & AI Student at HTU | Aspiring AI Engineer | Co-Founder of Madmoon (FinTech) | Machine Learning & NLP",
    "location": "Amman, Jordan",
    "email": "22110077@htu.edu.jo",
    "phone": "+962 77 806 4473",
    "linkedin": "https://www.linkedin.com/in/hamza-abu-saleh-9572b7242/",
    "objective": "Data Science & AI student with a strong interest in applied AI, computer vision, and intelligent systems, seeking opportunities to contribute to real-world, high-impact projects through research-driven engineering and advanced AI solutions.",
    "education": {
        "degree": "Bachelor of Data Science & Artificial Intelligence",
        "institution": "Hussein Technical University (HTU)",
        "period": "2022 – 2026 (Expected)",
        "gpa": "3.61 (Excellence)"
    },
    "experience": [
        {
            "title": "Student Volunteer & Gifted Student Support",
            "organization": "Deanship of Student Affairs – HTU",
            "period": "2025 – Present",
            "responsibilities": [
                "Support student engagement initiatives by collaborating with clubs, teams, and events",
                "Foster creativity, leadership, and teamwork among students through program coordination",
                "Balance academic commitments with professional development"
            ]
        },
        {
            "title": "Volunteer Team Leader",
            "organization": "Invent for the Planet 2025 – HTU",
            "period": "Feb 2025",
            "responsibilities": [
                "Coordinated volunteer teams during a global innovation event with 24 countries & 51 universities",
                "Supported teams in prototyping sustainable solutions using advanced maker tools",
                "Ensured smooth event execution by liaising with mentors, faculty, and participants"
            ]
        },
        {
            "title": "Co-Founder & Team Lead",
            "organization": "Madmoon (FinTech Escrow)",
            "period": "2025",
            "responsibilities": [
                "Co-founded Madmoon, a third-party escrow fintech solution to enhance secure online transactions",
                "Pitched the idea against 100+ teams, reaching top 4 finalists and securing incubation support",
                "Led team through ideation, market research, and prototype development"
            ]
        }
    ],
    "skills": {
        "technical": ["Python", "PyTorch", "TensorFlow", "Computer Vision", "Machine Learning", "Deep Learning", 
                     "scikit-learn", "SQL", "MATLAB", "Hugging Face", "Power BI", "MySQL", "Flask", 
                     "Raspberry Pi", "n8n", "Networking", "HTML", "CSS"],
        "soft": ["Team Leadership", "Event Management", "Innovation", "Problem-solving", "Adaptability", "Project Coordination"]
    },
    "achievements": [
        "4th Place, Rocket Pitch Startup Competition (2025)",
        "Incubation opportunity with INJAZ for Madmoon startup development",
        "Leadership recognition during global Invent for the Planet challenge",
        "Computing Research Project on clinical factors influencing heart disease risk"
    ]
}


# ==================== PORTFOLIO ROUTES ====================

@app.route('/')
def home():
    """Home page with hero section and featured projects"""
    featured = get_featured_projects(3)
    return render_template('portfolio_home.html', 
                         personal=PERSONAL_INFO, 
                         featured_projects=featured)

@app.route('/about')
def about():
    """About page with bio, education, experience, achievements"""
    return render_template('portfolio_about.html', personal=PERSONAL_INFO)

@app.route('/projects')
def projects():
    """Projects gallery with filtering"""
    category = request.args.get('category', 'All')
    if category == 'All':
        filtered_projects = get_all_projects()
    else:
        filtered_projects = get_projects_by_category(category)
    
    return render_template('portfolio_projects.html', 
                         personal=PERSONAL_INFO,
                         projects=filtered_projects, 
                         current_category=category)

@app.route('/projects/<project_id>')
def project_detail(project_id):
    """Individual project detail page"""
    project = get_project(project_id)
    if not project:
        return redirect(url_for('projects'))
    
    return render_template('portfolio_project_detail.html', 
                         personal=PERSONAL_INFO,
                         project=project)

@app.route('/contact')
def contact():
    """Contact page"""
    return render_template('portfolio_contact.html', personal=PERSONAL_INFO)


# ==================== CV SCREENING DEMO ROUTES ====================

@app.route('/cv-screening-demo')
def cv_screening_demo():
    """CV Screening demo landing page"""
    return render_template('cv_demo_index.html', 
                         personal=PERSONAL_INFO,
                         cv_available=cv_screening_available,
                         demo_mode=config.DEMO_MODE)

@app.route('/cv-demo/step1', methods=['GET', 'POST'])
def cv_demo_step1():
    """Step 1: Input vacancy details"""
    if not cv_screening_available:
        return redirect(url_for('cv_screening_demo'))
    
    if request.method == 'POST':
        # Store vacancy details in session
        session['job_title'] = request.form.get('job_title', '')
        session['job_description'] = request.form.get('job_description', '')
        return redirect(url_for('cv_demo_step2'))
    
    return render_template('cv_demo_step1.html', personal=PERSONAL_INFO)

@app.route('/cv-demo/step2', methods=['GET', 'POST'])
def cv_demo_step2():
    """Step 2: Upload CVs and process"""
    if not cv_screening_available:
        return redirect(url_for('cv_screening_demo'))
    
    if 'job_title' not in session:
        return redirect(url_for('cv_demo_step1'))
    
    if request.method == 'POST':
        try:
            job_title = session.get('job_title', '')
            job_description = session.get('job_description', '')
            
            # Check if running in demo mode
            if config.DEMO_MODE:
                # Demo mode - use pre-computed results
                print("[INFO] Demo mode: returning pre-computed results")
                
                # Get demo results
                demo_results = get_demo_results()
                text_results = demo_results['text_results']
                data_results = demo_results['data_results']
                graph_results = demo_results['graph_results']
                
                # Store in session (use dummy session ID for demo)
                session_id = 'demo_session'
                session_data[session_id] = {
                    'job_title': job_title or DEMO_VACANCY['title'],
                    'job_description': job_description or DEMO_VACANCY['description'],
                    'text_results': text_results,
                    'data_results': data_results,
                    'graph_results': graph_results,
                    'cv_paths': ['Demo CV 1', 'Demo CV 2', 'Demo CV 3']
                }
                session['session_id'] = session_id
                
                return redirect(url_for('cv_demo_results'))
            
            # Live mode - process uploaded CVs
            # Get uploaded files
            files = request.files.getlist('cv_files')
            if not files or files[0].filename == '':
                return render_template('cv_demo_step2.html', personal=PERSONAL_INFO, error="Please upload at least one CV")
            
            # Save files
            cv_paths = []
            for file in files:
                if file and file.filename.endswith('.pdf'):
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                    file.save(filepath)
                    cv_paths.append(filepath)
            
            if not cv_paths:
                return render_template('cv_demo_step2.html', personal=PERSONAL_INFO, error="Please upload PDF files only")
            
            # Process CVs with text mining (one at a time)
            text_results = {}
            cv_data_list = []
            
            if text_engine:
                for idx, cv_path in enumerate(cv_paths):
                    candidate_id = f"CV_{idx+1:02d}"
                    cv_data = text_engine.process_cv(cv_path, candidate_id)
                    text_results[candidate_id] = cv_data
                    cv_data_list.append(cv_data)
            
            # Process vacancy text
            vacancy_data = {}
            if text_engine:
                vacancy_data = text_engine.process_vacancy(job_title, job_description)
            
            # Process with data mining (ranking and skill matching)
            data_results = {}
            if data_engine and cv_data_list and vacancy_data:
                # Classify vacancy
                vacancy_cluster = data_engine.classify_vacancy(vacancy_data['cleaned_text'])
                
                # Rank candidates
                ranked_candidates = data_engine.rank_candidates(
                    vacancy_data['cleaned_text'], 
                    cv_data_list
                )
                
                # Generate shortlist with skill matching
                shortlist = data_engine.generate_shortlist(
                    ranked_candidates, 
                    job_description, 
                    top_n=min(5, len(cv_data_list))
                )
                
                data_results = {
                    'vacancy_cluster': vacancy_cluster,
                    'ranked_candidates': ranked_candidates,
                    'shortlist': shortlist
                }
            
            # Process with graph mining
            graph_results = {}
            if graph_engine and cv_data_list:
                # Build similarity graph
                graph_engine.build_similarity_graph(cv_data_list, similarity_threshold=0.1)
                
                # Calculate centrality metrics
                centrality = graph_engine.calculate_centrality_metrics()
                
                # Identify duplicates and outliers
                duplicates = graph_engine.identify_duplicates(threshold=0.8)
                outliers = graph_engine.identify_outliers()
                
                # Generate visualization
                graph_viz = graph_engine.visualize_graph()
                
                graph_results = {
                    'centrality_metrics': centrality,
                    'duplicates': duplicates,
                    'outliers': outliers,
                    'visualization': graph_viz
                }
            
            # Initialize RAG chatbot with CV data
            if rag_chatbot and text_results:
                for cv_name, cv_data in text_results.items():
                    cv_text = cv_data.get('full_text', '')
                    rag_chatbot.add_cv(cv_name, cv_text)
            
            # Store results in session
            session_id = str(hash(str(cv_paths)))
            session_data[session_id] = {
                'job_title': job_title,
                'job_description': job_description,
                'text_results': text_results,
                'data_results': data_results,
                'graph_results': graph_results,
                'cv_paths': cv_paths
            }
            session['session_id'] = session_id
            
            return redirect(url_for('cv_demo_results'))
            
        except Exception as e:
            return render_template('cv_demo_step2.html', personal=PERSONAL_INFO, error=f"Error processing CVs: {str(e)}")
    
    return render_template('cv_demo_step2.html', personal=PERSONAL_INFO)

@app.route('/cv-demo/results')
def cv_demo_results():
    """Display CV screening results"""
    if not cv_screening_available:
        return redirect(url_for('cv_screening_demo'))
    
    session_id = session.get('session_id')
    if not session_id or session_id not in session_data:
        return redirect(url_for('cv_demo_step1'))
    
    results = session_data[session_id]
    return render_template('cv_demo_results.html', 
                         personal=PERSONAL_INFO,
                         job_title=results['job_title'],
                         text_results=results.get('text_results', {}),
                         data_results=results.get('data_results', {}),
                         graph_results=results.get('graph_results', {}))

@app.route('/cv-demo/chatbot')
def cv_demo_chatbot():
    """RAG Chatbot interface"""
    if not cv_screening_available or not rag_chatbot:
        return redirect(url_for('cv_screening_demo'))
    
    session_id = session.get('session_id')
    if not session_id or session_id not in session_data:
        return redirect(url_for('cv_demo_step1'))
    
    return render_template('cv_demo_chatbot.html', personal=PERSONAL_INFO)

@app.route('/api/cv-demo/chat', methods=['POST'])
def api_cv_demo_chat():
    """API endpoint for chatbot queries"""
    if not cv_screening_available or not rag_chatbot:
        return jsonify({"error": "Chatbot not available"}), 400
    
    data = request.get_json()
    query = data.get('query', '')
    
    if not query:
        return jsonify({"error": "No query provided"}), 400
    
    try:
        response = rag_chatbot.query(query)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Print configuration
    config.print_config()
    
    print("Running on: http://127.0.0.1:5000\n")
    
    app.run(debug=config.DEBUG, port=5000)
