import frappe

def custom_boot(bootinfo):
    user = frappe.session.user
    roles = frappe.get_roles(user)

    # If the user is a Student, change the home page route
    if "Student" in roles:
        bootinfo['home_page'] = '/student-portal/schedule'

    return bootinfo