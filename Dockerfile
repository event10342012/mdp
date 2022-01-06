FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./mdp /app
COPY requirements.txt /app

RUN pip install /app/requirements.txt
