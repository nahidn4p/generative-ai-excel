# **Generative AI using FastAPI**

This is a simple FastAPI-based project for building a Document Question Answering (QA) system. 

**> For Better Result Use CURL or Postmen**

It allows users to:

	Upload documents

	Process and store their embeddings

	Query questions based on the uploaded content


**🚀 Features**
	Upload and process documents via /upload
	Ask natural language questions via /query
	Asynchronous handling for performance
	Modular components for document loading, embedding, and answering
	Dockerized for easy deployment

🛠️ Requirements
•	Python 3.8+
•	FastAPI
•	Uvicorn
•	Other dependencies like transformers, langchain, etc.



Install the required packages:
pip install -r requirements.txt


📦 Project Structure
├── main.py               # FastAPI application
├── document_loader.py   # Loads and chunks uploaded documents
├── embed_store.py       # Embeds and stores the document chunks
├── query_handler.py     # Handles question answering using context
├── requirements.txt
├── Dockerfile
└── README.md

📤 Endpoints
/upload (POST)
Upload a document to be processed and embedded.

Request
- Form Data: *file* (the document)

Response
```json

{
  "message": "File processed",
  "chunks_stored": 42
}

```
/query (POST)
Ask a question related to the uploaded document content.

Request
JSON Body:

```json
{
  "question": "What is the document about?"
}

```

Response

```json
{
  "answer": "The document discusses..."
}
```


▶️ Running Locally
Start the server using Uvicorn:

```python
uvicorn main:app --reload
```
Then open: http://localhost:8000/docs


🐳 Running with Docker (It will Take some time depending on Internet Speed to Build)
Step 1: Build the Docker image 

```console
docker build -t fastapi-doc-qa .
```

Step 2: Run the container

```console
docker run -d -p 8000:8000 --name doc-qa-api fastapi-doc-qa
```

Now the API will be available at: http://localhost:8000/docs


🐳 Running with Docker Compose

```console
docker compose up --build
```
Once built, open in browser:

```console
http://localhost:8000/docs
```
You can now:

- Upload a .pdf, .docx, .jpg, or .txt

- Ask a question

- Get answers from flan-t5-base





