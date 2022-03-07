FROM huggingface/transformers-pytorch-gpu:latest

COPY models /models
COPY data /data
COPY requirements.txt /requirements.txt
COPY api /api

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT