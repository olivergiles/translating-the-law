from fastapi import FastAPI
from transformers import pipeline
from api.get_from_bucket import open_from_bucket, cleaner

app = FastAPI()
data = open_from_bucket()

@app.get("/")
def index():
    return {"ok":True}

@app.get("/question")
def question(type, key, question):
    model = pipeline("question-answering", model="/models/questions-pretrained")
    if type == "full":
        ARTICLE = cleaner(data[int(key)]["judgement"]["body"])
    else:
        ARTICLE = cleaner(data[int(key)]["press summary"]["Reasons for the judgment"])
    QUESTION = question
    input = {
        "question": QUESTION,
        "context": ARTICLE
    }
    return {"answer": model(input)}