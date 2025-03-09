import frappe
from frappe.auth import LoginManager


@frappe.whitelist(allow_guest=True)
def login_site(*args, **kwargs):
    username = kwargs.get("username")
    password = kwargs.get("password")
    login_manager = LoginManager()
    login_manager.authenticate(username, password)
    user = frappe.get_doc("User", username)
    return {
        "api_key": user.api_key,
        "api_secret_key": user.get_password("api_secret"),
        "full_name": user.full_name,
        "email": user.email,
        "full_name": user.full_name,
    }
