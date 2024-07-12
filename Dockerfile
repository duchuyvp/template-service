FROM python:3.12

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /template-service
COPY pyproject.toml .
RUN python -m pip install poetry
RUN poetry config virtualenvs.create false

RUN --mount=type=ssh mkdir -p ~/.ssh
RUN --mount=type=ssh ssh-keyscan github.com > ~/.ssh/known_hosts
RUN --mount=type=ssh poetry install --no-dev --no-interaction --no-ansi --no-root

COPY . /template-service

CMD ["uvicorn", "template_service.entrypoints.rest.app:app", "--host", "0.0.0.0", "--port", "8000"]
