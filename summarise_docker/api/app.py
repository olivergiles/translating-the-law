from fastapi import FastAPI
from transformers import pipeline
from api.get_from_bucket import open_from_bucket, cleaner

app = FastAPI()
data = open_from_bucket()

@app.get("/")
def index():
    return {'ok': True}

@app.get("/summary")
def summary(text):
    model = pipeline("summarization", model="/models/summarization-pretrained")
    text = text.replace("%", " ")
    TEXT = cleaner(text)
    return {"summary": model(TEXT, max_length=110, min_length=75, do_sample=True)}
