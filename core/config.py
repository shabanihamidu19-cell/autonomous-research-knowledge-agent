import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

# Model Configuration
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.3"))

# Agent Settings
MAX_ITERATIONS = 8
MAX_RPM = 20  # Requests per minute limit

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
KNOWLEDGE_DIR = os.path.join(DATA_DIR, "knowledge")
LOGS_DIR = os.path.join(DATA_DIR, "logs")
MEMORY_DIR = os.path.join(BASE_DIR, "memory", "chroma_db")

# Ensure directories exist
os.makedirs(KNOWLEDGE_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(MEMORY_DIR, exist_ok=True)
