# utils/pdf_generation.py
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

def generate_case_pdf(analysis, summary):
    """Generate a PDF from analysis and summary."""
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.drawString(100, 750, "Case Summary")
    y = 730
    for entity in analysis.get("entities", []):
        c.drawString(100, y, f"{entity['label']}: {entity['word']}")
        y -= 20
    c.drawString(100, y, "Summary:")
    y -= 20
    for line in summary.split('\n'):
        c.drawString(100, y, line)
        y -= 15
    c.save()
    buffer.seek(0)
    return buffer.getvalue()