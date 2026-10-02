from fastapi import FastAPI
from pydantic import BaseModel
from services.document_generator import generate_document
from services.ai_generator import generate_with_gemini, gemini_available

app = FastAPI(title="LegalEase API", version="1.0.0")

class DocumentRequest(BaseModel):
    document_type: str
    language: str
    party_a: str
    party_b: str = ""
    address: str = ""
    purpose: str
    date: str
    duration: str = ""
    amount: str = ""
    extra: str = ""
    use_ai: bool = True

@app.get("/")
def root():
    return {"project": "LegalEase", "status": "running"}

@app.get("/health")
def health():
    return {"status": "ok", "gemini_available": gemini_available()}

@app.post("/generate")
def generate(request: DocumentRequest):
    data = request.model_dump()
    if request.use_ai and gemini_available():
        document = generate_with_gemini(data)
    else:
        document = generate_document(data)
    return {"document": document}
