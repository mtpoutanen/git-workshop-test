from fastapi import FastAPI

app = FastAPI()

@app.get("/hello1")
def read_hello1():
  return {"message": "Hello World 1"}

@app.get("/hello2")
def read_hello2():
  return {"message": "Hello World 2"}

@app.get("/hello3")
def read_hello3():
  return {"message": "Hello World 3"}

@app.get("/hello4")
def read_hello4():
  return {"message": "Hello World 4"}

@app.get("/hello5")
def read_hello5():
  return {"message": "Hello World 5"}

@app.get("/hello6")
def read_hello6():
  return {"message": "Hello World 6"}

@app.get("/hello7")
def read_hello7():
  return {"message": "Hello World 7"}

@app.get("/hello8")
def read_hello8():
  return {"message": "Hello World 8"}

@app.get("/hello9")
def read_hello9():
  return {"message": "Hello World 9"}

@app.get("/hello10")
def read_hello10():
  return {"message": "Hello World 10"}
