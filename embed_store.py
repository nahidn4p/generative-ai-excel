from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.IndexFlatL2(384)
texts = []

def embed_and_store(chunks):
    global texts
    embeddings = model.encode(chunks)
    index.add(np.array(embeddings).astype("float32"))
    texts.extend(chunks)

def search_similar(question, top_k=3):
    embedding = model.encode([question])
    D, I = index.search(np.array(embedding).astype("float32"), top_k)
    return [texts[i] for i in I[0]]
