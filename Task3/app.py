"""
Flask Application for Recruitment Screening Portal
Integrates text mining, data mining, graph mining, and RAG chatbot
"""
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os
import pickle
from werkzeug.utils import secure_filename
import sys

# Add modules to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from modules.text_mining import TextMiningEngine
from modules.data_mining import DataMiningEngine
from modules.graph_mining import GraphMiningEngine
from modules.rag_chatbot import RAGChatbot

app = Flask(__name__)
app.secret_key = 'techhire_recruitment_portal_2024'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load pre-trained models from Task 1
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'Data')

try:
    with open(os.path.join(MODEL_PATH, 'tfidf_vectorizer.pkl'), 'rb') as f:
        tfidf_vectorizer = pickle.load(f)
    
    with open(os.path.join(MODEL_PATH, 'kmeans_model.pkl'), 'rb') as f:
        kmeans_model = pickle.load(f)
    
    print("[OK] Models loaded successfully")
except Exception as e:
    print(f"[ERROR] Error loading models: {e}")
    tfidf_vectorizer = None
    kmeans_model = None

# Initialize engines
text_engine = TextMiningEngine(tfidf_vectorizer) if tfidf_vectorizer else None
data_engine = DataMiningEngine(kmeans_model, tfidf_vectorizer) if kmeans_model and tfidf_vectorizer else None
graph_engine = GraphMiningEngine(tfidf_vectorizer) if tfidf_vectorizer else None
rag_chatbot = RAGChatbot()

# Global storage for session data (in production, use database)
session_data = {}


@app.route('/')
def index():
    """Homepage"""
    return render_template('index.html')


@app.route('/step1', methods=['GET', 'POST'])
def step1():
    """Step 1: Input Vacancy Details"""
    if request.method == 'POST':
        vacancy_title = request.form.get('vacancy_title', '')
        vacancy_description = request.form.get('vacancy_description', '')
        
        if not vacancy_title or not vacancy_description:
            return render_template('step1_vacancy.html', error="Please provide vacancy title and description", 
                                 vacancy_title=vacancy_title, vacancy_description=vacancy_description)
        
        # Check if engines are initialized
        if not text_engine or not data_engine:
            return render_template('step1_vacancy.html', error="Models not loaded. Please ensure Task 1 models exist.")

        # Process vacancy immediately to get cluster
        vacancy_data = text_engine.process_vacancy(vacancy_title, vacancy_description)
        cluster_info = data_engine.classify_vacancy(vacancy_data['cleaned_text'])
        
        # Store in session for Step 2
        session['vacancy_title'] = vacancy_title
        session['vacancy_description'] = vacancy_description
        session['vacancy_data'] = vacancy_data
        session['cluster_info'] = cluster_info
        
        return redirect(url_for('step2'))
        
    return render_template('step1_vacancy.html')


