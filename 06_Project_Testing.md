# Phase 6 — Project Testing

## Test cases

| ID | Test | Expected result |
|---|---|---|
| T01 | Open application | UI loads |
| T02 | Submit without required fields | Validation message appears |
| T03 | Generate English document | English draft appears |
| T04 | Generate Tamil document | Tamil draft appears |
| T05 | Generate Hindi document | Hindi draft appears |
| T06 | Gemini unavailable | Template fallback works |
| T07 | Download DOCX | DOCX file downloads |
| T08 | Download PDF | PDF file downloads |
| T09 | API health | `/health` returns status |
| T10 | API generation | `/generate` returns document |

## Security test
A real Gemini API key must not appear in source files or Git history. `.env` and Streamlit secrets are excluded through `.gitignore`.
