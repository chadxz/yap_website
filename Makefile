BIN=venv/bin

all: dev
.PHONY: all

dev: venv node_modules css
	$(BIN)/python manage.py runserver
.PHONY: dev

venv: venv/bin/activate
.PHONY: venv

css: static/main.min.css
.PHONY: css

node_modules:
	npm install

static/main.min.css:
	npm run build

venv/bin/activate:
	python3 -m venv venv; \
		venv/bin/pip install -r requirements.txt

clean:
	rm -rf node_modules
	rm -rf static/main.min.css
	rm -rf db.sqlite3
	rm -rf .pytest_cache
	rm -rf venv
.PHONY: clean
