from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
  print("read_root called")
  return {"message": "FastAPI + WhatsApp Integration"}


@app.get("/health")
def health_check():
  print("health_check called")
  return {"status": "ok"}
