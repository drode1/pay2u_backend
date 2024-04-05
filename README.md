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

The other dependencies are specified in the file pyproject.toml

## Development

There are two ways of local development

- Native
- Docker

### Native

1. cp `.env.example` -> `.env`
2. Install all scripts via `poetry install`
3. Then run `pre-commit install` to use pre-commit hook automatically
4. Run `make migrate` to update DB schema
5. Run `make seed` if you need fake data

### Docker

1. cp `.env.example` -> `.env`
2. Then run `pre-commit install` to use pre-commit hook automatically
3. Run `docker compose up -d`
4. Open your docker Django container and run:
    - Run `make migrate` to update DB schema
    - Run `make seed` if you need fake data

## Authors

- Egor Remezov
    - [mr.drodel@gmail.com](mailto:info@eremezov.com)
    - [@e_remezov](https://t.me/e_remezov)
- Ivan Barchuninov
    - [bikovshanin@yandex.ru](mailto:bikovshanin@yandex.ru)
    - [@bikovshanin](https://t.me/bikovshanin)