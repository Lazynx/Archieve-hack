FROM python:3.12.0-slim

RUN apt-get update && apt-get install -y \
    texlive-latex-base \
    texlive-lang-cyrillic \
    --no-install-recommends

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn main:app --workers 8 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
