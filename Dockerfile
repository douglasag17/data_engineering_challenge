FROM python:latest

RUN mkdir /code

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /code/etl/ .

RUN mkdir /data/

COPY /code/etl/data/data.json /data/data.json

CMD ["python", "code/etl/main.py"]
