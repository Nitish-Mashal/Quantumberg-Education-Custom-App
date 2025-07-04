app_name = "student_portal_access"
app_title = "Student Portal Access"
app_publisher = "Nitish"
app_description = "Education_App"
app_email = "nitishmashal0@gmail.com"
app_license = "mit"

export_python_type_annotations = True

# Web route
app_include_frontend = "frontend/index.html"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "student_portal_access",
# 		"logo": "/assets/student_portal_access/logo.png",
# 		"title": "Student Portal Access",
# 		"route": "/student_portal_access",
# 		"has_permission": "student_portal_access.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/student_portal_access/css/student_portal_access.css"
# app_include_js = "/assets/student_portal_access/js/student_portal_access.js"

app_include_js = "/assets/student_portal_access/js/student_redirect.js"

# doc_events = {
#     "Notification Log": {
#         "after_insert": "student_portal_access.api.notifications.push_realtime_notification"
#     }
# }


doc_events = {
    "Notification Log": {
        "after_insert": "student_portal_access.api.notifications.push_realtime_notification"
    },
    "Student": {
        "on_update": "student_portal_access.api.notifications.fix_student_notification_recipient"
    }
}


app_include_js = "/assets/frappe/js/frappe-web.bundle.js"

# app_include_js = "student_portal_access/public/js/student_redirect.js"

# I added this code {

# boot_session = "student_portal_access.api.custom_boot"

# role_home_page = {
#     "Student": "/student-dashboard"
# }

# after_install = "student_portal_access.navbarSettings.setup_help_dropdown"

# before_uninstall = "student_portal_access.navbarSettings.revert_help_dropdown"

after_install = "student_portal_access.navbarSettings.setup_help_dropdown"

before_uninstall = "student_portal_access.navbarSettings.revert_help_dropdown"



# I added this code }

# include js, css files in header of web template
# web_include_css = "/assets/student_portal_access/css/student_portal_access.css"
# web_include_js = "/assets/student_portal_access/js/student_portal_access.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "student_portal_access/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "student_portal_access/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "student_portal_access.utils.jinja_methods",
# 	"filters": "student_portal_access.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "student_portal_access.install.before_install"
# after_install = "student_portal_access.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "student_portal_access.uninstall.before_uninstall"
# after_uninstall = "student_portal_access.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "student_portal_access.utils.before_app_install"
# after_app_install = "student_portal_access.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "student_portal_access.utils.before_app_uninstall"
# after_app_uninstall = "student_portal_access.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "student_portal_access.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"student_portal_access.tasks.all"
# 	],
# 	"daily": [
# 		"student_portal_access.tasks.daily"
# 	],
# 	"hourly": [
# 		"student_portal_access.tasks.hourly"
# 	],
# 	"weekly": [
# 		"student_portal_access.tasks.weekly"
# 	],
# 	"monthly": [
# 		"student_portal_access.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "student_portal_access.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "student_portal_access.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "student_portal_access.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["student_portal_access.utils.before_request"]
# after_request = ["student_portal_access.utils.after_request"]

# Job Events
# ----------
# before_job = ["student_portal_access.utils.before_job"]
# after_job = ["student_portal_access.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"student_portal_access.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

