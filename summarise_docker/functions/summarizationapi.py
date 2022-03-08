from fastapi import FastAPI
app = FastAPI()

from models.summarization-pretrained import 
@app.get("/")
def index():
    return {'ok':True}
@app.get("/summarize")
def summary():
    model = pipeline('summarizer', model=summarization_pretrained, tokenizer=tokenizer.json)
