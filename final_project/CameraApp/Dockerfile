FROM python:3.12.3-slim 

WORKDIR /Camera

COPY CameraApp.py /Camera/

RUN pip install --no-cache-dir pytz && \
    mkdir -p /cameradados 

VOLUME [ "cameradados" ] 

CMD [ "python3", "CameraApp.py" ]