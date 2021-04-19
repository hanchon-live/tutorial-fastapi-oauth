from fastapi import FastAPI

api_app = FastAPI()


@api_app.get('/')
def test():
    return {'message': 'api_app'}
