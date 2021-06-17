FROM python:3.9-slim

RUN pip install poetry gunicorn
RUN apt-get update
RUN apt-get install -y cron

WORKDIR /app

RUN poetry config virtualenvs.create false
ADD pyproject.toml poetry.lock /app/
RUN poetry install --no-root --no-interaction --no-ansi

COPY start.sh /bin/start.sh

COPY cron.cfg /etc/cron.d/cron.cfg

RUN crontab /etc/cron.d/cron.cfg

COPY . /app

CMD ["/bin/start.sh"]
