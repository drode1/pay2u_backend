PYTHON = poetry run python
ROOT = .

all:
	@echo "make migrations		- Create migrations of changed models"
	@echo "make migrate			- Migrate changes to db of changed models"
	@echo "make seed			- Seed database with fake data"
	@echo "make collectstatic	- Collect static files"
	@echo "make run				- Start localserver"
	@exit 0

migrations:
	$(PYTHON) ${ROOT}/manage.py makemigrations

migrate:
	$(PYTHON) ${ROOT}/manage.py migrate

seed:
	$(PYTHON) ${ROOT}/manage.py seed

collectstatic:
	$(PYTHON) ${ROOT}/manage.py collectstatic --no-input

run:
	$(PYTHON) ${ROOT}/manage.py runserver