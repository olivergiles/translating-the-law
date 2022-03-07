FROM huggingface/transformers-pytorch-gpu:latest

COPY models /models
COPY requirements.txt /requirements.txt
COPY api /api

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn api.app:app --host 0.0.0.0 --port $PORT