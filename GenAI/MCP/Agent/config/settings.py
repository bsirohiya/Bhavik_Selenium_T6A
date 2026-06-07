# config/settings.py

# python-dotenv is a library that reads .env files
from dotenv import load_dotenv
import os

# load_dotenv() reads your .env file and loads
# its contents into environment variables
load_dotenv()

# os.getenv() reads a variable from the environment
# If GEMINI_API_KEY doesn't exist, returns None
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Safety check — if key is missing, give a clear error
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Please check your .env file.")