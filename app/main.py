from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
def hello():
    return {"msg", "Hello"}

@app.get('/users/{id}')
def get(id: int):
    return {"user", id}
