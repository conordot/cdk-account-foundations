.PHONY: lint
lint:
	pylint *.py **/**.py

.PHONY: test
test:
	pytest -s -v