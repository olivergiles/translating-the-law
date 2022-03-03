FROM huggingface/transformers-pytorch-gpu:latest

COPY models /models
COPY data /data
COPY requirements.txt /requirements.txt
COPY functions /functions

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["tree"]