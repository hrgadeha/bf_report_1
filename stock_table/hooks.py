# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "stock_table"
app_title = "Stock Table"
app_publisher = "Hardik Gadesha"
app_description = "App to show stock in all warehouse in sales invoice table"
app_icon = "octicon octicon-file-directory"
app_color = "LIGHTSALMON"
app_email = "hardikgadesha"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/stock_table/css/stock_table.css"
# app_include_js = "/assets/stock_table/js/stock_table.js"

# include js, css files in header of web template
# web_include_css = "/assets/stock_table/css/stock_table.css"
# web_include_js = "/assets/stock_table/js/stock_table.js"

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

# Website user home page (by function)
# get_website_user_home_page = "stock_table.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "stock_table.install.before_install"
# after_install = "stock_table.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "stock_table.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Invoice": {
		"after_insert": "stock_table.stock_table.doctype.product_query.product_query.updateJV",
		"on_cancel": "stock_table.stock_table.doctype.product_query.product_query.cancelSI"
	},
	"Delivery Note": {
		"on_submit": "stock_table.stock_table.doctype.stock_table.stock_table.updateSITEM",
	}
}

#scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"stock_table.tasks.all"
# 	],
# 	"daily": [
# 		"stock_table.tasks.daily"
# 	],
# 	"hourly": [
# 		"stock_table.tasks.hourly"
# 	],
# 	"weekly": [
# 		"stock_table.tasks.weekly"
# 	]
# 	"monthly": [
# 		"stock_table.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "stock_table.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "stock_table.event.get_events"
# }

