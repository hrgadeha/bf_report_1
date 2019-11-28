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
	return [_("Item Code") + ":Link/Item:120",_("Item Name") + ":Data:180",_("Discription") + ":Data:180",_("UOM") + ":Data:50",_("Sales Price") + ":Currency:100",_("Wholesale Price") + ":Currency:100",_("Valuation Rate") + ":Currency:100",_("Last Purchase Price") + ":Currency:100",_("SN Stock") + ":Float:70",_("AH Stock") + ":Float:75",_("MN Stock") + ":Float:75",_("SZ Stock") + ":Float:70",_("SH Stock") + ":Float:70",_("Total Stock") + ":Float:70",_("Stock in Transit") + ":Float:100"]

def get_data(filters):
	if filters.get("item"):
		item = filters.get("item")	
		item_data = frappe.db.sql("""select item_code, item_name, description,stock_uom, standard_rate,wholesale_rate,
(select valuation_rate
from `tabStock Ledger Entry` 
where item_code =  '{0}' and is_cancelled='No' 
order by posting_date desc, posting_time desc, 
name desc limit 1),
(select rate from `tabPurchase Invoice Item`,`tabPurchase Invoice` 
where `tabPurchase Invoice Item`.parent = `tabPurchase Invoice`.name and item_code = '{0}'  
order by `tabPurchase Invoice`.creation desc limit 1),
(select actual_qty from `tabBin` where item_code =  '{0}' and warehouse = 'SN - B'),
(select actual_qty from `tabBin` where item_code =  '{0}' and warehouse = 'AH - B'),
(select actual_qty from `tabBin` where item_code =  '{0}' and warehouse = 'MN - B'),
(select actual_qty from `tabBin` where item_code =  '{0}' and warehouse = 'SZ - B'),
(select actual_qty from `tabBin` where item_code =  '{0}' and warehouse = 'SH - B'),
(select sum(actual_qty) from `tabBin` where item_code =  '{0}' and (warehouse = 'SN - B' or warehouse = 'SZ - B' or warehouse = 'AH - B' or warehouse = 'MN - B' or warehouse = 'SH - B')),
(select ordered_qty from `tabBin` where item_code =  '{0}' order by name limit 1)
from `tabItem` where  item_code =  '{0}'; """.format(item), as_list=1)
		return item_data
