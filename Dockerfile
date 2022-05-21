FROM python:latest

MAINTAINER aneudy.motacatalino@gmail.com

RUN mkdir -p /var/cas-automation

COPY ./ /var/cas-automation

RUN pip install -r /var/cas-automation/requirements.txt

WORKDIR /var/cas-automation

ENTRYPOINT pytest /var/cas-automation