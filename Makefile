export PYTHONPATH=$(shell pwd)/src/
export PYTHONDONTWRITEBYTECODE=1

.PHONY=help

help:  ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

clean: ## Remove cache files
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

###
# Tests section
###
test: clean## Run tests
	@pytest -x tests/

test-coverage: clean ## Run tests with coverage output
	@pytest -x tests/ --cov . --cov-report term-missing --cov-report xml

test-matching: clean ## Run tests by match ex: make test-matching k=name_of_test
	@pytest -k $(k) tests/