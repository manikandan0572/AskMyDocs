from dotenv import load_dotenv
import os
from elasticsearch import Elasticsearch

load_dotenv()

url = os.getenv("ELASTIC_URL")
key = os.getenv("ELASTIC_API_KEY")

es = Elasticsearch(
    hosts=[url],
    api_key=key
)

try:
    print(es.info())
    print("Elasticsearch connected successfully!")
except Exception as e:
    print("Elasticsearch connection failed:", e)