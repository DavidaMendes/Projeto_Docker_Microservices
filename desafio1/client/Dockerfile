FROM python:3.11-slim

WORKDIR /client

RUN pip install requests

COPY client.py .

CMD ["python", "client.py"]
