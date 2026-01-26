# Portfolio Deployment Guide

This guide explains how to deploy your portfolio application in both **Demo Mode** (public deployment) and **Live Mode** (local development with real API).

## Quick Start

### Demo Mode (Default - For Public Deployment)

Demo mode uses pre-computed sample data and makes **no API calls**. Safe for public deployment without exposing secrets.

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Portfolio
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set demo mode** (optional, already default)
   ```bash
   # Windows
   set PORTFOLIO_DEMO_MODE=True
   
   # Mac/Linux
   export PORTFOLIO_DEMO_MODE=True
   ```

4. **Run the application**
   ```bash
   python portfolio_app.py
   ```

5. **Visit**: `http://127.0.0.1:5000/cv-screening-demo`

✅ **Result**: Visitors can explore the CV screening feature with sample results - no costs, no API keys needed!

---

### Live Mode (For Local Development with Real API)

Live mode processes real uploaded CVs using Gemini API. Requires API key.

1. **Get Google Gemini API Key**
   - Visit: https://makersuite.google.com/app/apikey
   - Create and copy your API key

2. **Create `.env` file**
   ```bash
   cp .env.example .env
   ```

3. **Edit `.env` file**
   ```env
   PORTFOLIO_DEMO_MODE=False
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

4. **Run the application**
   ```bash
   python portfolio_app.py
   ```

5. **Upload real PDFs**: System will process them using the API

⚠️ **Note**: Live mode makes real API calls and may incur costs.

---

## Deployment Options

### ⚠️ Important: Flask vs Static Sites

**Your portfolio is a Flask application (Python backend), NOT a static site.**

- ❌ **Won't work**: GitHub Pages, Cloudflare Pages, Netlify (static only)
- ✅ **Will work**: Render, Railway, Heroku, PythonAnywhere (support Python backends)

---

## Recommended Deployment Platforms (FREE Tier Available)

### 1. Render.com (⭐ RECOMMENDED - Easiest)

**Free Tier:** 750 hours/month, automatic sleep after inactivity

**Steps:**

1. **Push to GitHub first** (see GITHUB_UPLOAD_CHECKLIST.md)

2. **Create Render Account**
   - Go to https://render.com
   - Sign up with GitHub

3. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Select "Connect a repository"
   - Choose your `portfolio` repository

4. **Configure Service:**
   ```
   Name: hamza-portfolio
   Region: Choose closest to you
   Branch: main
   Root Directory: (leave empty)
   Runtime: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: python portfolio_app.py
   ```

5. **Set Environment Variables:**
   - Click "Advanced" → "Add Environment Variable"
   - Add: `PORTFOLIO_DEMO_MODE` = `True`

6. **Deploy!**
   - Click "Create Web Service"
   - Wait 3-5 minutes for first deployment
   - You'll get a URL like: `https://hamza-portfolio.onrender.com`

**Pros:** Auto-deploys on git push, free SSL, easy setup  
**Cons:** Sleeps after 15min inactivity (wakes in 30-60 seconds)

---

### 2. Railway.app (Great Alternative)

**Free Tier:** $5 credit/month (usually enough for portfolio)

**Steps:**

1. **Visit** https://railway.app and sign in with GitHub

2. **New Project** → "Deploy from GitHub repo"

3. **Select** your portfolio repository

4. **Add Variables:**
   - Click "Variables" tab
   - Add: `PORTFOLIO_DEMO_MODE=True`

5. **Settings:**
   - Start Command: `python portfolio_app.py`
   - Auto-deploy on push: ✅

6. **Generate Domain**
   - Go to "Settings" → "Domains"
   - Click "Generate Domain"
   - You'll get: `https://your-app.up.railway.app`

**Pros:** Fast deployments, generous free tier, excellent UI  
**Cons:** $5/month limit (monitor usage)

---

### 3. PythonAnywhere (Python-Specific Hosting)

**Free Tier:** Unlimited time, but slower speed

**Steps:**

1. **Create Account** at https://www.pythonanywhere.com

2. **Upload Code:**
   - Go to "Files" tab
   - Upload your entire portfolio folder
   - Or clone from GitHub

3. **Create Web App:**
   - Go to "Web" tab → "Add a new web app"
   - Choose "Manual configuration" → Python 3.10
   - Set source code directory: `/home/yourusername/portfolio`

4. **Configure WSGI:**
   - Edit WSGI configuration file
   - Update to point to your `portfolio_app.py`

5. **Install Dependencies:**
   - Open Bash console
   - Run: `pip install -r requirements.txt --user`

6. **Set Environment Variable:**
   - Go to Web tab → Environment variables
   - Add: `PORTFOLIO_DEMO_MODE=True`

7. **Reload** the web app

**Pros:** Always on (no sleep), Python-focused, beginner-friendly  
**Cons:** Slower than Render/Railway, custom domain requires paid tier

---

### 4. Heroku (Classic Option)

**Note:** Heroku removed free tier in 2022, now requires credit card for $5/month minimum

1. **Install Heroku CLI**

2. **Create `Procfile`**:
   ```
   web: python portfolio_app.py
   ```

3. **Deploy**:
   ```bash
   heroku create your-portfolio-name
   heroku config:set PORTFOLIO_DEMO_MODE=True
   git push heroku main
   ```

**Pros:** Industry standard, reliable  
**Cons:** No longer free

---

## Switching Between Modes

### To Demo Mode (Public):
```bash
# Set environment variable
set PORTFOLIO_DEMO_MODE=True  # Windows
export PORTFOLIO_DEMO_MODE=True  # Mac/Linux

# Or edit .env file
PORTFOLIO_DEMO_MODE=True
```

### To Live Mode (Local):
```bash
# Set environment variable
set PORTFOLIO_DEMO_MODE=False  # Windows
export PORTFOLIO_DEMO_MODE=False  # Mac/Linux

# And provide API key in .env
GOOGLE_API_KEY=your_key_here
```

---

## Security Checklist

Before pushing to GitHub:

- [ ] `.env` file is in `.gitignore`
- [ ] No API keys in code
- [ ] `.env.example` exists (template only, no real keys)
- [ ] `PORTFOLIO_DEMO_MODE=True` in production environment variables
- [ ] Test demo mode locally before deploying

---

## Troubleshooting

### Demo Mode Not Working?
1. Check environment variable: `echo %PORTFOLIO_DEMO_MODE%` (Windows) or `echo $PORTFOLIO_DEMO_MODE` (Mac/Linux)
2. Verify startup message shows "DEMO MODE"
3. Clear browser cache and restart Flask app

### Live Mode: API Key Error?
1. Verify `.env` file exists and contains `GOOGLE_API_KEY`
2. Check API key is valid at https://makersuite.google.com
3. Ensure `python-dotenv` is installed: `pip install python-dotenv`

### Permission Errors on Deployment?
1. Ensure `requirements.txt` includes all dependencies
2. Check Python version compatibility (3.8+)
3. Verify environment variables are set in platform dashboard

---

## Cost Management

**Demo Mode**: **$0** - No API calls
**Live Mode**: Usage-based pricing from Google Gemini API

To minimize costs in live mode:
- Use demo mode for public visitors
- Enable live mode only for personal testing
- Set API rate limits in Google Cloud Console
- Monitor usage in Google Cloud dashboard

---

## Support

For issues or questions:
- Check `.env.example` for configuration reference
- Verify all files in `.gitignore` are not committed
- Test locally before deploying

Happy deploying! 🚀
