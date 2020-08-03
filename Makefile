run: ## Run the server
	uvicorn app.main:app

run-with-reload: ## Run the server with hot reload options - it reacts on code changes
	uvicorn app.main:app --reload

db-create-tables: ## Create tables in database
	python ./app/utils/create_tables.py
