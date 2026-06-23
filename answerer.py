from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def answer_question(question: str, index ) -> str:
    docs = index.similarity_search(question, k=3)
    context = "\n".join([doc.page_content for doc in docs])
    prompt = f"""Answer the question based on the context below.
                Context:
                {context}

                Question:
                {question}"""
    response = client.chat.completions.create(
       model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
        
    )
    return response.choices[0].message.content



