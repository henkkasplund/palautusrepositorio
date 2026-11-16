# Login project guidance

- This is a `uv` project; run Python and test commands as `uv run ...` from this directory. If dependencies are missing, run `uv sync`.
- Start the Flask app with `uv run python src/index.py`. It listens on port `5001`.
- Start the app in the background and stop it when finished; port 5001 must be free.
- Run the Robot Framework browser tests with `uv run robot src/tests`. The app must already be running on `localhost:5001` while tests run. Initialize Playwright browsers once with `uv run rfbrowser install chromium` if needed.
- Username and password validation for registration is in `src/services/user_service.py`, in `UserService.validate`; login credential checks are in `UserService.check_credentials` in the same file.
