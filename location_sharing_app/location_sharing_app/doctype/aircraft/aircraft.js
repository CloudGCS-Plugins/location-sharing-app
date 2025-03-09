frappe.ui.form.on("Aircraft", {
  refresh: function (frm) {
    console.log(frm.doc);
    if (frm.doc.is_active) {
      frm.add_custom_button("Stop", function () {
        frappe.call({
          method:
            "location_sharing_app.location_sharing_app.doctype.aircraft.aircraft.stop_location_sharing",
          args: {
            aircraft_name: frm.doc.aircraft_name,
          },
          callback: function (r) {
            if (r.message) {
              frm.reload_doc();
            }
          },
        });
      });
    }
  },
});
