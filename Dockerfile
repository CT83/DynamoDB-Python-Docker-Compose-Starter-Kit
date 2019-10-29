FROM python:3-buster

ADD requirements.txt /tmp/requirements.txt 
RUN pip install -r /tmp/requirements.txt 

COPY . /app
WORKDIR /app

ENTRYPOINT ["python","./app.py"]