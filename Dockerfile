FROM python:3-slim-buster

ADD requirements.txt /tmp/requirements.txt 
RUN pip install -r /tmp/requirements.txt 
COPY . /app
WORKDIR /app

RUN chmod +X wait-for-it.sh

ENTRYPOINT ["./wait-for-it.sh", "database:8000", "--", "python", "app.py"]