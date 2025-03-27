# Copyright (c) 2025, CloudGCS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ContactUs(Document):
	pass


@frappe.whitelist(allow_guest=True)
def send_message(full_name, email, subject, message):
	contact_us = frappe.new_doc('Contact Us')
	contact_us.full_name = full_name
	contact_us.email = email
	contact_us.subject = subject
	contact_us.message = message
	contact_us.insert(ignore_permissions=True)
	frappe.db.commit()
	return contact_us