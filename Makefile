run: ## Run the server
	uvicorn app.main:app

run-with-reload: ## Run the server with hot reload options - it reacts on code changes
	uvicorn app.main:app --reload

db-run: ## Run the docker image with Postgres
	docker run --name map-db -p 5430:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=map-app-db -d postgres
