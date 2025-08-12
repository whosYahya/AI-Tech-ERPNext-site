import frappe
from frappe.utils import get_site_path

# Optional: if you want to call OpenAI or use PDF parser
# import fitz  # PyMuPDF
# import openai

def extract_resume_data(doc, method):
    if not doc.resume:
        frappe.logger().info("No resume uploaded.")
        return

    path = get_site_path("public", doc.resume)
    frappe.logger().info(f"Resume uploaded at: {path}")

    # === Example: Extract dummy text ===
    # Replace this with actual PDF/AI logic
    resume_text = "Experienced Python developer with 3 years in Django and Frappe"

    # Simulated AI extraction
    doc.skills = "Python, Django, Frappe"
    doc.experience = "3 years"
    doc.save()
