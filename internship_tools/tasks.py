import frappe
from frappe.utils import today


def update_overdue_tasks():
    """Mark unfinished tasks with past due dates as Overdue."""

    frappe.db.sql(
        """
        UPDATE `tabInternship Task`
        SET status = 'Overdue'
        WHERE due_date < %s
          AND status != 'Completed'
          AND status != 'Overdue'
        """,
        (today(),),
    )

    frappe.db.commit()
