import frappe
from frappe import _

@frappe.whitelist()
def get_logged_in_user():
    if not frappe.session.user or frappe.session.user == "Guest":
        frappe.throw(_("User not logged in"), frappe.PermissionError)
    
    user = frappe.get_doc("User", frappe.session.user)

    # Ensure the user has a student role
    if "Student" not in [role.role for role in user.roles]:
        frappe.throw(_("Access Denied: Not a Student"), frappe.PermissionError)
    
    return {
        "email": user.email,
        "full_name": user.full_name,
        "roles": [role.role for role in user.roles]
    }
