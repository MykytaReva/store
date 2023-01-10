SHELL := /bin/bash

run:
	python app/manage.py runserver

shell_plus:
	python app/manage.py shell_plus --print-sql

show_urls:
	python app/manage.py show_urls

makemigrations:
	python app/manage.py makemigrations

migrate1:
	python app/manage.py migrate
migrate: makemigrations \
	migrate1

coverage:
	cd app && coverage run manage.py test

html:
	cd app && coverage html

show-report:  ## open coverage HTML report in default browser
	cd app && python3 -c "import webbrowser; webbrowser.open('htmlcov/index.html')"

report:
	cd app &&coverage report

show: coverage \
	html \
	show-report

kill:
	lsof -t -i tcp:8000 | xargs kill -9