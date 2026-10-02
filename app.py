import streamlit as st
from services.document_generator import generate_document
from services.translator import translate_text
from services.ai_generator import generate_with_gemini, gemini_available
from services.exporter import make_docx, make_pdf

st.set_page_config(page_title="LegalEase", page_icon="⚖️", layout="wide")

st.title("⚖️ LegalEase")
st.caption("AI-assisted multilingual legal document generator")
st.info("Educational project only. LegalEase does not provide legal advice. Review generated documents with a qualified legal professional before real-world use.")

with st.sidebar:
    st.header("Document Settings")
    language = st.selectbox("Language", ["English", "Tamil", "Hindi"])
    document_type = st.selectbox(
        "Document type",
        ["Rental Agreement", "Leave & License Agreement", "Affidavit", "General Legal Notice", "Declaration"]
    )
    use_ai = st.checkbox("Use Gemini AI when API key is available", value=True)
    st.divider()
    st.write("**AI status:**", "Connected" if gemini_available() else "Template fallback")

st.subheader("Enter document details")
col1, col2 = st.columns(2)

with col1:
    party_a = st.text_input("First party / Applicant name")
    party_b = st.text_input("Second party / Respondent name")
    address = st.text_area("Address")
    purpose = st.text_area("Purpose / reason")

with col2:
    date = st.date_input("Date")
    duration = st.text_input("Duration (if applicable)", placeholder="e.g. 11 months")
    amount = st.text_input("Amount / consideration (if applicable)", placeholder="e.g. ₹15,000 per month")
    extra = st.text_area("Additional terms", placeholder="Add any other important terms...")

if st.button("Generate Document", type="primary", use_container_width=True):
    if not party_a or not purpose:
        st.error("Please enter at least the first party/applicant name and purpose.")
    else:
        data = {
            "document_type": document_type,
            "language": language,
            "party_a": party_a,
            "party_b": party_b,
            "address": address,
            "purpose": purpose,
            "date": str(date),
            "duration": duration,
            "amount": amount,
            "extra": extra,
        }
        with st.spinner("Generating your document..."):
            if use_ai and gemini_available():
                result = generate_with_gemini(data)
            else:
                result = generate_document(data)
        st.session_state["document"] = result
        st.session_state["data"] = data

if "document" in st.session_state:
    st.divider()
    st.subheader("Generated Document")
    edited = st.text_area("Review / edit before export", st.session_state["document"], height=520)
    st.session_state["document"] = edited

    c1, c2 = st.columns(2)
    with c1:
        docx_bytes = make_docx(edited, document_type)
        st.download_button("Download DOCX", docx_bytes, "LegalEase_Document.docx",
                           "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                           use_container_width=True)
    with c2:
        try:
            pdf_bytes = make_pdf(edited, document_type)
            st.download_button("Download PDF", pdf_bytes, "LegalEase_Document.pdf",
                               "application/pdf", use_container_width=True)
        except Exception as e:
            st.warning("PDF export is unavailable in this environment. DOCX export is still available.")

st.divider()
st.caption("LegalEase • SmartBridge project prototype • Human review required")
