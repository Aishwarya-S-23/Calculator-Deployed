from fastapi import FastAPI
from pydantic import BaseModel
from calculator import tokenize , compute
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ExpRequest(BaseModel):
  expression:str


@app.get("/")
def index():
  return {"message":"Calulator API is running fine"}

@app.post("/result")
def calculate(request: ExpRequest):
  try:
    tokens = tokenize(request.expression)
    answer = compute(tokens)
    return {
      "Expression " : request.expression,
      "result" : answer
    }
  except Exception as e:
    return {
      "error": str(e)
    }

  finally:
    print("Calculation completed")