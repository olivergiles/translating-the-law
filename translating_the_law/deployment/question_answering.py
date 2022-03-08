
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def index():
    return {'ok':True}

@app.get("/answer")
def answer():
    return

# url = 'http://localhost:8000/predict'
# params = {
#     'question': 0, # 0 for Sunday, 1 for Monday, ...
#     'context': '14:00'
# }
# response = requests.get(url, params=params)
# response.json()