@app.route('/step2', methods=['GET', 'POST'])
def step2():
    """Step 2: Upload CVs"""
    # Verify Step 1 is done
    vacancy_title = session.get('vacancy_title')
    cluster_info = session.get('cluster_info')
    
    if not vacancy_title:
        return redirect(url_for('step1'))
    
    # Format cluster label for display
    cluster_label = f"Cluster {cluster_info['cluster_id']}: {', '.join(cluster_info['cluster_keywords'][:3])}" if cluster_info else "Unknown"

    if request.method == 'POST':
        cv_files = request.files.getlist('cv_files')
        
        if not cv_files or len(cv_files) == 0:
            return render_template('step2_cvs.html', error="Please upload at least one CV", 
                                 vacancy_title=vacancy_title, cluster_label=cluster_label)
        
        if len(cv_files) > 10:
            return render_template('step2_cvs.html', error="Maximum 10 CVs allowed", 
                                 vacancy_title=vacancy_title, cluster_label=cluster_label)
        
        # Retrieve vacancy data
        vacancy_data = session.get('vacancy_data')
        
        # Process CVs (using Gemini logic inside text_engine)
        cv_data_list = []
        for idx, cv_file in enumerate(cv_files):
            if cv_file and cv_file.filename.endswith('.pdf'):
                candidate_id = f"CV_{idx+1:02d}"
                # Note: verify files are at start of stream if needed, usually flask handles this
                cv_data = text_engine.process_cv(cv_file, candidate_id)
                cv_data_list.append(cv_data)
        
        if len(cv_data_list) == 0:
            return render_template('step2_cvs.html', error="No valid PDF files processed", 
                                 vacancy_title=vacancy_title, cluster_label=cluster_label)
        
        # Rank candidates
        ranked_candidates = data_engine.rank_candidates(
            vacancy_data['cleaned_text'], 
            cv_data_list
        )
        
        # Generate shortlist
        shortlist = data_engine.generate_shortlist(
            ranked_candidates,
            vacancy_data['description'],
            top_n=min(5, len(ranked_candidates))
        )
        
        # Build graph
        if graph_engine:
            graph_engine.build_similarity_graph(cv_data_list, similarity_threshold=0.1)
            centrality_metrics = graph_engine.calculate_centrality_metrics()
            duplicates = graph_engine.identify_duplicates(threshold=0.8)
            outliers = graph_engine.identify_outliers()
            graph_image = graph_engine.visualize_graph()
        else:
            centrality_metrics = {}
            duplicates = []
            outliers = []
            graph_image = None
        
        # Build RAG vector database
        num_chunks = rag_chatbot.build_vector_db(cv_data_list)
        
        # Store comprehensive session data
        session_id = str(hash(vacancy_title + str(len(cv_data_list))))
        session_data[session_id] = {
            'vacancy': vacancy_data,
            'cluster_info': cluster_info,
            'cv_data_list': cv_data_list,
            'ranked_candidates': ranked_candidates,
            'shortlist': shortlist,
            'centrality_metrics': centrality_metrics,
            'duplicates': duplicates,
            'outliers': outliers,
            'graph_image': graph_image,
            'num_chunks': num_chunks
        }
        
        session['session_id'] = session_id
        
        return redirect(url_for('results'))

    return render_template('step2_cvs.html', vacancy_title=vacancy_title, cluster_label=cluster_label)


@app.route('/results')
def results():
    """Display all analysis results"""
    session_id = session.get('session_id')
    
    if not session_id or session_id not in session_data:
        return redirect(url_for('upload'))
    
    data = session_data[session_id]
    
    return render_template('results.html', data=data)


@app.route('/chatbot')
def chatbot():
    """RAG Chatbot interface"""
    session_id = session.get('session_id')
    
    if not session_id or session_id not in session_data:
        return redirect(url_for('upload'))
    
    data = session_data[session_id]
    
    return render_template('chatbot.html', 
                         shortlist=data['shortlist'],
                         num_chunks=data['num_chunks'])


@app.route('/api/chat', methods=['POST'])
def api_chat():
    """API endpoint for chatbot queries"""
    session_id = session.get('session_id')
    
    if not session_id or session_id not in session_data:
        return jsonify({'error': 'No active session'}), 400
    
    query = request.json.get('query', '')
    
    if not query:
        return jsonify({'error': 'No query provided'}), 400
    
    # Retrieve relevant chunks
    relevant_chunks = rag_chatbot.retrieve_relevant_chunks(query, top_k=10)
    
    # Generate response
    response_data = rag_chatbot.generate_response(query, relevant_chunks)
    
    return jsonify(response_data)


@app.route('/api/interview_questions/<candidate_id>')
def api_interview_questions(candidate_id):
    """Generate interview questions for a candidate"""
    session_id = session.get('session_id')
    
    if not session_id or session_id not in session_data:
        return jsonify({'error': 'No active session'}), 400
    
    data = session_data[session_id]
    
    # Find candidate CV data
    cv_data = None
    for cv in data['cv_data_list']:
        if cv['candidate_id'] == candidate_id:
            cv_data = cv
            break
    
    if not cv_data:
        return jsonify({'error': 'Candidate not found'}), 404
    
    # Generate questions
    questions = rag_chatbot.generate_interview_questions(
        candidate_id,
        cv_data,
        data['vacancy']['description'],
        num_questions=5
    )
    
    return jsonify({'questions': questions})


if __name__ == '__main__':
    if not tfidf_vectorizer or not kmeans_model:
        print("\n[WARNING] Models not loaded. Please ensure tfidf_vectorizer.pkl and kmeans_model.pkl exist in ../Data/")
        print("Run Task 1 notebook first to generate these models.\n")
    
    print("\n" + "="*60)
    print("TechHire Recruitment Screening Portal")
    print("="*60)
    print("Running on: http://127.0.0.1:5000")
    print("="*60 + "\n")
    
    app.run(debug=True, port=5000)
