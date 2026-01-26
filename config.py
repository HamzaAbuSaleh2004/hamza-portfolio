"""
Configuration module for Portfolio Application
Manages demo mode vs live mode settings
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Demo mode configuration
# When True: Uses pre-computed sample data, no API calls (safe for public deployment)
# When False: Uses real API with engines (requires API key)
DEMO_MODE = os.getenv('PORTFOLIO_DEMO_MODE', 'True').lower() in ('true', '1', 'yes')

# API Configuration (only needed for live mode)
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', '')

# Upload configuration
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload

# Application configuration
SECRET_KEY = os.getenv('SECRET_KEY', 'hamza-portfolio-secret-key-2026')
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 'yes')

# Print configuration on startup
def print_config():
    """Print configuration settings on startup"""
    print("\n" + "="*70)
    print("PORTFOLIO CONFIGURATION")
    print("="*70)
    print(f"Mode: {'DEMO MODE (using sample data)' if DEMO_MODE else 'LIVE MODE (using real API)'}")
    print(f"CV Screening: {'Available (demo)' if DEMO_MODE else ('Available (live)' if GOOGLE_API_KEY else 'Unavailable (no API key)')}")
    print(f"Debug: {DEBUG}")
    print("="*70 + "\n")
