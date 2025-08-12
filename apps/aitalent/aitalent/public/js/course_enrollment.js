console.log("🟢 JS for Course Enrollment loaded");

frappe.ui.form.on('Course Enrollment', {
    refresh: function(frm) {
        frm.add_custom_button('🎯 Dummy Button', function() {
            frappe.msgprint('✅ The button works!');
        });
    }
});
