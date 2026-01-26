"""
Data Mining Module
Handles vacancy clustering, candidate ranking, and skill matching
"""
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Cluster labels from Task 1
CLUSTER_LABELS = {
    0: "Medical & Lab Science",
    1: "Project/Product Management",
    2: "Data Engineering & Cloud",
    3: "Data Science & Analytics",
    4: "AI & Machine Learning"
}

# Top keywords for each cluster (from Task 1)
CLUSTER_KEYWORDS = {
    0: ["laboratory", "medical", "technologist", "mlt", "ascp", "clinical", "testing", "specimens", "chemistry"],
    1: ["data", "management", "skills", "database", "communication", "project", "business", "analysis", "team"],
    2: ["data", "azure", "aws", "cloud", "engineering", "spark", "etl", "pipeline", "warehouse"],
    3: ["data", "analysis", "business", "management", "analytics", "reporting", "sql", "insights"],
    4: ["learning", "machine", "data", "ml", "ai", "model", "science", "python", "deep"]
}

class DataMiningEngine:
    def __init__(self, kmeans_model, tfidf_vectorizer):
        """Initialize with pre-trained models"""
        self.kmeans_model = kmeans_model
        self.tfidf_vectorizer = tfidf_vectorizer
    
    def classify_vacancy(self, vacancy_cleaned_text):
        """Classify vacancy into job cluster"""
        # Vectorize vacancy
        vacancy_vector = self.tfidf_vectorizer.transform([vacancy_cleaned_text])
        
        # Predict cluster
        cluster_id = int(self.kmeans_model.predict(vacancy_vector)[0])
        cluster_label = CLUSTER_LABELS.get(cluster_id, "General IT")
        cluster_keywords = CLUSTER_KEYWORDS.get(cluster_id, [])
        
        return {
            'cluster_id': cluster_id,
            'cluster_label': cluster_label,
            'cluster_keywords': cluster_keywords
        }
    
    def calculate_similarity(self, vacancy_vector, cv_vector):
        """Calculate cosine similarity between vacancy and CV"""
        similarity = float(cosine_similarity(vacancy_vector, cv_vector)[0][0])
        return similarity
    
    def rank_candidates(self, vacancy_cleaned_text, cv_data_list):
        """Rank candidates by similarity to vacancy using dynamic TF-IDF"""
        from sklearn.feature_extraction.text import TfidfVectorizer
        
        # Create a fresh TF-IDF vectorizer for this session
        # This ensures it knows the vocabulary in the current vacancy and CVs
        session_vectorizer = TfidfVectorizer(
            max_features=5000,
            stop_words='english',
            ngram_range=(1, 2)
        )
        
        # Prepare all documents: vacancy + all CVs
        all_documents = [vacancy_cleaned_text] + [cv['cleaned_text'] for cv in cv_data_list]
        
        # Fit and transform all documents
        tfidf_matrix = session_vectorizer.fit_transform(all_documents)
        
        # First row is vacancy, rest are CVs
        vacancy_vector = tfidf_matrix[0:1]
        cv_vectors = tfidf_matrix[1:]
        
        # Calculate similarities
        ranked_candidates = []
        for idx, cv_data in enumerate(cv_data_list):
            cv_vector = cv_vectors[idx:idx+1]
            similarity = self.calculate_similarity(vacancy_vector, cv_vector)
            
            ranked_candidates.append({
                'candidate_id': cv_data['candidate_id'],
                'similarity_score': similarity,
                'cv_data': cv_data
            })
        
        # Sort by similarity (descending)
        ranked_candidates.sort(key=lambda x: x['similarity_score'], reverse=True)
        
        return ranked_candidates
    
    def extract_skills_from_text(self, text):
        """Extract potential skills from text (simple keyword matching)"""
        # Common IT skills (simplified)
        skill_keywords = [
            'python', 'java', 'javascript', 'c++', 'sql', 'nosql',
            'machine learning', 'deep learning', 'ai', 'data science',
            'aws', 'azure', 'cloud', 'docker', 'kubernetes',
            'react', 'angular', 'vue', 'node',
            'mysql', 'postgresql', 'mongodb',
            'git', 'agile', 'scrum',
            'pandas', 'numpy', 'tensorflow', 'pytorch',
            'spark', 'hadoop', 'etl', 'pipeline',
            'tableau', 'power bi', 'excel'
        ]
        
        text_lower = text.lower()
        found_skills = [skill for skill in skill_keywords if skill in text_lower]
        return found_skills
    
    def match_skills(self, vacancy_text, cv_text):
        """Match skills between vacancy and CV"""
        vacancy_skills = set(self.extract_skills_from_text(vacancy_text))
        cv_skills = set(self.extract_skills_from_text(cv_text))
        
        matched_skills = vacancy_skills.intersection(cv_skills)
        missing_skills = vacancy_skills.difference(cv_skills)
        
        return {
            'matched_skills': list(matched_skills),
            'missing_skills': list(missing_skills),
            'match_percentage': len(matched_skills) / len(vacancy_skills) * 100 if vacancy_skills else 0
        }
    
    def generate_shortlist(self, ranked_candidates, vacancy_text, top_n=5):
        """Generate shortlist with skill matching"""
        shortlist = []
        
        for candidate in ranked_candidates[:top_n]:
            cv_data = candidate['cv_data']
            
            # Match skills
            skill_match = self.match_skills(vacancy_text, cv_data['full_text'])
            
            shortlist.append({
                'candidate_id': candidate['candidate_id'],
                'similarity_score': candidate['similarity_score'],
                'matched_skills': skill_match['matched_skills'],
                'missing_skills': skill_match['missing_skills'],
                'match_percentage': skill_match['match_percentage'],
                'keywords': cv_data['keywords']
            })
        
        return shortlist
