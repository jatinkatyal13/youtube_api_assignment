FROM python:3.9-slim

RUN pip install poetry gunicorn

WORKDIR /app

RUN poetry config virtualenvs.create false
ADD pyproject.toml poetry.lock /app/
RUN poetry install --no-root --no-interaction --no-ansi

ADD . /app

CMD ["gunicorn", "youtube_api.wsgi", "-b", "0.0.0.0:8000"]
