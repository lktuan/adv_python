# Advanced Python Programming
by Quan Nguyen via PacktPublishing

This repo holds my code/note experience along reading this book. The book comprises 4 parts:

1. Python Native & Specialized Optimization (c1 - c6);
2. Concurrency & Parallelism (c7 - c15);
3. Design Patterns in Python (c16 - c26).

## Setup

I am using a very modern Python toolkit, listed below:

- `Python 3.11`;
- `uv` for packages installer and resolver;
- `mypy` for static type checking;
- `ruff` for linter.

`uv` can be installed with `pip` or `pipx` (or even with a standalone installer, [read more](https://docs.astral.sh/uv/getting-started/installation/)). After installed `uv`, create `.venv` virtual environment and active it (Window) with:

```bash
uv venv
.venv/Scripts/activate
```

and install depenencies for this book with:

```bash
uv pip install -r .\requirements.txt
```
