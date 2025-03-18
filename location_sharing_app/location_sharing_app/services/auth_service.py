import frappe
from frappe.auth import LoginManager
from frappe.core.doctype.user.user import generate_keys, sign_up
from frappe.utils.password import update_password


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


@frappe.whitelist(allow_guest=True)
def register_site(*args, **kwargs):
    model = kwargs
    email = model.get("email")
    first_name = model.get("full_name")
    password = model.get("password")

    try:

        sign_up(email, first_name, "/welcome")
        frappe.db.commit()

        user = frappe.get_doc("User", email)
        user.search_bar = 0
        update_password(user.name, password)
        api_secret = frappe.generate_hash(length=15)
        # if api key is not set generate api key
        if not user.api_key:
            api_key = frappe.generate_hash(length=15)
            user.api_key = api_key
        user.api_secret = api_secret
        user.save(ignore_permissions=True)
        frappe.db.commit()

        return {
            "api_key": user.api_key,
            "api_secret_key": user.get_password("api_secret"),
            "full_name": user.full_name,
            "email": user.email,
        }
    except Exception as e:
        return {"error": "User could not be created. Please try again."}
