FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./mdp /app
COPY requirements.txt /app

RUN pip install /app/requirements.txt -i http://172.20.189.30:8081/repository/pypi-esec-grp-prod/simple --trusted-host 172.20.189.30
