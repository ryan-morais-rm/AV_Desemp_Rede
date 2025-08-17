FROM python:3.12.3-slim

WORKDIR /Semaforo

COPY Semaforo.py /Semaforo/ 

RUN pip install --no-cache-dir pytz && \
    mkdir -p /semaforodados 

VOLUME /semaforodados

CMD ["python3", "Semaforo.py"] 