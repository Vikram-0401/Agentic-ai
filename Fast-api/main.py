from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/mail")
def read_root():
    return {"email": "vikram@gmail.com"}
