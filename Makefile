lint:
	@ruff check --select I --fix
	@ruff format
	@ruff check
	@mypy .
	@echo "ALL PASS"

streamlit:
	@streamlit run _home.py
