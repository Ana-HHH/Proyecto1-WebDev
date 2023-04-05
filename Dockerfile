FROM python:3.9-alpine

WORKDIR /WEBDEV1
COPY Logica .
COPY API_Rest .

RUN apt-get update
RUN apt-get install -y gcc
RUN apt-get install -y default-libmysqlclient-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV PYTHONPATH = "$PYTHONPATH:/"


EXPOSE 8000
CMD ["PYTHON", 'MANAGE.PY', "RUNSERVER", '0.0.0.0:8000']