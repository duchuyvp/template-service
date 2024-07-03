FROM python:3.12

EXPOSE 8000

# # ARG GITHUB_TOKEN
# # RUN git config --global url."https://${GITHUB_TOKEN}@github.com".insteadOf "https://github.com"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN chmod 600 /root/.ssh/id_rsa

WORKDIR /template-service
COPY pyproject.toml .
RUN python -m pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi --no-root

COPY . /template-service

CMD ["uvicorn", "template_service.entrypoints.rest.app:app", "--host", "0.0.0.0", "--port", "8000"]
