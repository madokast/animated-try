# AGENTS.md

## Environment
- Python 3.12+, managed via `.python-version`
- Package manager: **uv** (not pip/poetry), invoked via `python -m uv`
- Virtual env: `.venv/` (run `python -m uv sync` to install)
- Dependencies declared in `pyproject.toml`, locked in `uv.lock`

## Commands
- Install deps: `python -m uv sync`
- Add a package: `python -m uv add <pkg>`
- Run a script: `python -m uv run python <file>.py`

## Project intent
AI automation exploration for personal use. Early stage / blank slate — no established package structure yet.

## OpenCode provider
Local DeepSeek-compatible endpoint at `http://192.168.45.32:3000/v1`. If that host is unreachable, OpenCode sessions will fail.
