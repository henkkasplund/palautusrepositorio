# tdd-ostoskori – agent instructions

- uv project, Python 3.14. Run commands from this directory. Install deps with `uv sync`.
- Tests are under `src/tests` and are executed with `uv run pytest`.
- The class under development is `Ostoskori` in `src/ostoskori.py`.

# Rules
- Code of `src/ostos.py` and `src/tuote.py` must not be changed.
- Tests must not be edited unless explicitly asked.
- Always implement the absolutely minimal code that makes the currently failing test pass. Do not implement anything that no test requires, even if comments in the code describe it. Hardcoded or trivial return values are fine if they make the tests pass.
- Work only in this directory.
