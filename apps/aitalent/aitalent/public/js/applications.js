console.log("🟢 Applications JS loaded");

frappe.ui.form.on('Applications', {
    refresh: function(frm) {
        if (!frm.is_new()) {
            frm.add_custom_button('🛠 Extract Skills', function() {
                frappe.call({
                    method: "aitalent.jobs.doctype.applications.applications.extract_skills",
                    args: {
                        docname: frm.doc.name
                    },
                    callback: function(r) {
                        if (r.message) {
                            frm.reload_doc();  // refresh to show new rows
                            frappe.msgprint("✅ Skills extracted from resume.");
                        }
                    }
                });
            });
        }
    }
});
