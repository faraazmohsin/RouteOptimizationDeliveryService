FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y sudo

COPY knn_model.pkl /app/knn_model.pkl
COPY . /app

ENV PORT=8080
ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

EXPOSE 8080

CMD streamlit run --server.port $PORT --server.enableCORS false --server.address 0.0.0.0 app.py