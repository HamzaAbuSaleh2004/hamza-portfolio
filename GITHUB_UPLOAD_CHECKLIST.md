# GitHub Upload Checklist

## ✅ Completed Steps

- [x] Created `screenshots/` folder with organized project screenshots
- [x] Moved CV screening demo screenshots to `screenshots/cv-screening-demo/`
- [x] Added Charging Portal screenshots to `screenshots/charging-portal/`
- [x] Created README.md for main portfolio
- [x] Created README.md for screenshots folder

## 🗑️ Files/Folders to DELETE Before Upload

### Required Deletions (Must Delete):
- [ ] `.venv/` - Virtual environment (large, auto-generated)
- [ ] `antigravity_portfolio_brief.json` - Planning document
- [ ] `antigravity_portfolio_brief.md` - Planning document  
- [ ] `Web_Test_job.txt` - Test file
- [ ] `Task1/` - Assignment notebooks (not needed for portfolio)
- [ ] `Task2/` - Assignment notebooks (not needed for portfolio)

### Optional Deletions (Recommended):
- [ ] `tests/` folder - If you want to keep unit tests, KEEP it; otherwise DELETE
- [ ] `Data/` folder - Contains large .pkl model files (already in .gitignore, but can delete to reduce size)

**Total Space Saved: ~5-10 MB**

## 📁 Final Folder Structure (After Cleanup)

```
Portfolio/
├── .env.example              ✅ KEEP - Template for environment variables
├── .gitignore                ✅ KEEP - Prevents sensitive files from upload
├── README.md                 ✅ KEEP - Main documentation
├── DEPLOYMENT.md             ✅ KEEP - Deployment instructions
├── config.py                 ✅ KEEP - Configuration file
├── demo_data.py              ✅ KEEP - Demo mode sample data
├── portfolio_app.py          ✅ KEEP - Main Flask application
├── projects_data.py          ✅ KEEP - Project information
├── requirements.txt          ✅ KEEP - Python dependencies
├── screenshots/              ✅ KEEP - Project screenshots
│   ├── README.md
│   ├── cv-screening-demo/    (8 images)
│   └── charging-portal/      (12 images)
├── static/                   ✅ KEEP - CSS, JS, images
│   ├── css/
│   ├── images/
│   └── js/
├── templates/                ✅ KEEP - HTML templates
│   ├── portfolio_*.html
│   └── cv_demo_*.html
├── Task3/                    ✅ KEEP - CV screening modules
│   └── modules/
└── tests/                    ⚠️  OPTIONAL - Keep if useful
```

## 🚀 Upload Steps

### 1. Delete Unnecessary Files (Run These Commands):

```powershell
# Navigate to portfolio folder
cd C:\Users\monay\Desktop\Portfolio

# Delete virtual environment (large)
Remove-Item -Recurse -Force .venv

# Delete planning documents
Remove-Item -Force antigravity_portfolio_brief.json, antigravity_portfolio_brief.md, Web_Test_job.txt

# Delete assignment folders
Remove-Item -Recurse -Force Task1, Task2

# Optional: Delete tests folder
# Remove-Item -Recurse -Force tests
```

### 2. Upload to GitHub:

1. **Go to** [github.com](https://github.com) and sign in
2. **Click** the "+" icon (top right) → "New repository"
3. **Configure:**
   - Repository name: `portfolio` or `data-science-portfolio`
   - Description: "Data Science & AI Portfolio Website with CV Screening Demo"
   - Visibility: **Public** ✅
   - **Do NOT** initialize with README (unchecked)
   - **Do NOT** add .gitignore (unchecked)
   - **Do NOT** choose a license yet (unchecked)
4. **Click** "Create repository"
5. On the next page, **click** "uploading an existing file"
6. **Drag and drop** ALL files from `C:\Users\monay\Desktop\Portfolio` 
   - Make sure to include hidden files (`.gitignore`, `.env.example`)
   - To show hidden files in Windows Explorer: View → Show → Hidden items
7. **Commit message:** "Initial portfolio commit with projects and demos"
8. **Click** "Commit changes"

### 3. Verify Upload:

✅ Check that these files are present on GitHub:
- `README.md` (displays on homepage)
- `.gitignore` (protects sensitive files)
- `screenshots/` folder with all images
- `static/`, `templates/`, `Task3/` folders
- All `.py` files

✅ Check that these are NOT present:
- `.venv/` folder
- `.env` file (should never exist)
- `antigravity_portfolio_brief.*` files
- `Task1/`, `Task2/` folders

## 🌐 Next Steps (Deploy Live)

After uploading to GitHub, deploy to **Render.com**:

1. Create account at [render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name:** hamza-portfolio
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python portfolio_app.py`
   - **Environment Variables:**
     - `PORTFOLIO_DEMO_MODE` = `True`
5. Click "Create Web Service"
6. Wait for deployment (~5 minutes)
7. Visit your live URL! 🎉

## 📝 Notes

- **Demo Mode** is enabled by default - safe for public deployment
- **No API keys needed** - demo uses pre-computed sample data
- **Screenshots included** - showcasing both projects
- **Professional README** - provides clear documentation
- **Security maintained** - `.gitignore` protects secrets

---

**Ready to upload?** Follow the steps above! 🚀
