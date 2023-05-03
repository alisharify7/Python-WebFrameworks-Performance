FROM python:alpine


RUN mkdir /app
ADD . /app
WORKDIR /app
# RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]