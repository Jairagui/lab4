# calculadora api
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Calculadora")

@app.get("/")
def inicio():
    return {"app": "calculadora", "status": "ok"}

@app.get("/suma")
def suma(a: float, b: float):
    return {"op": "suma", "resultado": a + b}

@app.get("/resta")
def resta(a: float, b: float):
    return {"op": "resta", "resultado": a - b}

@app.get("/multi")
def multi(a: float, b: float):
    return {"op": "multi", "resultado": a * b}

@app.get("/div")
def div(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="No se puede dividir entre cero")
    return {"op": "div", "resultado": a / b}
