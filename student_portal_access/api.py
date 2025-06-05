# import frappe

# def custom_boot(bootinfo):
#     user = frappe.session.user
#     roles = frappe.get_roles(user)

#     # If the user is a Student, change the home page route
#     if "Student" in roles:
#         bootinfo['home_page'] = '/student-portal/schedule'

#     return bootinfo

# import frappe

# def custom_boot(bootinfo):
#     user = frappe.session.user
#     roles = frappe.get_roles(user)

#     # Only redirect students
#     if "Student" in roles:
#         # Set the home_page to your custom student portal
#         bootinfo['home_page'] = '/student-portal'

#         # Just to be extra safe, in case any Workspace tries to override
#         if bootinfo.get("module_app") == "welcome-workspace":
#             bootinfo["home_page"] = "/student-portal"

#     return bootinfo


