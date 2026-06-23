from fastapi import FastAPI
from fetcher import fetch_wikipedia_content
from indexer import build_index
from answerer import answer_question
from pydantic import BaseModel


app = FastAPI()
class AskRequest(BaseModel):
    question : str
    topic : str

@app.post("/ask")
def ask(request: AskRequest):
    content = fetch_wikipedia_content(request.topic)
    index = build_index(content)
    answer = answer_question(request.question, index)

    return {"answer": answer}


