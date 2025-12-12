from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
  print("read_root called")
