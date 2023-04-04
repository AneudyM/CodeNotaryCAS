FROM golang:1.18
MAINTAINER aneudy.motacatalino@gmail.com

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub >> google.pub
RUN apt-key add google.pub
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt update -y
RUN apt install -y google-chrome-stable
RUN apt-get install -y python3 python3-pip

RUN mkdir -p /var/cas-automation

COPY ./ /var/cas-automation

RUN pip install --upgrade pip
RUN pip install -r /var/cas-automation/requirements.txt

WORKDIR /var/cas-automation

CMD ["python3", "./run.py"]