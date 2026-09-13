from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class InvestigationRequest(BaseModel):
    question: str


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "ARGUS AI"
    }


@app.post("/investigate")
def investigate(request: InvestigationRequest):
    return {
        "question": request.question,
        "status": "investigation_started"
    }