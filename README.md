# pay2u_backend

## For local development

1. cp `.env.example` -> `.env`
2. Install all scripts via `poetry install`
3. Then run `pre-commit install` to use pre-commit hook automatically
4. Run `make migrate` to update DB schema
5. Run `make seed` if you need fake data

## For trough docker

1. cp `.env.example` -> `.env`
2. Then run `pre-commit install` to use pre-commit hook automatically
3. Run `docker compose up -d`
4. Open your docker Django container and run:
    - Run `make migrate` to update DB schema
    - Run `make seed` if you need fake data
