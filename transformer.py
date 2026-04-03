import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

with open("data/faqs.json", "r") as f:
    data = json.load(f)

questions = [item["question"] for item in data]

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(questions)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

faiss.write_index(index, "vector.index")

with open("questions.json", "w") as f:
    json.dump(data, f)