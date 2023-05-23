FROM python

RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "-b", "127.0.0.1:8000"]
