import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("vector.index")

with open("questions.json", "r") as f:
    data = json.load(f)

def get_answer(query):
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), k=1)
    return data[I[0][0]]["answer"]