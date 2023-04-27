FROM python:alpine

RUN mkdir /app
ADD . /app

WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD gunicorn -b 0.0.0.0:5000 app:app 