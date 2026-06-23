# Wikipedia RAG API

Ask any question, get a direct answer — powered by Wikipedia content and a Llama 3 LLM.

Reading through long Wikipedia articles just to find one answer is tedious. This API solves that — give it a topic and a question, and it fetches the relevant Wikipedia content, finds the most relevant chunks using FAISS vector search, and returns a direct answer via Groq's Llama 3. No scrolling, no skimming.

---

## Tech Stack

- **FastAPI** — web framework that serves the `/ask` endpoint
- **Wikipedia-API** — fetches Wikipedia article content by topic
- **LangChain** — text splitting and vector store integration
- **FAISS** — local vector database for similarity search
- **HuggingFace Embeddings** — converts text chunks into vectors (runs locally)
- **Groq (Llama 3)** — LLM that generates the final answer

---

## Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/arsh-bains/wiki-rag-api.git
   cd wiki-rag-api
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file in the root folder**
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Start the server**
   ```bash
   uvicorn main:app --reload
   ```

---

## Example

Send a POST request to `/ask` with a topic and question:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/ask" `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"question": "Who created Python?", "topic": "Python (programming language)"}'
```

**Response:**
```
answer
------
Guido van Rossum created Python. He began working on Python in the late 1980s
as a successor to the ABC programming language...
```

---

## What I Learned

Building this project taught me how a RAG pipeline works end to end — from fetching and chunking raw text, to converting it into vector embeddings, to retrieving the most relevant context and passing it to an LLM for a grounded answer. I also learned how to wire these components together cleanly using FastAPI.
