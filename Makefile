SHELL := /bin/bash

# Determine the OS and set the activation command accordingly
ifeq ($(OS),Windows_NT)
    ACTIVATE = .venv\Scripts\activate
else
    ACTIVATE = source .venv/bin/activate
endif

.PHONY: activate install lint

activate: ## Activate the virtual environment
	$(ACTIVATE)

install: activate ## Install the dependencies
	uv pip install -r requirements.txt

lint: activate ## Run Ruff to lint the code
	ruff .

docs: activate
	mkdocs serve

generate-docs: activate
	python scripts/generate_docs.py
