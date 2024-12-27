#!/usr/bin/env just --justfile

# Show this help
list:
    just --list


# Run the development server
dev:
    @uv run src/manage.py runserver


# Check formatting and syntax
check:
    @uv run pre-commit run --all-files


# Format code with Ruff
format:
    @ruff check --fix
    @ruff format


# Run mypy
mypy:
    @uv run mypy .


# Push to remote
push:
    @git push --set-upstream origin `git rev-parse --abbrev-ref HEAD`