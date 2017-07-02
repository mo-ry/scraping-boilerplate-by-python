FROM python:3.6

WORKDIR /code
RUN pip install python-dotenv
RUN pip install mysqlclient
RUN pip install selenium