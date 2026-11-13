import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

EMBEDDING_MODEL = "text-embedding-3-small"
LLM_MODEL = "gpt-4.1-mini"

COLLECTION_NAME = "my_documents"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

TOP_K = 3

UPLOAD_DIR = "data/uploads"
CHROMA_DB_DIR = "data/chroma_db"