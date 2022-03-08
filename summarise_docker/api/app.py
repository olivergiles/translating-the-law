from fastapi import FastAPI
from transformers import pipeline
from api.get_from_bucket import open_from_bucket, cleaner

app = FastAPI()
data = open_from_bucket()

@app.get("/")
def index():
    return {'ok': True}

#cleaner(data[int(key)]['press summary']['Background to the appeal'])+cleaner(data[int(key)]['press summary']['Reasons for the judgment'])

@app.get("/summary")
def summary(text):
    model = pipeline("summarization", model="/models/summarization-pretrained")
    TEXT = cleaner(text)
    return {"summary": model(TEXT, max_length=110, min_length=30, do_sample=True)}
