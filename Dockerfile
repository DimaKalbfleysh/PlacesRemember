FROM python:3.7
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin
ENV PYTHONUNBUFFERED 1
RUN mkdir /opt/app
WORKDIR /opt/app
COPY requirements.txt /opt/app/
RUN pip install -r requirements.txt
COPY . /opt/app/