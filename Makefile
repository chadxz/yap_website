all: dev
.PHONY: all

dev: deps
	pipenv run python manage.py runserver
.PHONY: dev

test: deps
	pipenv run pytest
.PHONY: test

watchtest: deps
	pipenv run pytest-watch
.PHONY: watchtest

deps: venv node_modules css
.PHONY: deps

venv: venv/bin/activate
.PHONY: venv

css: static/main.min.css
.PHONY: css

node_modules:
	npm install

static/main.min.css:
	npm run build

venv/bin/activate:
	pip3 install pipenv
	pipenv install

clean:
	rm -rf node_modules
	rm -rf static/main.min.css
	rm -rf db.sqlite3
	rm -rf .pytest_cache
	rm -rf .coverage
	pipenv --rm
.PHONY: clean
