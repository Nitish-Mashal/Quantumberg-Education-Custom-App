import frappe
from student_portal_access.navbarSettings import patch_help_dropdown  # 👈 import your patcher

def custom_boot(bootinfo):
    user = frappe.session.user
    roles = frappe.get_roles(user)

    # Set homepage for Student users
    if "Student" in roles:
        bootinfo['home_page'] = '/student-portal/schedule'

    # Call your navbar patch function
    patch_help_dropdown(bootinfo)

    return bootinfo
