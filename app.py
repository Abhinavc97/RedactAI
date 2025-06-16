import streamlit as st
from redact_utils import redact_text
import openai
import os
import pdfplumber
import tempfile

from pdf_utils import generate_blackout_pdf, generate_placeholder_pdf

st.set_page_config(page_title="🔐 RedactAI", layout="wide")

st.title("🔐 RedactAI – The Smart Security Redactor")


openai.api_key = os.getenv("OPENAI_API_KEY")

text = st.text_area("Paste your text here:", height=250)
#mode = st.selectbox("Choose Redaction Mode", ["Legal", "Anonymization", "Zero-Trust"])

if st.button("Redact Now"):
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        redacted_text, explanation = redact_text(text)
        st.subheader("🧾 Redacted Text")
        st.code(redacted_text, language='markdown')
        st.subheader("💡 Explanation")
        st.write(explanation)



import fitz  # PyMuPDF

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
redaction_style = st.radio("Redaction Output", ["Blackout", "Placeholder"])

if uploaded_file and st.button("Process PDF"):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
        temp.write(uploaded_file.read())
        temp_path = temp.name

    with pdfplumber.open(temp_path) as pdf:
        full_text = "\n".join(page.extract_text() or "" for page in pdf.pages)

    redacted_text, explanation = redact_text(full_text)

    if redaction_style == "Placeholder":
        # Replace and regenerate PDF with placeholder text
        redacted_pdf_path = generate_placeholder_pdf(temp_path, redacted_text, full_text)
    else:
        # Overlay blackout boxes (visual redaction)
       redacted_pdf_path = generate_blackout_pdf(temp_path, redacted_text, full_text)

    st.download_button("Download Redacted PDF", open(redacted_pdf_path, "rb"), file_name="Redacted.pdf")

    st.subheader("Explanation")
    st.write(explanation)