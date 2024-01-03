from fastapi import FastAPI
from typing import Dict

app = FastAPI()

@app.get("/hello1")
def read_hello1() -> Dict[str, str]:
    return {"message": "Hello World 1"}

@app.get("/hello2")
def read_hello2() -> Dict[str, str]:
    return {"message": "Hello World 2"}

@app.get("/hello3")
def read_hello3() -> Dict[str, str]:
    return {"message": "Hello World 3"}

@app.get("/hello4")
def read_hello4() -> Dict[str, str]:
    return {"message": "Hello World 4"}

@app.get("/hello5")
def read_hello5() -> Dict[str, str]:
    return {"message": "Hello World 5"}

@app.get("/hello6")
def read_hello6() -> Dict[str, str]:
    return {"message": "Hello World 6"}

@app.get("/hello7")
def read_hello7() -> Dict[str, str]:
    return {"message": "Hello World 7"}

@app.get("/hello8")
def read_hello8() -> Dict[str, str]:
    return {"message": "Hello World 8"}

@app.get("/hello9")
def read_hello9() -> Dict[str, str]:
    return delete_all_users()

@app.get("/hello10")
def read_hello10() -> Dict[str, str]:
    return {"message": "Hello World 10"}
