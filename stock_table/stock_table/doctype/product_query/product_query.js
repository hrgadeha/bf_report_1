// Copyright (c) 2019, Hardik Gadesha and contributors
// For license information, please see license.txt

frappe.ui.form.on('Product Query', {
	refresh: function(frm) {

	}
});

frappe.ui.form.on("Product Query", {
  item_code: function(frm) {
//	cur_frm.refresh();
//	cur_frm.refresh_fields();
	
	if(frm.doc.item_code){
	
    frappe.call({
    "method": "stock_table.stock_table.doctype.product_query.product_query.getProductQuery",
args: {
doctype: "Product Query",
item_code: frm.doc.item_code
},
callback:function(r){
	var len=r.message.length;
	for (var i=0;i<len;i++){
		frm.set_value("item_name",r.message[i][0]);
		frm.set_value("discription",r.message[i][1]);
		frm.set_value("uom",r.message[i][2]);
		frm.set_value("sales_price",r.message[i][3]);
		frm.set_value("wholesale_price",r.message[i][4]);
		frm.set_value("valuation_rate",r.message[i][5]);
		frm.set_value("last_purchase_price",r.message[i][6]);
		frm.set_value("sn_stock",r.message[i][7]);
		frm.set_value("ah_stock",r.message[i][8]);
		frm.set_value("mn_stock",r.message[i][9]);
		frm.set_value("sz_stock",r.message[i][10]);
		frm.set_value("sh_stock",r.message[i][11]);
		frm.set_value("total_stock",r.message[i][12]);
		frm.set_value("stock_in_transit",r.message[i][13]);
	}
		cur_frm.refresh();
	}
    });
}
}
});

frappe.ui.form.on("Product Query", "onload", function(frm){
    frm.add_custom_button("Open Sales Invoice", function(){
	window.open('http://babefakhri.ribox.me/desk#Form/Sales%20Invoice/New%20Sales%20Invoice%201');
	});
});
