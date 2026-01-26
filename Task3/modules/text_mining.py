"""
Text Mining Module
Handles CV PDF extraction, text cleaning, and keyword extraction
"""
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import google.generativeai as genai
import os
from dotenv import load_dotenv

class TextMiningEngine:
    def __init__(self, tfidf_vectorizer):
        """Initialize with pre-trained TF-IDF vectorizer and Gemini"""
        self.tfidf_vectorizer = tfidf_vectorizer
        self.feature_names = tfidf_vectorizer.get_feature_names_out()
        
        # Configure Gemini
        load_dotenv()
        api_key = os.getenv('GOOGLE_API_KEY')
        
        if not api_key:
            print("[WARNING] No GOOGLE_API_KEY found in environment. Gemini features will be disabled.")
            self.gemini_model = None
            return
            
        try:
            genai.configure(api_key=api_key)
            self.gemini_model = genai.GenerativeModel('gemini-2.0-flash')
            print("[INFO] Gemini API successfully configured")
        except Exception as e:
            print(f"[WARNING] Could not initialize Gemini in TextMining: {e}")
            self.gemini_model = None
    
    def clean_text(self, text):
        """Clean and preprocess text using simple regex (preserves vocabulary for TF-IDF)"""
        import re
        # Convert to lowercase
        text = text.lower()
        # Remove special characters but keep spaces
        text = re.sub(r'[^a-z0-9\s]', ' ', text)
        # Remove extra whitespace
        text = ' '.join(text.split())
        return text
    
    def extract_text_from_pdf(self, pdf_file):
        """Extract text from PDF file page by page
        
        Returns:
            dict: {page_number: text_content}
        """
        page_texts = {}
        try:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                page_texts[page_num + 1] = text  # 1-indexed pages
        except Exception as e:
            print(f"Error extracting PDF: {e}")
            page_texts[1] = ""
        
        return page_texts
    
    def process_cv(self, pdf_file, candidate_id):
        """Process a single CV PDF
        
        Returns:
            dict: CV data with page texts, cleaned text, keywords
        """
        # Extract text per page
        page_texts = self.extract_text_from_pdf(pdf_file)
        
        # Combine all pages for full text
        full_text = ' '.join(page_texts.values())
        cleaned_text = self.clean_text(full_text)
        
        # Extract keywords using TF-IDF
        keywords = self.extract_keywords(cleaned_text, top_n=15)
        
        # Find evidence snippets for top keywords
        evidence_snippets = self.find_evidence_snippets(page_texts, keywords[:10])
        
        return {
            'candidate_id': candidate_id,
            'page_texts': page_texts,
            'full_text': full_text,
            'cleaned_text': cleaned_text,
            'keywords': keywords,
            'evidence_snippets': evidence_snippets
        }
    
    def extract_keywords(self, text, top_n=15):
        """Extract top keywords using TF-IDF"""
        try:
            # Vectorize the text
            tfidf_vector = self.tfidf_vectorizer.transform([text])
            
            # Get scores
            scores = tfidf_vector.toarray()[0]
            
            # Get top indices
            top_indices = scores.argsort()[-top_n:][::-1]
            
            # Get keywords with scores
            keywords = [(self.feature_names[idx], float(scores[idx])) 
                       for idx in top_indices if scores[idx] > 0]
            
            return keywords
        except:
            return []
    
    def find_evidence_snippets(self, page_texts, keywords, snippet_length=100):
        """Find evidence snippets for keywords with page numbers"""
        evidence = []
        
        for keyword, score in keywords:
            for page_num, text in page_texts.items():
                # Find keyword in text (case insensitive)
                text_lower = text.lower()
                keyword_lower = keyword.lower()
                
                if keyword_lower in text_lower:
                    # Find position
                    pos = text_lower.find(keyword_lower)
                    
                    # Extract snippet around keyword
                    start = max(0, pos - snippet_length//2)
                    end = min(len(text), pos + len(keyword) + snippet_length//2)
                    snippet = text[start:end].strip()
                    
                    # Add ellipsis if needed
                    if start > 0:
                        snippet = "..." + snippet
                    if end < len(text):
                        snippet = snippet + "..."
                    
                    evidence.append({
                        'keyword': keyword,
                        'page': page_num,
                        'snippet': snippet,
                        'score': score
                    })
                    break  # Only first occurrence
        
        return evidence
    
    def process_vacancy(self, title, description):
        """Process vacancy text"""
        combined_text = f"{title} {description}"
        cleaned_text = self.clean_text(combined_text)
        
        # Extract keywords
        keywords = self.extract_keywords(cleaned_text, top_n=10)
        
        return {
            'title': title,
            'description': description,
            'cleaned_text': cleaned_text,
            'keywords': keywords
        }
