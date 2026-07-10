from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.calculator import calculate
from app.version import VERSION

app = FastAPI(
    title="Calculator API",
    version=VERSION
)


class CalculationRequest(BaseModel):
    a: float
    b: float
    operation: str


@app.get("/")
def root():
    return {
        "message": "Calculator API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }


@app.get("/version")
def version():
    return {
        "version": VERSION
    }


@app.post("/calculate")
def calculate_endpoint(request: CalculationRequest):
    try:
        result = calculate(
            request.a,
            request.b,
            request.operation
        )
        return {
            "result": result
        }
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )