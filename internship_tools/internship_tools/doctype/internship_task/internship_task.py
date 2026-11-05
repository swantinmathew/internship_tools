# Copyright (c) 2026, Swantin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate, today


class InternshipTask(Document):
    def validate(self):
        self.validate_task_title()
        self.validate_due_date()

    def validate_task_title(self):
        if not self.task_title or not self.task_title.strip():
            frappe.throw("Task Title is required.")

    def validate_due_date(self):
        if (
            self.due_date
            and self.has_value_changed("due_date")
            and getdate(self.due_date) < getdate(today())
        ):
            frappe.throw("Due Date cannot be in the past.")


@frappe.whitelist()
def complete_task(task_name):
    task = frappe.get_doc("Internship Task", task_name)

    task.check_permission("write")

    if task.status == "Completed":
        return "Task is already completed."

    task.status = "Completed"
    task.save()

    return "Task completed successfully."

def get_task_permission_query(user):
    """Restrict Interns to tasks assigned to their own account."""

    if not user:
        user = frappe.session.user

    if user == "Administrator":
        return None

    roles = frappe.get_roles(user)

    if "System Manager" in roles or "Mentor" in roles:
        return None

    if "Intern" in roles:
        return f"`tabInternship Task`.`assigned_to` = {frappe.db.escape(user)}"

    return "1=0"


def has_task_permission(doc, user=None, permission_type=None):
    """Check whether a user can access a specific Internship Task."""

    if not user:
        user = frappe.session.user

    if user == "Administrator":
        return True

    roles = frappe.get_roles(user)

    if "System Manager" in roles or "Mentor" in roles:
        return True

    if "Intern" in roles:
        return doc.assigned_to == user

    return False
