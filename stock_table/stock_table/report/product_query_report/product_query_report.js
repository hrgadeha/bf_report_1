// Copyright (c) 2016, Hardik Gadesha and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Product Query Report"] = {
	"filters": [
		{
		    "fieldname": "item",
	            "label": __("Select Item"),
	            "fieldtype": "Link",
		    "options": "Item"
		}
	]
}
