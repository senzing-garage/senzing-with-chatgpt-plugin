lint:
	ruff check .
lint-fix:
	ruff check --fix .
lint-watch:
	ruff check --watch .

run:
	uvicorn server.main:app --port=8080 --reload

test:
	pytest --cov server --cov-report term-missing -v -s tests
test-watch:
	ptw -- --testmon

openapi-schema:
	python server/openapi_schema.py

