import wikipediaapi

def fetch_wikipedia_content(topic: str) -> str:
    wiki_wiki = wikipediaapi.Wikipedia(user_agent='wiki-rag-api', language='en')

    page_py = wiki_wiki.page(topic)
    
    if page_py.exists():
        return(page_py.summary)
    
    else :
        return ""
    



       


