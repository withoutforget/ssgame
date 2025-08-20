@run: 
    uv run python -m src.ssgame.main
@lint:
    uv run ruff check --fix
    uv run ruff format