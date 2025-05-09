app_name = "location_sharing_app"
app_title = "Location Sharing App"
app_publisher = "CloudGCS"
app_description = "Location Sharing System"
app_email = "contact@cloudgcs.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

fixtures = [{"dt": "Custom HTML Block"}, {"dt": "Web Page"}]

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "location_sharing_app",
# 		"logo": "/assets/location_sharing_app/logo.png",
# 		"title": "Location Sharing App",
# 		"route": "/location_sharing_app",
# 		"has_permission": "location_sharing_app.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = ["/assets/location_sharing_app/css/location_sharing_app.css"]
# app_include_js = "/assets/location_sharing_app/js/location_sharing_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/location_sharing_app/css/location_sharing_app.css"
# web_include_js = "/assets/location_sharing_app/js/location_sharing_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "location_sharing_app/public/scss/website"

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
# app_include_icons = "location_sharing_app/public/icons.svg"

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
# 	"methods": "location_sharing_app.utils.jinja_methods",
# 	"filters": "location_sharing_app.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "location_sharing_app.install.before_install"
# after_install = "location_sharing_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "location_sharing_app.uninstall.before_uninstall"
# after_uninstall = "location_sharing_app.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "location_sharing_app.utils.before_app_install"
# after_app_install = "location_sharing_app.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "location_sharing_app.utils.before_app_uninstall"
# after_app_uninstall = "location_sharing_app.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "location_sharing_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

permission_query_conditions = {
    "Aircraft": "location_sharing_app.location_sharing_app.doctype.aircraft.aircraft.get_aircraft_query"
}
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
# 		"location_sharing_app.tasks.all"
# 	],
# 	"daily": [
# 		"location_sharing_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"location_sharing_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"location_sharing_app.tasks.weekly"
# 	],
# 	"monthly": [
# 		"location_sharing_app.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "location_sharing_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
    "get_aircrafts": "location_sharing_app.location_sharing_app.doctype.aircraft.aircraft.get_aircrafts",
    "get_aircraft_by_name": "location_sharing_app.location_sharing_app.doctype.aircraft.aircraft.get_aircraft_by_name",
    "stop_location_sharing": "location_sharing_app.location_sharing_app.doctype.aircraft.aircraft.stop_location_sharing",
    "start_location_sharing": "location_sharing_app.location_sharing_app.doctype.aircraft.aircraft.start_location_sharing",
    "login_site": "location_sharing_app.location_sharing_app.services.auth_service.login_site",
    "register_site": "location_sharing_app.location_sharing_app.services.auth_service.register_site",
    "create_aircraft": "location_sharing_app.location_sharing_app.doctype.aircraft.aircraft.create_aircraft",
    "update_aircraft": "location_sharing_app.location_sharing_app.doctype.aircraft.aircraft.update_aircraft",
    "bulk_aircraft_log_insert": "location_sharing_app.location_sharing_app.doctype.aircraft_log.aircraft_log.bulk_aircraft_log_insert",
    "disable_user_account": "location_sharing_app.location_sharing_app.services.auth_service.disable_user_account",
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "location_sharing_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["location_sharing_app.utils.before_request"]
# after_request = ["location_sharing_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["location_sharing_app.utils.before_job"]
# after_job = ["location_sharing_app.utils.after_job"]

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
# 	"location_sharing_app.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
