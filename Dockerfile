FROM python:latest

WORKDIR /code
RUN pip install python-dotenv
RUN pip install mysqlclient
RUN pip install selenium