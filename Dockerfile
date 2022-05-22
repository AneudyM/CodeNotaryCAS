FROM python:latest

MAINTAINER aneudy.motacatalino@gmail.com

RUN mkdir -p /var/cmd-automation

COPY ./ /var/cas-automation

RUN pip install -r /var/cmd-automation/requirements.txt

WORKDIR /var/cas-automation

ENTRYPOINT pytest /var/cas-automation