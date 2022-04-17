FROM python:3.10-slim

WORKDIR /app

RUN pip install "poetry==1.1.3"

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

COPY . .

CMD gunicorn django_Liis.wsgi:application --bind 0.0.0.0:8000