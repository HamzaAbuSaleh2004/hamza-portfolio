# 🚀 Quick Deployment Guide

## Step 1: Upload to GitHub (5 minutes)

### What to Upload:
Upload **ALL files** from `C:\Users\monay\Desktop\Portfolio` **EXCEPT**:
- Don't manually select `.venv/` folder (too large and not needed)
- `.gitignore` will automatically prevent sensitive files

### How to Upload:

1. **Go to** [github.com](https://github.com) and **sign in**

2. **Click** the green "New" button or "+" icon → "New repository"

3. **Fill in:**
   - **Repository name:** `portfolio` (or `data-science-portfolio`)
   - **Description:** `Data Science & AI Portfolio with Interactive CV Screening Demo`
   - **Visibility:** ✅ **Public**
   - **Initialize:** ❌ Leave all checkboxes **unchecked**

4. **Click** "Create repository"

5. On the next page, **click** the blue link: **"uploading an existing file"**

6. **Drag and drop ALL files** from your Portfolio folder into the browser
   - Select everything EXCEPT `.venv` folder
   - Make sure to include hidden files (`.gitignore`, `.env.example`)
   - **Tip:** In Windows Explorer: View → Show → Hidden items

7. **Scroll down**, write commit message: `Initial portfolio with demo mode`

8. **Click** "Commit changes" (green button)

✅ **Done!** Your code is now on GitHub at: `github.com/yourusername/portfolio`

---

## Step 2: Deploy to Render.com (5 minutes)

### 1. Create Render Account

- Go to **https://render.com**
- Click **"Get Started"**
- Sign up with **GitHub** (easiest option)
- Authorize Render to access your repositories

### 2. Create Web Service

- Click **"New +"** (top right)
- Select **"Web Service"**
- Click **"Connect a repository"** (you may need to configure GitHub access)
- Find and select your **`portfolio`** repository

### 3. Configure Your Service

Fill in these settings:

```
Name: hamza-portfolio
Region: Frankfurt (EU Central) or closest to you
Branch: main
Runtime: Python 3
Root Directory: (leave blank)
Build Command: pip install -r requirements.txt
Start Command: python portfolio_app.py
```

### 4. Add Environment Variable

- Click **"Advanced"** to expand
- Click **"Add Environment Variable"**
- Add:
  - **Key:** `PORTFOLIO_DEMO_MODE`
  - **Value:** `True`

### 5. Select Free Plan

- Scroll down to **"Instance Type"**
- Select **"Free"** (750 hours/month)

### 6. Deploy!

- Click **"Create Web Service"** (bottom)
- Wait 3-5 minutes for deployment
- Watch the logs - you'll see:
  ```
  [INFO] Running in DEMO MODE
  Running on: http://127.0.0.1:5000
  ```

### 7. Get Your Live URL

- Once deployed, you'll see: **"Your service is live 🎉"**
- Your URL will be: `https://hamza-portfolio.onrender.com`
- Click it to view your live portfolio!

---

## 🎯 What You'll Have

✅ **Live Portfolio Website** at `https://hamza-portfolio.onrender.com`  
✅ **GitHub Repository** with all your code  
✅ **CV Screening Demo** using sample data (no API costs)  
✅ **Auto-deploy** on every git push  
✅ **Free SSL Certificate** (HTTPS)  
✅ **Professional URL** to share on LinkedIn/Resume

---

## ⚠️ Important Notes

### Free Tier Sleep Mode:
- After **15 minutes of no traffic**, Render puts your app to sleep
- **First visit** after sleep takes 30-60 seconds to wake up
- **Subsequent visits** are instant
- This is normal for free tier - perfect for portfolio!

### Keep it Running:
If you want to prevent sleep before showing to someone:
1. Visit your site 5 minutes before
2. Click around a few pages
3. Now it's warm and ready!

---

## 🔄 Updating Your Portfolio Later

Made changes? Update in 2 steps:

1. **Upload changes to GitHub:**
   - Go to your repo → "Add file" → "Upload files"
   - Drag updated files
   - Commit

2. **Render auto-deploys!**
   - Render detects the change
   - Rebuilds automatically
   - Live in 2-3 minutes

---

## 📝 Troubleshooting

**Problem:** Build failed on Render  
**Solution:** Check that `requirements.txt` is uploaded

**Problem:** App crashes on startup  
**Solution:** Check logs - usually missing files or syntax error

**Problem:** Can't see my changes  
**Solution:** Hard refresh browser (Ctrl+F5) or clear cache

**Problem:** Demo mode not working  
**Solution:** Verify environment variable `PORTFOLIO_DEMO_MODE=True` in Render dashboard

---

## ✨ You're All Set!

Share your portfolio:
- Add to LinkedIn profile
- Include in CV/Resume  
- Send to potential employers
- Share on Twitter/social media

**Your URL:** `https://hamza-portfolio.onrender.com` 🎉
