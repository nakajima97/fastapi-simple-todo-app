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

# migration
create migration file  
`docker compose exec api poetry run alembic revision --autogenerate -m "title"`  
  
execute migration  
`docker compose exec api poetry run alembic upgrade head`  

# test
`docker compose exec api poetry run pytest`