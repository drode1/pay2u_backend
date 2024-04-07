# Pay2u API

[![Release to production](https://github.com/drode1/pay2u_backend/actions/workflows/release-production.yml/badge.svg?branch=main)](https://github.com/drode1/pay2u_backend/actions/workflows/release-production.yml)

This is the API of the application for the bank. Through this API, the user will be able to subscribe to various
services (Spotify, OKKO, etc.), receive cashback when paying for these services, etc.

You can view the current backend at the link - [pay2u.eremezov.com](https://pay2u.eremezov.com)

Credential for admin panel:

- Login `admin@test.ru`
- Password `admin`

API Schema - [Swagger](https://pay2u.eremezov.com/api/v1/docs/swagger/)

## Stack

![python version](https://img.shields.io/badge/Python-3.11+-blue)
![django version](https://img.shields.io/badge/Django-4.2-51a77a)
![djangorestframework version](https://img.shields.io/badge/DRF-3.14-951d12)
![poetry](https://img.shields.io/pypi/v/poetry?label=Poetry)

### Other dependencies

The other dependencies are specified in the file `pyproject.toml` and the list of them under this text

- `python-dotenv` - for env variables
- `psycopg2-binary` - to connect django with postgres
- `django-cors-headers` - for cors settings
- `gunicorn` - as a python webserver
- `djangorestframework-simplejwt` - to obtain JWT user token
- `django-phonenumber-field` & `babel` - to provide phone validation in user
- `pillow` - for managing images
- `django-filter` - to filter entities
- `drf-spectacular` - for swagger & OpenAPI documentation
- `pre-commit` & `ruff` - to maintain clean code
- `factory-boy` - to generate fake data

## Development

There are two ways of local development

- Native
- Docker

### Native

1. cp `.env.example` -> `.env`
2. Install all scripts via `poetry install`
3. Then run `pre-commit install` to use pre-commit hook automatically (if needed)
4. Run `make migrate` to update DB schema
5. Run `make seed` if you need fake data
6. Run `make collectstatic` to collect static files

### Docker

1. cp `.env.example` -> `.env`
2. Then run `pre-commit install` to use pre-commit hook automatically (if needed)
3. Run `docker compose up -d`
4. Open your docker Django container and run:
    - Run `make migrate` to update DB schema
    - Run `make seed` if you need fake data
5. Run `make collectstatic` to collect static files

## Authors

- Egor Remezov
    - [mr.drodel@gmail.com](mailto:info@eremezov.com)
    - [@e_remezov](https://t.me/e_remezov)
- Ivan Barchuninov
    - [bikovshanin@yandex.ru](mailto:bikovshanin@yandex.ru)
    - [@bikovshanin](https://t.me/bikovshanin)
