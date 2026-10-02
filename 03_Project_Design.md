# Phase 3 — Project Design

## Architecture

```text
+-------------------+
|   Streamlit UI    |
+---------+---------+
          |
          v
+-------------------+
| Service / FastAPI |
+---------+---------+
          |
     +----+----+
     |         |
     v         v
 Gemini AI   Templates
     |         |
     +----+----+
          |
          v
+-------------------+
| Document Exporter |
+---------+---------+
          |
      DOCX / PDF
```

## Main modules
- `app.py`: user interface
- `backend/main.py`: API
- `services/ai_generator.py`: Gemini integration
- `services/document_generator.py`: multilingual fallback templates
- `services/exporter.py`: DOCX/PDF output
