import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("ELASTIC_URL")
elastic_key = os.getenv("ELASTIC_API_KEY")
pinecone_key = os.getenv("PINECONE_API_KEY")
gemini_key = os.getenv("GEMINI_API_KEY")

print("Elastic URL loaded:", bool(url))
print("Elastic API key loaded:", bool(elastic_key))
print("Pinecone API key loaded:", bool(pinecone_key))
print("Gemini API key loaded:", bool(gemini_key))
print("Elastic URL:", url)