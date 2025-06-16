from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import tempfile
import fitz
import difflib

def extract_redacted_phrases(original_text, redacted_text):
    diff = difflib.ndiff(original_text.split(), redacted_text.split())
    redacted_phrases = [word[2:] for word in diff if word.startswith('- ')]
    return list(set(redacted_phrases))  # Remove duplicates

def get_placeholder_for(term):
    term_lower = term.lower()
    if "@" in term_lower:
        return "[EMAIL]"
    elif term_lower.isdigit() and len(term_lower) >= 5:
        return "[ID]"
    elif any(char.isdigit() for char in term_lower):
        return "[DATE]" if "-" in term or "/" in term else "[NUMBER]"
    elif len(term_lower.split()) >= 2:
        return "[NAME]"
    else:
        return "[REDACTED]"

def generate_placeholder_pdf(original_pdf, redacted_text, original_text):
    redacted_terms = extract_redacted_phrases(original_text, redacted_text)
    doc = fitz.open(original_pdf)

    for page in doc:
        for term in redacted_terms:
            rects = page.search_for(term)
            for rect in rects:
                print(f"→ Redacting: '{term}' at {rect}")

                # Step 1: Draw white box (remove black border)
                page.draw_rect(rect, fill=(1, 1, 1), color=None)

                # Step 2: Add placeholder using insert_text()
                placeholder = get_placeholder_for(term)
                font_size = max(rect.y1 - rect.y0 - 2, 8)

                # Insert text slightly above the bottom of the box
                page.insert_text(
                    point=(rect.x0, rect.y1 - 2),  # x0, slightly above bottom y
                    text=placeholder,
                    fontsize=font_size,
                    fontname="helv",
                    color=(0, 0, 0)
                )

    output_path = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name
    doc.save(output_path)
    return output_path


def generate_blackout_pdf(original_pdf, redacted_text, original_text):
    redacted_terms = extract_redacted_phrases(original_text, redacted_text)
    print("🔍 Redacted Terms Detected:")
    for term in redacted_terms:
        print(f"  - {term}")
    
    doc = fitz.open(original_pdf)

    for page in doc:
        for term in redacted_terms:
            text_instances = page.search_for(term)
            for inst in text_instances:
                page.draw_rect(inst, fill=(0, 0, 0), color=(0, 0, 0))

    output_path = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name
    doc.save(output_path)
    return output_path