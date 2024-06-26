from fastapi import FastAPI, Request
import uvicorn
from text_summarizer import TextSummarizer

app = FastAPI()

summarizer = TextSummarizer()  

@app.post("/summarize")
async def summarize(request: Request):
    """
    Summarize the provided text.

    Args:
        request (Request): The incoming request containing JSON data with a 'text' field.

    Returns:
        dict: A dictionary with the summarized text.
    """
    data = await request.json()
    text = data.get("text", "")
    summary = summarizer.summarize(text)  
    return {"summary": summary}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
