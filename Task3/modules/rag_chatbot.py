"""
RAG Chatbot Module
Evidence-based Q&A using FAISS and Gemini API
"""

import os
from sentence_transformers import SentenceTransformer
import faiss
import google.generativeai as genai
import google.generativeai as genai
import time
import re

from dotenv import load_dotenv

class RAGChatbot:
    def __init__(self):
        """Initialize RAG chatbot"""
        # Load environment variables
        env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
        load_dotenv(env_path)
        
        # Initialize embedding model
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Initialize Gemini
        api_key = os.getenv("GEMINI_API_KEY")
        
        try:
            genai.configure(api_key=api_key)
            self.gemini_model = genai.GenerativeModel('gemini-2.0-flash')
        except Exception as e:
            print(f"[WARNING] Could not initialize Gemini API: {e}")
            self.gemini_model = None
        
        # FAISS index
        self.index = None
        self.chunks_data = []

    def _generate_with_retry(self, prompt, max_retries=5, initial_delay=10):
        """Generates content with retry logic for rate limits"""
        for attempt in range(max_retries):
            try:
                return self.gemini_model.generate_content(prompt)
            except Exception as e:
                error_str = str(e)
                if "429" in error_str or "Quota exceeded" in error_str:
                    if attempt < max_retries - 1:
                        # Default backoff
                        wait_time = initial_delay * (2 ** attempt)
                        
                        # Try to parse exact wait time from error message
                        # Look for "Please retry in X.Xs."
                        match = re.search(r"retry in ([0-9.]+)s", error_str)
                        if match:
                            wait_time = float(match.group(1)) + 2.0  # Add 2s buffer
                        
                        print(f"[WARNING] Rate limit hit. Waiting {wait_time:.1f} seconds before retry {attempt+1}/{max_retries}...")
                        time.sleep(wait_time)
                        continue
                raise e
    
    def chunk_text(self, text, chunk_size=400, overlap=50):
        """Chunk text with overlap
        
        Args:
            text: Text to chunk
            chunk_size: Target chunk size in tokens (approx. 300-600)
            overlap: Overlap size in tokens (approx. 50-100)
        
        Returns:
            List of text chunks
        """
        # Simple word-based chunking (approximation of tokens)
        words = text.split()
        chunks = []
        
        start = 0
        while start < len(words):
            end = start + chunk_size
            chunk = ' '.join(words[start:end])
            chunks.append(chunk)
            start += (chunk_size - overlap)
        
        return chunks
    
    def build_vector_db(self, cv_data_list):
        """Build FAISS vector database from CV chunks
        
        Args:
            cv_data_list: List of processed CV data
        """
        all_chunks = []
        
        # Chunk each CV's page texts
        for cv_data in cv_data_list:
            candidate_id = cv_data['candidate_id']
            page_texts = cv_data['page_texts']
            
            for page_num, text in page_texts.items():
                if len(text.strip()) == 0:
                    continue
                
                chunks = self.chunk_text(text)
                
                for chunk_id, chunk in enumerate(chunks):
                    all_chunks.append({
                        'candidate_id': candidate_id,
                        'page': page_num,
                        'chunk_id': chunk_id,
                        'text': chunk
                    })
        
        # Generate embeddings
        chunk_texts = [chunk['text'] for chunk in all_chunks]
        embeddings = self.embedding_model.encode(chunk_texts, show_progress_bar=False)
        
        # Build FAISS index
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings.astype('float32'))
        
        # Store chunk data
        self.chunks_data = all_chunks
        
        return len(all_chunks)
    
    def retrieve_relevant_chunks(self, query, top_k=10):
        """Retrieve top-k most relevant chunks for query
        
        Args:
            query: User query string
            top_k: Number of chunks to retrieve (8-15)
        
        Returns:
            List of relevant chunks with metadata
        """
        if self.index is None:
            return []
        
        # Embed query
        query_embedding = self.embedding_model.encode([query])
        
        # Search
        distances, indices = self.index.search(query_embedding.astype('float32'), top_k)
        
        # Get relevant chunks
        relevant_chunks = []
        for i, idx in enumerate(indices[0]):
            if idx < len(self.chunks_data):
                chunk_data = self.chunks_data[idx]
                relevant_chunks.append({
                    'candidate_id': chunk_data['candidate_id'],
                    'page': chunk_data['page'],
                    'text': chunk_data['text'],
                    'distance': float(distances[0][i])
                })
        
        return relevant_chunks
    
    def format_context(self, relevant_chunks):
        """Format retrieved chunks as context for Gemini"""
        context = "Retrieved Evidence:\n\n"
        
        for i, chunk in enumerate(relevant_chunks):
            context += f"[Source {i+1}: Candidate {chunk['candidate_id']}, Page {chunk['page']}]\n"
            context += f"{chunk['text']}\n\n"
        
        return context
    
    def generate_response(self, query, relevant_chunks):
        """Generate response using Gemini with retrieved evidence
        
        Returns:
            dict with response and citations
        """
        if self.gemini_model is None:
            return {
                'response': "Gemini API key not configured. Please set GEMINI_API_KEY in .env file.",
                'citations': [],
                'has_evidence': False
            }
        
        if not relevant_chunks:
            return {
                'response': "Not found in CV.",
                'citations': [],
                'has_evidence': False,
                'debug': "No supporting evidence retrieved."
            }
        
        # Format context
        context = self.format_context(relevant_chunks)
        
        # Create prompt
        prompt = f"""You are a recruitment assistant. Answer the question ONLY based on the retrieved evidence below.

{context}

Question: {query}

IMPORTANT RULES:
1. Answer ONLY using information from the retrieved evidence above
2. Cite your sources using format: (Candidate [ID], Page [NUM], "[short quote]")
3. If the evidence doesn't contain the answer, respond with: "Not found in CV."
4. Be concise and precise

Answer:"""
        
        try:
            # Generate response
            response = self._generate_with_retry(prompt)
            answer = response.text
            
            # Extract citations (candidates and pages mentioned)
            citations = self._extract_citations(answer, relevant_chunks)
            
            return {
                'response': answer,
                'citations': citations,
                'has_evidence': True,
                'retrieved_chunks': relevant_chunks
            }
        
        except Exception as e:
            return {
                'response': f"Error generating response: {str(e)}",
                'citations': [],
                'has_evidence': False
            }
    
    def _extract_citations(self, text, chunks):
        """Extract citation information from response"""
        citations = []
        
        # Simple extraction: find candidate IDs and pages mentioned
        for chunk in chunks:
            candidate_id = chunk['candidate_id']
            page = chunk['page']
            
            if candidate_id in text or f"Candidate {candidate_id}" in text:
                citations.append({
                    'candidate_id': candidate_id,
                    'page': page
                })
        
        return citations
    
    def generate_interview_questions(self, candidate_id, cv_data, vacancy_text, num_questions=5):
        """Generate tailored interview questions for a candidate
        
        Args:
            candidate_id: Candidate ID
            cv_data: CV data for the candidate
            vacancy_text: Vacancy requirements
            num_questions: Number of questions to generate
        """
        if self.gemini_model is None:
            return ["Gemini API key not configured."]
        
        # Get candidate's relevant chunks
        prompt = f"""Based on the candidate's CV and the job vacancy, generate {num_questions} tailored interview questions.

Vacancy: {vacancy_text}

Candidate CV Key Points:
{cv_data['full_text'][:2000]}

Generate {num_questions} specific interview questions that:
1. Probe the candidate's experience mentioned in their CV
2. Relate to the vacancy requirements
3. Include technical and behavioral questions
4. Reference specific skills or projects from the CV

Format:
1. [Question Text]
   - Evidence: [Quote specific project/experience from CV]

2. [Question Text] ..."""
        
        try:
            response = self._generate_with_retry(prompt)
            questions_text = response.text
            
            # Parse questions
            questions = []
            for line in questions_text.split('\n'):
                line = line.strip()
                if line and (line[0].isdigit() or line.startswith('-')):
                    questions.append(line)
            
            return questions if questions else [questions_text]
        
        except Exception as e:
            return [f"Error generating questions: {str(e)}"]
