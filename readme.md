# Advanced Python Programming
by Quan Nguyen via PacktPublishing

This repo holds my code experience along reading this book.

## Setup

I am using:

- `Python 3.11`;
- `uv` for packages installer and resolver;
- `mypy` for static type checking;
- `ruff` for linter.

`uv` can be installed with `pip` or `pipx` (or even with a standalone installer, [readmore](https://docs.astral.sh/uv/getting-started/installation/)). After installed `uv`, create `.venv` virtual environment and active it (Window) with:

```bash
uv venv
.venv/Scripts/activate
```

and install depenencies for this book with:

```bash
uv pip install -r .\requirements.txt
```
