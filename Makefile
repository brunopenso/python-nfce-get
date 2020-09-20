export PYTHONPATH=$(shell pwd)/src/
export PYTHONDONTWRITEBYTECODE=1

.PHONY=help

###
# Tests section
###
test: ## Run tests
	@pytest -x src/

test-coverage: ## Run tests with coverage output
	@pytest -x src/ --cov . --cov-report term-missing --cov-report xml
