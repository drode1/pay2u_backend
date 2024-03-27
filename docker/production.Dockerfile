FROM python:3.12.2-slim

ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.8.2 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' \
    PATH="/root/.local/bin:$PATH"

RUN apt-get update && \
    apt-get install -y curl make --no-install-recommends && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false && \
    apt-get clean -y && rm -rf /var/lib/apt/lists/*

WORKDIR /var/www/html

COPY ../poetry.lock ../pyproject.toml ./

RUN $POETRY_HOME/bin/poetry install --no-interaction --no-ansi --no-root

COPY . .

RUN chmod a+x ./docker/web_entrypoint.sh &&  \
    sed -i 's/\r$//g' './docker/web_entrypoint.sh'

ENTRYPOINT ["./docker/web_entrypoint.sh"]