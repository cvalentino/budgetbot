FROM python:3

WORKDIR /app

COPY . .

RUN apt-get update \
    && apt-get install -y logrotate \
    && pip install --no-cache-dir -r requirements.txt \
    && mkdir /app/logs/ \
    && mv /app/logrotate.conf /etc/logrotate.d/app

ENV FLASK_APP=app.py PYTHONPATH="${PYTHONPATH}:/app"

EXPOSE 8080

CMD ["bash", "start_budget_bot_api.sh"]