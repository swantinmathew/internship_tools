// Copyright (c) 2026, Swantin and contributors
// For license information, please see license.txt

frappe.ui.form.on("Internship Task", {
    refresh(frm) {
        // Do not show the button for a new, unsaved task.
        if (frm.is_new()) {
            return;
        }

        // Show the button only when the task is not completed.
        if (frm.doc.status !== "Completed") {
            frm.add_custom_button("Complete Task", () => {
                frappe.call({
                    method: "internship_tools.internship_tools.doctype.internship_task.internship_task.complete_task",
                    args: {
                        task_name: frm.doc.name
                    },
                    callback: function (r) {
                        if (!r.exc) {
                            frappe.show_alert({
                                message: r.message,
                                indicator: "green"
                            });
                            frm.reload_doc();
                        }
                    }
                });
            });
        }
    },
});
