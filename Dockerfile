FROM python:3.7
RUN apt-get update
ENV PYTHONUNBUFFERED 1
RUN mkdir /opt/app
WORKDIR /opt/app
COPY requirments.txt /opt/app/
RUN pip install -r requirments.txt
COPY . /opt/app/