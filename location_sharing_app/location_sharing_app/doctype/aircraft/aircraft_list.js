frappe.listview_settings["Aircraft"] = {
  onload: function (listview) {
    // frappe.call({
    //   method: "frappe.client.get_value",
    //   args: {
    //     doctype: "User",
    //     filters: { name: frappe.session.user },
    //     fieldname: "email",
    //   },
    //   callback: function (response) {
    //     if (response.message) {
    //       let user_email = response.message.email;
    //       listview.filter_area.add([
    //         ["Aircraft", "user_email", "=", user_email],
    //       ]);
    //       listview.refresh();
    //     }
    //   },
    // });
  },
};
