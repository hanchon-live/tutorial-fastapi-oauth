# FastAPI and Google Login (OAuth)
This is an example following the tutorial on https://blog.hanchon.live/guides/google-login-with-fastapi/

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
- Run the app: `python run.py`
