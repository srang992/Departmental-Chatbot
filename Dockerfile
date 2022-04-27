FROM python:3.7.12-slim-bullseye

WORKDIR /WhatsAppBot

RUN apt-get update && apt-get -y install gcc

COPY requirements.txt .

RUN pip install -r requirements.txt && python -m spacy link en_core_web_sm en

COPY . .

CMD python main.py $PORT