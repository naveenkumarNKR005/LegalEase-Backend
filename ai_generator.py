import os

def gemini_available():
    return bool(os.getenv("GEMINI_API_KEY"))

def generate_with_gemini(data):
    try:
        from google import genai
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        model = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
        prompt = f"""
You are an AI-assisted legal document drafting component for an educational software project.
Create a clear, professional draft based ONLY on the supplied facts.
Do not invent names, dates, amounts, laws, clauses, case numbers, or legal rights.
If information is missing, use [TO BE FILLED].
Use the requested language.
Clearly state that the document is a draft requiring human/legal-professional review.
Document type: {data['document_type']}
Language: {data['language']}
First party/applicant: {data['party_a']}
Second party/respondent: {data['party_b']}
Address: {data['address']}
Purpose: {data['purpose']}
Date: {data['date']}
Duration: {data['duration']}
Amount: {data['amount']}
Additional terms: {data['extra']}
"""
        response = client.models.generate_content(model=model, contents=prompt)
        return response.text
    except Exception:
        from services.document_generator import generate_document
        return generate_document(data)
