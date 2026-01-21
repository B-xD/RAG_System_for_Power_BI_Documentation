# config.py

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# ========= OpenAI =========
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("base_url")

EMBEDDING_MODEL = "text-embedding-3-small"
CHAT_MODEL = "gpt-4o-mini"

ENCODING_NAME = "cl100k_base"
# ========= Paths =========
PDF_PATH = "data/"
VECTOR_DB_DIR = "vector_db/powerBI_db"

# ========= Chunking =========
CHUNK_SIZE = 512 
CHUNK_OVERLAP = 16

# ========= Retrieval =========
TOP_K = 5