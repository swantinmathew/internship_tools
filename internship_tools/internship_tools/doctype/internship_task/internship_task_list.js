frappe.listview_settings["Internship Task"] = {
    add_fields: ["status", "priority"],

    get_indicator: function (doc) {
        const status_colors = {
            "Open": "red",
            "In Progress": "orange",
            "Overdue": "red",
            "Completed": "green"
        };

        return [
            __(doc.status),
            status_colors[doc.status] || "gray",
            "status,=," + doc.status
        ];
    },

    formatters: {
        priority: function (value) {
            const priority_colors = {
                "Urgent": "red",
                "High": "orange",
                "Medium": "blue",
                "Low": "green"
            };

            const color = priority_colors[value] || "gray";

            return `<span class="indicator-pill ${color}">${__(value || "Medium")}</span>`;
        }
    }
};
