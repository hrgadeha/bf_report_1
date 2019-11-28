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
	return [_("Voucher Type") + ":Data:120",_("Voucher Number") + ":Data:120",_("Party Type") + ":Data:120",_("Party Name") + ":Data:120",_("Payment Entry") + ":Data:150",_("Date") + ":Date:100",_("Total Amount") + ":Float:100",_("Outstanding Amount") + ":Float:100",_("Allocated Amount") + ":Float:100"]

def get_data(filters):
	if filters.get("customer"):
		customer = filters.get("customer")	
		payment_data = frappe.db.sql("""select per.reference_doctype,per.reference_name,pe.party_type, pe.party_name,pe.name,pe.posting_date, per.total_amount, per.outstanding_amount,per.allocated_amount from `tabPayment Entry` pe, `tabPayment Entry Reference` per where pe.name = per.parent and party_name = '{0}' ORDER BY pe.name;
; """.format(customer), as_list=1)
		return payment_data
