from transformers import pipeline
from api.get_from_bucket import open_from_bucket, cleaner
from fastapi import FastAPI

data = open_from_bucket()
app = FastAPI()

@app.get("/")
def index():
    return {'result':True}

@app.get("/summary")
def generate_summary():
    model = pipeline('summarization', model='/models/summarization-pretrained')
    for x in range(1):
        text1 = cleaner(data[x]['press summary']['Background to the appeal'])
        text2 = cleaner(data[x]['press summary']['Reasons for the judgment'])[:5000]
        background_summary = model(text1, max_length = 300, min_length = 30, do_sample=True)
        judgment_summary = model(text2, max_length = 300, min_length = 30, do_sample=True)
        data[x]['background summary'] = background_summary[0]['summary_text']
        data[x]['judgment summary'] = judgment_summary[0]['summary_text']
    return data

if __name__ == "__main__":
    print(data()[0].keys())
