.ONESHELL:
lint:
	flake8 .

check-fmt:
	black . --check

fmt:
	black .

api:
	docker-compose up --build -d redis 
	python manage.py runserver