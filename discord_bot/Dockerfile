FROM python:3

WORKDIR /app

COPY discord-requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY *.py ./
COPY .env .env

CMD [ "python", "./main.py" ]