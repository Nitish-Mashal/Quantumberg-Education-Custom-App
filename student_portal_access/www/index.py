# import frappe

# def get_context(context):
#     user = frappe.session.user

#     # Redirect Guests to login
#     if user == "Guest":
#         frappe.local.flags.redirect_location = "/login"
#         raise frappe.Redirect

#     # Redirect Students to student portal schedule
#     if "Student" in frappe.get_roles(user):
#         frappe.local.flags.redirect_location = "/student-portal/schedule"
#         raise frappe.Redirect

#     # Other users stay on the default homepage
#     return context
