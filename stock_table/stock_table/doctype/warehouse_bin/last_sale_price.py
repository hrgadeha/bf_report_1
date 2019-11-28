from __future__ import unicode_literals
import frappe, erpnext
import frappe.defaults
from frappe.utils import cint, flt, fmt_money
from frappe import _, msgprint, throw

@frappe.whitelist()
def get_last_sales_price(item,customer):
        lst_rate = frappe.db.sql("""select rate from `tabSales Invoice Item`,`tabSales Invoice`
                where `tabSales Invoice`.docstatus = 1 and `tabSales Invoice Item`.parent = `tabSales Invoice`.name and item_code = %s 
		and customer = %s order by `tabSales Invoice`.creation desc limit 1;""",(item,customer))
        return lst_rate[0][0] if lst_rate else 0.0
