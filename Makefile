.ONESHELL:
lint:
	flake8 .

check-fmt:
	black . --check

fmt:
	black .

api:
	python manage.py runserver