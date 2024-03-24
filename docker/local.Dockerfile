FROM python:3.12.2-slim

ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.8.2 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local'

RUN apt-get update && \
    apt-get install -y vim curl make --no-install-recommends && \
    curl -sSL https://install.python-poetry.org | python - && \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false && \
    apt-get clean -y && rm -rf /var/lib/apt/lists/*

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app
COPY ../poetry.lock ../pyproject.toml /app/

RUN --mount=type=cache,target="$POETRY_CACHE_DIR" \
    /usr/local/bin/poetry install --no-interaction --no-ansi --no-root

COPY . /app/
