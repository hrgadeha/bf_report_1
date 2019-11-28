# Copyright (c) 2013, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns = get_column()
	data = get_data(filters)
	return columns,data

def get_column():
	return [_("Invoice Number") + ":Data:150",_("Invoice Date") + ":Date:120",_("Item Code") + ":Data:120",_("Item Name") + ":Data:300",_("Qty") + ":Float:100",_("Selling Rate") + ":Currency:180",_("UOM") + ":Data:100"]

def get_data(filters):
	if filters.get("customer"):
		customer = filters.get("customer")
		sales_data = frappe.db.sql("""select sinv.name,sinv.posting_date,sit.item_code,sit.item_name,sit.qty,sit.rate,sit.uom from `tabSales Invoice` sinv, `tabSales Invoice Item` sit where sinv.name = sit.parent and sinv.customer = '{0}';
; """.format(customer), as_list=1)
		return sales_data
