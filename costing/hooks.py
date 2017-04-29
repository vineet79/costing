# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "costing"
app_title = "Costing"
app_publisher = "Mayur"
app_description = "Costing Module"
app_icon = "octicon octicon-repo"
app_color = "blue"
app_email = "mayur@mittalclothing.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/costing/css/costing.css"
# app_include_js = "/assets/costing/js/costing.js"

# include js, css files in header of web template
# web_include_css = "/assets/costing/css/costing.css"
# web_include_js = "/assets/costing/js/costing.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "costing.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "costing.install.before_install"
# after_install = "costing.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "costing.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"costing.tasks.all"
# 	],
# 	"daily": [
# 		"costing.tasks.daily"
# 	],
# 	"hourly": [
# 		"costing.tasks.hourly"
# 	],
# 	"weekly": [
# 		"costing.tasks.weekly"
# 	]
# 	"monthly": [
# 		"costing.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "costing.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "costing.event.get_events"
# }

