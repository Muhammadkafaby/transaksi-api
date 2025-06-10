import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app as vercel_app

# Vercel will use 'vercel_app' as the entry point for the serverless function
