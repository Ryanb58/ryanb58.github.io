.PHONY: help
help: ## Display callable targets.
	@echo "Reference card for usual actions."
	@echo "Here are available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


.PHONY: sortimports
sortimports: ## Sort imports
	pip install isort
	isort -rc .


.PHONY: format
format: ## Sort imports
	pip install black
	black .


.PHONY: clean
clean: ## Cleanup python cache files.
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete


.PHONY: build
build: ## Build the website
	venv/bin/python build.py


.PHONY: run
run: ## Run an HTTP server
	python -m http.server --directory docs

