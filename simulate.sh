#!/bin/bash
set -e

echo "running mypy..."
poetry run mypy omnitost

echo "running pyright..."
poetry run pyright

echo "running..."
poetry run python3 omnitost
