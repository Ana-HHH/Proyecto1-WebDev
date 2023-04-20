FROM python:3.9-slim

WORKDIR /WebDevP1
COPY Logica ./Logica
COPY API_Rest ./API_Rest

RUN apt-get update
RUN apt-get install -y gcc
RUN apt-get install -y default-libmysqlclient-dev
RUN pip install --upgrade pip
RUN pip install -r ./API_Rest/requirements.txt
ENV PYTHONPATH="$PYTHONPATH:/"

EXPOSE 8000
CMD ["python", "./API_Rest/manage.py", "runserver", "0.0.0.0:8000"]
