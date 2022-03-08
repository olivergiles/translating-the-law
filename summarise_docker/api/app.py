from fastapi import FastAPI
from transformers import pipeline
from api.get_from_bucket import open_from_bucket, cleaner

app = FastAPI()
data = open_from_bucket()

@app.get("/")
def index():
    return {'ok': True}

@app.get("/summary")
def summary(key):
    model = pipeline('summarizer', model='/models/summarization-pretrained')
    TEXT = cleaner(data[int(key)]['press summary']['Background to the appeal'])+cleaner(data[int(key)]['press summary']['Reasons for the judgment'])
    input = {
        "text":TEXT
    }
    return {"summary": model(text, max_length=300, min_length=60, do_sample=True)}
