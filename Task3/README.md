# Recruitment Portal

## Overview
A portal for screening candidates using:
- CV Analysis
- Clustering & Ranking
- Candidate Graph
- Chatbot

## How to Run

1. **Install Requirements**
   `pip install -r requirements.txt`

2. **API Key**
   Add your Gemini API key to `.env`.

3. **Check Models**
   Ensure `tfidf_vectorizer.pkl` and `kmeans_model.pkl` are in `../Data/`.

4. **Start App**
   `python app.py`
   Go to `http://127.0.0.1:5000`

## Features
- **Upload**: Submit vacancy and CVs.
- **Results**: See rankings and graphs.
- **Chat**: Ask questions about candidates.
