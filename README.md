# 🔐 RedactAI – The Smart Security Redactor

RedactAI is a GPT-powered privacy tool that automatically redacts sensitive content from uploaded PDF or text files. It uses a smart GenAI backend to detect personally identifiable information (PII), financials, medical terms, and other sensitive data — then visually redacts it using either black boxes or labeled placeholders directly on the original document.

> “Built for privacy, designed for clarity.”

---

## 🚀 Features

✅ Upload PDFs or paste raw text  
✅ Automatically detects sensitive information (names, emails, addresses, financials, etc.)  
✅ Two redaction styles:  
  – **Blackout**: Draws black boxes over the sensitive content  
  – **Placeholder**: Replaces with tags like `[NAME]`, `[EMAIL]`, `[REDACTED]`  
✅ Redactions rendered directly on the original PDF (no content layout lost)  
✅ Streamlit UI – clean, fast, and intuitive  
✅ Powered by OpenAI’s GPT-3.5


---

## 📂 Project Structure

RedactAI/
├── app.py                 # Streamlit frontend
├── redact_utils.py        # GPT-based redaction logic
├── pdf_utils.py           # In-place PDF redaction (blackout + placeholder)
├── prompts.py             # LLM prompt templates
├── requirements.txt       # Python dependencies
├── sample_docs/           # Optional test files
└── README.md              # This file


## 🛠️ Installation & Usage

### 1. Clone the Repository

``bash
git clone https://github.com/abhinavc97/RedactAI.git
cd RedactAI

2. Set Up a Virtual Environment

python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Set Your OpenAI API Key

You must have an OpenAI API key (from https://platform.openai.com/)

export OPENAI_API_KEY="sk-..."       # macOS/Linux
set OPENAI_API_KEY="sk-..."          # Windows CMD
$env:OPENAI_API_KEY="sk-..."         # PowerShell

5. Launch the App

streamlit run app.py

Visit http://localhost:8501 in your browser.

⸻

📄 Example Input

John Doe lives at 123 Main Street. His email is john.doe@example.com and his salary is $95,000.

Placeholder style:

[NAME] lives at [ADDRESS]. His email is [EMAIL] and his salary is [NUMBER].

Blackout style:
The original PDF will show black boxes over the redacted phrases.

⸻

📦 Requirements
	•	Python 3.8+
	•	Streamlit
	•	OpenAI SDK (v1+)
	•	PyMuPDF (fitz)
	•	pdfplumber
	•	reportlab

Install all via:

pip install -r requirements.txt



⸻

🧠 How It Works
	1.	Text is extracted from PDF (or taken from input box)
	2.	Prompt sent to OpenAI GPT to generate a redacted version
	3.	Differences are analyzed using difflib
	4.	Matching text is blacked out or replaced with a placeholder using PyMuPDF
	5.	A downloadable PDF is returned with all redactions applied visually

⸻

💡 Future Enhancements
	•	CSV export of redacted terms for audit logs
	•	NER fallback model using spaCy
	•	Support for docx or image-based OCR input
	•	Redaction previews with highlight toggles
	•	Deploy to HuggingFace or Render

