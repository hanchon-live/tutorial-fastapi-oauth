import uvicorn
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse

from apps.api import api_app
from apps.auth import auth_app

app = FastAPI()
app.mount('/auth', auth_app)
app.mount('/api', api_app)


@app.get('/')
async def root():
    return HTMLResponse('<body><a href="/auth/login">Log In</a></body>')


@app.get('/token')
async def token(request: Request):
    return HTMLResponse('''
                <script>
                function send(){
                    var req = new XMLHttpRequest();
                    req.onreadystatechange = function() {
                        if (req.readyState === 4) {
                            console.log(req.response);
                            if (req.response["result"] === true) {
                                window.localStorage.setItem('jwt', req.response["access_token"]);
                            }
                        }
                    }
                    req.withCredentials = true;
                    req.responseType = 'json';
                    req.open("get", "/auth/token?"+window.location.search.substr(1), true);
                    req.send("");

                }
                </script>
                <button onClick="send()">Get FastAPI JWT Token</button>

                <button onClick='fetch("http://127.0.0.1:7000/api/").then(
                    (r)=>r.json()).then((msg)=>{console.log(msg)});'>
                Call Unprotected API
                </button>
                <button onClick='fetch("http://127.0.0.1:7000/api/protected").then(
                    (r)=>r.json()).then((msg)=>{console.log(msg)});'>
                Call Protected API without JWT
                </button>
                <button onClick='fetch("http://127.0.0.1:7000/api/protected",{
                    headers:{
                        "Authorization": "Bearer " + window.localStorage.getItem("jwt")
                    },
                }).then((r)=>r.json()).then((msg)=>{console.log(msg)});'>
                Call Protected API wit JWT
                </button>
            ''')


if __name__ == '__main__':
    uvicorn.run(app, port=7000)
