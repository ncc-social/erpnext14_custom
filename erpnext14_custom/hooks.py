from . import __version__ as app_version

app_name = "erpnext14_custom"
app_title = "Erpnext14 Custom"
app_publisher = "NCC"
app_description = "Customisations for ERPNext 14"
app_email = "social@ncc.gov.gh"
app_license = "MIT"


fixtures = [
    {"dt": "Property Setter", "filters": [
        [
            "doc_type", "in", [
                "Employee",
                "Leave Application",
                "Leave Type",
                "Training Event",
                "Vehicle",
                "Notification",
                "Print Format",
                "Issue"
            ]
        ]
    ]},
    {"dt": "Custom Field", "filters": [
        [
            "fieldname", "in", [
                "assumption_of_duty",
                "acceptance_date",
                "reports_to_name",
                "age",
                "employee_name",
                "year",
                "type",
                "tyre_type",
                "vehicle_image",
                "column_break_7",
                "section_break_4",
                "department",
                "employee_number",
                "staff_id",
                "branch",
                "ssnit",
                "workflow_state",
                "additional_cell_number",
                "status",
                "ghanacard_details",
                "personal_id_number",
                "document_number",
                "column_break_83",
                "ghanacard_date_of_issuance",
                "ghanacard_date_of_expiry",
                "employee"
            ]
        ]
    ]},
    {"dt": "Client Script", "filters": [
        [
            "name", "in", [
                "Employee-Form",
                "Vehicle-Form",
                "Leave Application-Form",
                "Leave Application-List",
                "Send SMS for Leave Application"

            ]
        ]
    ]},
    {"dt": "Server Script", "filters": [
        [
            "name", "in", [
                "Full Name of User"
            ]
        ]
    ]}
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/erpnext14_custom/css/erpnext14_custom.css"
# app_include_js = "/assets/erpnext14_custom/js/erpnext14_custom.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext14_custom/css/erpnext14_custom.css"
# web_include_js = "/assets/erpnext14_custom/js/erpnext14_custom.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "erpnext14_custom/public/scss/website"

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

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "erpnext14_custom.utils.jinja_methods",
#	"filters": "erpnext14_custom.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "erpnext14_custom.install.before_install"
# after_install = "erpnext14_custom.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "erpnext14_custom.uninstall.before_uninstall"
# after_uninstall = "erpnext14_custom.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext14_custom.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
	"Leave Application": {
		"on_submit": "erpnext14_custom.server_scripts.leave_application.after_approval"
	}
}

# Scheduled Tasks
# ---------------

scheduler_events = {
#	"all": [
#		"erpnext14_custom.tasks.all"
#	],
	"daily": [
		"erpnext14_custom.birthday_reminder.send_birthday_reminders"
	],
#	"hourly": [
#		"erpnext14_custom.tasks.hourly"
#	],
#	"weekly": [
#		"erpnext14_custom.tasks.weekly"
#	],
#	"monthly": [
#		"erpnext14_custom.tasks.monthly"
#	],
}

# Testing
# -------

# before_tests = "erpnext14_custom.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "erpnext14_custom.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "erpnext14_custom.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"erpnext14_custom.auth.validate"
# ]
