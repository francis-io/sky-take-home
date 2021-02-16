FROM python:3.8.7-alpine

COPY *.py ./

ENTRYPOINT ["python", "main.py"]