app_name = "ballot"
app_title = "Ballot"
app_publisher = "Harsh Tandiya"
app_description = "E-Voting system based on Frappe"
app_email = "harsh@fossunited.org"
app_license = "mit"
# required_apps = []

website_route_rules = [
    {"from_route": "/ballot/<path:app_path>", "to_route": "ballot"},
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ballot/css/ballot.css"
# app_include_js = "/assets/ballot/js/ballot.js"

# include js, css files in header of web template
# web_include_css = "/assets/ballot/css/ballot.css"
# web_include_js = "/assets/ballot/js/ballot.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ballot/public/scss/website"

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
# app_include_icons = "ballot/public/icons.svg"

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
# 	"methods": "ballot.utils.jinja_methods",
# 	"filters": "ballot.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ballot.install.before_install"
# after_install = "ballot.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ballot.uninstall.before_uninstall"
# after_uninstall = "ballot.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "ballot.utils.before_app_install"
# after_app_install = "ballot.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "ballot.utils.before_app_uninstall"
# after_app_uninstall = "ballot.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ballot.notifications.get_notification_config"


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ballot.tasks.all"
# 	],
# 	"daily": [
# 		"ballot.tasks.daily"
# 	],
# 	"hourly": [
# 		"ballot.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ballot.tasks.weekly"
# 	],
# 	"monthly": [
# 		"ballot.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "ballot.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ballot.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ballot.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["ballot.utils.before_request"]
# after_request = ["ballot.utils.after_request"]

# Job Events
# ----------
# before_job = ["ballot.utils.before_job"]
# after_job = ["ballot.utils.after_job"]

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
# 	"ballot.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
