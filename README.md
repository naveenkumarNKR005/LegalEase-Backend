# ⚖️ LegalEase

**AI-Assisted Multilingual Legal Document Generator**

LegalEase is a SmartBridge educational project prototype that helps users create structured drafts of common legal documents from simple inputs. It supports English, Tamil and Hindi, optional Gemini AI generation, editable previews, and DOCX/PDF export.

> **Important:** LegalEase is an educational prototype and does not provide legal advice. Generated drafts must be reviewed by a qualified legal professional before real-world use.

## Features

- Streamlit web interface
- FastAPI backend
- Gemini AI integration
- Template fallback when Gemini is unavailable
- English / Tamil / Hindi
- Rental Agreement, Leave & License Agreement, Affidavit, Legal Notice and Declaration categories
- Editable generated document
- DOCX export
- PDF export
- API health endpoint
- Secret-safe configuration

## Project architecture

```text
User
  ↓
Streamlit UI
  ↓
FastAPI API / service layer
  ↓
Gemini AI OR safe template fallback
  ↓
Document formatter
  ↓
DOCX / PDF
```

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Optional API server:

```bash
uvicorn backend.main:app --reload
```

## Gemini setup

Create an API key in Google AI Studio, then set:

```bash
export GEMINI_API_KEY="YOUR_KEY"
```

For Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="YOUR_KEY"
```

Never commit API keys. For Streamlit deployment, put secrets in the platform's secret manager instead of the repository.

## SmartBridge phases

See `docs/` for the eight project phases.

## Testing

Basic functional tests are documented in `docs/06_Project_Testing.md`.

## Future improvements

- User authentication
- Database and document history
- More document categories
- Regional legal-template validation
- Human legal-review workflow
- Digital signatures
- Better multilingual PDF font support
- Cloud deployment with protected API credentials
