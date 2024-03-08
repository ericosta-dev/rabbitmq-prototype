FROM python:3.9-slim

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-ansi

CMD ["bash", "-c", "while true; do sleep 3600; done"]