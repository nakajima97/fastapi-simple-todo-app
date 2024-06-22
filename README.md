# fatapi-template
# setup
`docker compose run --entrypoint "poetry install --no-root" api`

# Lint
`docker compose exec api poetry run ruff check`

# format
check  
`docker compose exec api poetry run ruff format --check`  
run  
`docker compose exec api poetry run ruff format`  