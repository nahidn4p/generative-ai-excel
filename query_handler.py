from transformers.pipelines import pipeline
from embed_store import search_similar

qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")  # Small and fast

async def generate_answer(question):
    context = "\n".join(search_similar(question))
    prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
    result = qa_pipeline(prompt, max_length=200, do_sample=False)
    return {
        "answer": result[0]['generated_text']
    }
