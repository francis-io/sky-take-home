help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

# Supress printing of the make command
.SILENT:

lint:
	for file in "$(shell find . -name '*.py')"; do \
		docker run -ti --rm -v $(shell pwd):/apps alpine/flake8:3.8.4 $$file; \
	done

.PHONY: lint-dockerfile
lint-dockerfile: ## Use hadolint to warn on dockerfile best practices
	for file in "$(shell find . -name 'Dockerfile')"; do \
		docker run --rm -i hadolint/hadolint < $$file; \
	done

build:
	docker build -t lotto-results .

install-test-reqs:
	pip3 install -r test-requirements.txt

test:
	nosetests test test.py

