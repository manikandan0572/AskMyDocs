import os

# Elasticsearch
ELASTIC_URL = os.getenv("ELASTIC_URL")
ELASTIC_API_KEY = os.getenv("ELASTIC_API_KEY")

# Pinecone
PINCONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINCONE_INDEX = os.getenv("PINECONE_INDEX")

# Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")