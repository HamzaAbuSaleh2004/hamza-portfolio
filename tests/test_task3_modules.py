# tests/test_task3_modules.py

import os
import sys
import unittest

# Ensure the project root is on the path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(PROJECT_ROOT)

from Task3.modules.graph_mining import GraphMiningEngine
from Task3.modules.rag_chatbot import RAGChatbot
from sklearn.feature_extraction.text import TfidfVectorizer

class TestGraphMiningEngine(unittest.TestCase):
    def setUp(self):
        self.vectorizer = TfidfVectorizer()
        self.engine = GraphMiningEngine(tfidf_vectorizer=self.vectorizer)
        self.cv_data = [
            {'candidate_id': 'c1', 'cleaned_text': 'data science python'},
            {'candidate_id': 'c2', 'cleaned_text': 'machine learning java'}
        ]

    def test_build_similarity_graph(self):
        G = self.engine.build_similarity_graph(self.cv_data, similarity_threshold=0.0)
        self.assertEqual(G.number_of_nodes(), 2)
        # With a low threshold we expect at least one edge
        self.assertGreaterEqual(G.number_of_edges(), 1)

    def test_centrality_metrics(self):
        self.engine.build_similarity_graph(self.cv_data, similarity_threshold=0.0)
        metrics = self.engine.calculate_centrality_metrics()
        self.assertIn('c1', metrics)
        self.assertIn('c2', metrics)
        # PageRank values should sum to 1 (approximately)
        total_pr = sum(m['pagerank'] for m in metrics.values())
        self.assertAlmostEqual(total_pr, 1.0, places=2)

class TestRAGChatbot(unittest.TestCase):
    def setUp(self):
        # Ensure the GEMINI_API_KEY env var is set (dummy value for test)
        os.environ['GEMINI_API_KEY'] = 'test-key'
        self.bot = RAGChatbot()

    def test_initialization(self):
        self.assertIsNotNone(self.bot.embedding_model)
        # Gemini model may be None if the package cannot initialize; that's acceptable for unit test
        self.assertTrue(hasattr(self.bot, 'gemini_model'))

    def test_chunk_text(self):
        text = "word " * 500  # 500 words
        chunks = self.bot.chunk_text(text, chunk_size=100, overlap=20)
        # Expect at least 5 chunks (500/ (100-20) = 6.25 -> 7 chunks)
        self.assertGreaterEqual(len(chunks), 5)
        # Ensure overlap works: the first word of chunk i+1 should appear in the tail of chunk i
        for i in range(len(chunks) - 1):
            tail = chunks[i].split()[-20:]
            head = chunks[i+1].split()[:20]
            self.assertEqual(tail, head)

if __name__ == '__main__':
    unittest.main()
