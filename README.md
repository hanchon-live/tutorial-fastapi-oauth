# FastAPI and Google Login (OAuth)
This is an example following the tutorials:
- [Guide 1 - Google OAuth Login with FastAPI](https://blog.hanchon.live/guides/google-login-with-fastapi/)
- [Guide 2 - Google OAuth and FastAPI JWT](https://blog.hanchon.live/guides/google-login-with-fastapi-and-jwt/)
- [Guide 3 - JWT blacklist and refresh tokens](https://blog.hanchon.live/guides/jwt-tokens-and-fastapi/)

## Requirements:
- Python3.6+

## How to run the example:
- Create a virtualenv `python3 -m venv .venv`
- Activate the virtualenv `. .venv/bin/activate`
- Install the requirements `pip install -r requirements.txt`
- Set up the env vars:
    - export GOOGLE_CLIENT_ID=...
    - export GOOGLE_CLIENT_SECRET=...
    - export SECRET_KEY=...
    - export API_SECRET_KEY=...
- Run the app:
    - Guide 1: `python run.py`
    - Guide 2 and 3: `python main.py`
