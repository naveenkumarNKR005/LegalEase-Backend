# LegalEase — Project Report

## Abstract
LegalEase is an AI-assisted multilingual legal-document generation prototype developed using Python, Streamlit and FastAPI. The application converts structured user inputs into editable legal-document drafts and supports English, Tamil and Hindi. Google Gemini can be used for AI-assisted drafting, while deterministic templates provide a fallback when the API is unavailable. Documents can be exported to DOCX and PDF.

## Problem statement
Legal documents often use complex terminology and rigid structures. A first draft can take time to prepare, especially for users who are more comfortable with regional languages.

## Proposed solution
LegalEase provides a simple form-based interface and an AI-assisted generation workflow. It emphasizes transparency by showing a legal-review disclaimer and by avoiding invented facts in the AI prompt.

## Objectives
- Build a simple legal-tech prototype.
- Support multilingual document drafting.
- Demonstrate AI + API + document automation.
- Provide editable and downloadable output.
- Follow secure API-key practices.

## Methodology
Input → Validation → AI/template generation → Review/edit → DOCX/PDF export.

## Results
The prototype supports five document categories, three languages, optional Gemini generation, fallback templates, and downloadable documents.

## Future scope
Authentication, database storage, document history, jurisdiction-specific validated templates, stronger multilingual PDF typography, human review workflows and cloud deployment.

## Disclaimer
This project is an educational prototype. It does not constitute legal advice.
