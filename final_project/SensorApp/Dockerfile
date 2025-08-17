FROM python:3.12.3-slim 

WORKDIR /SensorApp

COPY sensor_ar.py . 

RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir pytz && \ 
    mkdir -p /sensordados 

VOLUME /sensordados

CMD ["python3", "sensor_ar.py"]