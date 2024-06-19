FROM python:3.12

EXPOSE 8000

ARG GITHUB_TOKEN
RUN git config --global url."https://${GITHUB_TOKEN}@github.com".insteadOf "https://github.com"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /user-service
COPY pyproject.toml .
RUN python -m pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi --no-root

COPY . /user-service

CMD ["uvicorn", "src.entrypoints.app:app", "--host", "0.0.0.0", "--port", "8000"]
