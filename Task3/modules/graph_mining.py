"""
Graph Mining Module
Builds candidate similarity graphs and calculates centrality metrics
"""
import networkx as nx
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import io
import base64

class GraphMiningEngine:
    def __init__(self, tfidf_vectorizer):
        """Initialize with TF-IDF vectorizer"""
        self.tfidf_vectorizer = tfidf_vectorizer
        self.graph = None
        self.centrality_metrics = {}
    
    def build_similarity_graph(self, cv_data_list, similarity_threshold=0.1):
        """Build candidate similarity graph using dynamic TF-IDF
        
        Args:
            cv_data_list: List of CV data dictionaries
            similarity_threshold: Minimum similarity to create edge (default 0.1)
        """
        from sklearn.feature_extraction.text import TfidfVectorizer
        
        # Create graph
        G = nx.Graph()
        
        # Add nodes (candidates)
        for cv_data in cv_data_list:
            G.add_node(cv_data['candidate_id'])
        
        # Create dynamic TF-IDF vectorizer for this session
        session_vectorizer = TfidfVectorizer(
            max_features=5000,
            stop_words='english',
            ngram_range=(1, 2)
        )
        
        # Vectorize all CVs
        all_cv_texts = [cv['cleaned_text'] for cv in cv_data_list]
        cv_vectors = session_vectorizer.fit_transform(all_cv_texts)
        
        # Calculate pairwise similarities and add edges
        n_candidates = len(cv_data_list)
        
        for i in range(n_candidates):
            for j in range(i + 1, n_candidates):
                # Calculate similarity
                similarity = float(cosine_similarity(cv_vectors[i:i+1], cv_vectors[j:j+1])[0][0])
                
                # Add edge if similarity above threshold
                if similarity >= similarity_threshold:
                    G.add_edge(
                        cv_data_list[i]['candidate_id'],
                        cv_data_list[j]['candidate_id'],
                        weight=similarity
                    )
        
        self.graph = G
        return G
    
    def calculate_centrality_metrics(self):
        """Calculate all centrality metrics"""
        if self.graph is None:
            return {}
        
        G = self.graph
        
        # PageRank
        pagerank = nx.pagerank(G, weight='weight')
        
        # Degree Centrality
        degree_centrality = nx.degree_centrality(G)
        
        # Betweenness Centrality
        betweenness = nx.betweenness_centrality(G, weight='weight')
        
        # Closeness Centrality
        closeness = nx.closeness_centrality(G, distance='weight')
        
        # Combine metrics
        metrics = {}
        for node in G.nodes():
            metrics[node] = {
                'pagerank': pagerank[node],
                'degree_centrality': degree_centrality[node],
                'betweenness': betweenness[node],
                'closeness': closeness[node]
            }
        
        # Sort by PageRank (descending)
        sorted_metrics = dict(sorted(metrics.items(), key=lambda x: x[1]['pagerank'], reverse=True))

        self.centrality_metrics = sorted_metrics
        return sorted_metrics
    
    def identify_duplicates(self, threshold=0.8):
        """Identify potential duplicate candidates based on high similarity"""
        duplicates = []
        
        if self.graph is None:
            return duplicates
        
        # Find edges with weight > threshold
        for u, v, data in self.graph.edges(data=True):
            if data['weight'] >= threshold:
                duplicates.append({
                    'candidate_1': u,
                    'candidate_2': v,
                    'similarity': data['weight']
                })
        
        # Sort by similarity
        duplicates.sort(key=lambda x: x['similarity'], reverse=True)
        
        return duplicates
    
    def identify_outliers(self):
        """Identify outlier candidates (low connectivity)"""
        outliers = []
        
        if self.graph is None:
            return outliers
        
        # Get degree for each node
        degrees = dict(self.graph.degree())
        
        # Find nodes with degree 0 (disconnected) or very low degree
        for node, degree in degrees.items():
            if degree <= 1:  # 0 or 1 connection
                outliers.append({
                    'candidate_id': node,
                    'degree': degree
                })
        
        return outliers
    
    def visualize_graph(self, figsize=(12, 8)):
        """Generate graph visualization
        
        Returns:
            base64-encoded image string
        """
        if self.graph is None or len(self.graph.nodes()) == 0:
            return None
        
        plt.figure(figsize=figsize)
        
        # Layout
        pos = nx.spring_layout(self.graph, k=0.5, iterations=50)
        
        # Node sizes based on degree
        node_sizes = [self.graph.degree(node) * 300 + 200 for node in self.graph.nodes()]
        
        # Node colors based on PageRank
        if self.centrality_metrics:
            node_colors = [self.centrality_metrics[node]['pagerank'] 
                          for node in self.graph.nodes()]
        else:
            node_colors = 'lightblue'
        
        # Draw graph
        nx.draw_networkx_nodes(self.graph, pos,
                              node_size=node_sizes,
                              node_color=node_colors,
                              cmap=plt.cm.YlOrRd,
                              alpha=0.8)
        
        nx.draw_networkx_labels(self.graph, pos,
                               font_size=10,
                               font_weight='bold')
        
        # Draw edges with varying thickness based on weight
        edges = self.graph.edges()
        weights = [self.graph[u][v]['weight'] for u, v in edges]
        
        nx.draw_networkx_edges(self.graph, pos,
                              width=[w * 3 for w in weights],
                              alpha=0.5,
                              edge_color='gray')
        
        plt.title('Candidate Similarity Graph', fontsize=16, fontweight='bold')
        plt.axis('off')
        plt.tight_layout()
        
        # Convert to base64
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.read()).decode()
        plt.close()
        
        return image_base64
