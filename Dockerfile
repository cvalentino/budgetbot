FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ADD python-files.tar.gz .
COPY .env .env

CMD [ "python", "./main.py" ]