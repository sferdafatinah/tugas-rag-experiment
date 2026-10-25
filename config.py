
import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")
 
UPLOAD_DIR = BASE_DIR / "data" / "uploads" 
UPLOAD_DIR.mkdir(parents=True, exist_ok=True) 
 
QDRANT_PATH = BASE_DIR / "qdrant_data" 
 
COLLECTION_NAME = "rag_documents" 
 
EMBEDDING_MODEL = ( 
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2" 
) 
 
TOP_K = 4
BRIEF_TOP_K = 1
 
# Token-aware chunking. 
# The embedding model has a max sequence length of 128 tokens. 
CHUNK_SIZE = 100
CHUNK_OVERLAP = 20