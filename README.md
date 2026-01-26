# Hamza Abu Saleh - Portfolio Website

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Interactive portfolio website showcasing data science and AI projects, featuring an intelligent CV screening demonstration system.

## 🌟 Features

- **Personal Portfolio**: Comprehensive showcase of projects, skills, and achievements
- **CV Screening Demo**: Advanced demonstration of text mining, data mining, and graph analysis
- **RAG Chatbot**: Retrieval-Augmented Generation chatbot for CV analysis
- **Responsive Design**: Modern, animated UI with glassmorphism effects
- **Demo Mode**: Safe public deployment with zero API costs

## 🚀 Live Demo

Visit the live site: [Add your deployed URL here]

## 📸 Screenshots

### Portfolio Homepage
Check out the live site to see the interactive portfolio with modern design!

### CV Screening Demo
![CV Demo - Step 1](screenshots/cv-screening-demo/Step1.png)
![CV Demo - Results](screenshots/cv-screening-demo/Results%201.png)

### Charging Intelligence Portal
![Charging Portal](screenshots/charging-portal/1.png)

**See more screenshots in the [`screenshots/`](screenshots/) folder:**
- [CV Screening Demo Screenshots](screenshots/cv-screening-demo/) - 8 images
- [Charging Portal Screenshots](screenshots/charging-portal/) - 12 images

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **AI/ML**: NLP, Text Mining, Graph Mining
- **Deployment**: Render / Heroku / Railway (demo mode)

## 📦 Installation

### Demo Mode (Recommended for Public)

```bash
# Clone the repository
git clone https://github.com/yourusername/portfolio.git
cd portfolio

# Install dependencies
pip install -r requirements.txt

# Run the application (demo mode is default)
python portfolio_app.py
```

Visit `http://127.0.0.1:5000`

### Live Mode (Local Development)

```bash
# Create .env file from template
cp .env.example .env

# Edit .env and set:
# PORTFOLIO_DEMO_MODE=False
# GOOGLE_API_KEY=your_actual_api_key

# Run the application
python portfolio_app.py
```

## 📁 Project Structure

```
Portfolio/
├── portfolio_app.py          # Main Flask application
├── config.py                 # Configuration management
├── projects_data.py          # Project portfolio data
├── demo_data.py              # Demo mode sample data
├── static/                   # CSS, JS, images
│   ├── css/
│   ├── js/
│   └── images/
├── templates/                # HTML templates
│   ├── portfolio_*.html      # Portfolio pages
│   └── cv_demo_*.html        # CV screening demo pages
├── Task3/                    # CV screening modules
│   └── modules/
│       ├── text_mining.py
│       ├── data_mining.py
│       ├── graph_mining.py
│       └── rag_chatbot.py
└── Data/                     # ML models (not included)
```

## 🎯 Key Projects Featured

1. **Charging Intelligence Portal** - ML/DL system for EV charging optimization
2. **Advanced CV Screening System** - Multi-stage text and graph mining pipeline
3. **Heart Disease Prediction** - Clinical data analysis and prediction
4. **FinTech Startup (Madmoon)** - Escrow payment solution

## 🔧 Configuration

The application supports two modes via environment variables:

| Variable | Values | Description |
|----------|--------|-------------|
| `PORTFOLIO_DEMO_MODE` | `True` (default) / `False` | Demo uses sample data, Live processes real CVs |
| `GOOGLE_API_KEY` | Your API key | Required only for Live mode |
| `DEBUG` | `True` / `False` | Flask debug mode |

## 🌐 Deployment

### Render (Recommended)

1. Push code to GitHub
2. Create account at [render.com](https://render.com)
3. Create new Web Service
4. Set environment: `PORTFOLIO_DEMO_MODE=True`
5. Deploy!

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions for Render, Heroku, and Railway.

## 📝 License

This project is licensed under the MIT License.

## 👤 Author

**Hamza Abu Saleh**
- LinkedIn: [hamza-abu-saleh](https://www.linkedin.com/in/hamza-abu-saleh-9572b7242/)
- Email: 22110077@htu.edu.jo
- University: Hussein Technical University (HTU)

## 🙏 Acknowledgments

- Hussein Technical University for academic support
- Google Gemini API for AI capabilities (Live mode)
- Open-source community for amazing tools

---

⭐ **Star this repo** if you find it helpful!
