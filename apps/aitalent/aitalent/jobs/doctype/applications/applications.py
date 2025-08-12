import frappe
import requests
from frappe.utils.file_manager import get_file_path

class Applications(frappe.model.document.Document):
    def on_submit(self):
        frappe.logger().info(f"Submitted Application: {self.full_name}")

        if not self.resume:
            frappe.throw("No resume file attached.")

        try:
            resume_path = get_file_path(self.resume)

            with open(resume_path, 'rb') as resume_file:
                response = requests.post(
                    "http://localhost:9000/extract-skills",
                    files={"resume": resume_file}
                )

            if response.status_code != 200:
                frappe.throw(f"Skill extraction failed with status {response.status_code}")

            data = response.json()

            if "skills" not in data:
                frappe.throw(f"Invalid response from AI service: {data}")

            skills = data["skills"]

            self.skills_table = []  # Clear existing skills
            for skill in skills:
                self.append("skills_table", {"skill_name": skill})
                
            self.skills_summary = ", ".join(skills)

            self.db_update()

        except requests.exceptions.RequestException:
            frappe.log_error(frappe.get_traceback(), "Connection to AI API failed")
            frappe.throw("Failed to connect to the AI skill extraction service.")

        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Skill Extraction Error")
            frappe.throw(f"Failed to extract skills: {str(e)}")
        else:
            frappe.logger().info(f"Skills extracted and saved for {self.full_name}")
            frappe.msgprint(f"Skills extracted successfully for {self.full_name}.")
            