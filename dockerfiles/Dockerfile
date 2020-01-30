FROM python:3.7-slim

COPY . /opt/app
WORKDIR /opt/app

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["python3", "server.py"]