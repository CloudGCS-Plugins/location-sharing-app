import frappe
import json
from frappe.model.document import Document
import requests

class Aircraft(Document):

    def validate(self):
        aircrafts = get_user_aircrafts(self.aircraft_name, self.user_email)
        if aircrafts:
            for aircraft in aircrafts:
                if aircraft.is_active and self.is_active and aircraft.name != self.name:
                    frappe.throw("Another Aircraft is already sharing location")
                trimmed_aircraft_name = aircraft.aircraft_name.strip().lower()
                trimmed_self_aircraft_name = self.aircraft_name.strip().lower()
                if (
                    trimmed_aircraft_name == trimmed_self_aircraft_name
                    and aircraft.name != self.name
                ):
                    frappe.throw("Aircraft with same name already exists")
        pass

    def before_save(self):
        user = get_current_user_doc()
        self.user_email = user.email


def get_aircraft_query(user):
    # if not user or user == "Administrator":
    #     return ""

    # This ensures users only see Aircraft they created
    return f"""(`tabAircraft`.owner = '{user}')"""


def get_current_user_doc():
    user = frappe.session.user
    user = frappe.get_doc("User", user)
    return user


def get_aircraft_doc_by_name(aircraft_name):
    user = get_current_user_doc()
    user_email = user.email
    aircrafts = frappe.get_all(
        "Aircraft",
        filters={"aircraft_name": aircraft_name, "user_email": user_email},
        fields=["name", "aircraft_name", "is_active", "last_coordinate"],
    )
    if not aircrafts:
        return None
    doc = frappe.get_doc("Aircraft", aircrafts[0].name)
    return doc


def get_user_aircrafts(aircraft_name, user_email):
    user = get_current_user_doc()
    user_email = user.email
    aircrafts = frappe.get_all(
        "Aircraft",
        filters={"user_email": user_email},
        fields=["name", "aircraft_name", "is_active", "last_coordinate"],
    )
    return aircrafts


@frappe.whitelist()
def start_location_sharing(*args, **kwargs):
    model = kwargs
    aircraft_name = model.get("aircraft_name")
    aircraft = get_aircraft_doc_by_name(aircraft_name)
    if not aircraft:
        frappe.throw("Aircraft not found")
    aircraft.is_active = 1
    location = {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "coordinates": [model.get("longitude"), model.get("latitude")],
            "type": "Point",
        },
    }
    aircraft.last_coordinate = json.dumps(location)
    try:
        aircraft.save()
        return True
    except Exception as e:
        print(e)
        return False


@frappe.whitelist()
def stop_location_sharing(*args, **kwargs):
    model = kwargs
    aircraft_name = model.get("aircraft_name")
    aircraft = get_aircraft_doc_by_name(aircraft_name)
    aircraft.is_active = 0
    try:
        aircraft.save()
        return True
    except Exception as e:
        print(e)
        return False


@frappe.whitelist()
def get_aircrafts(*args, **kwargs):
    return get_user_aircrafts()


@frappe.whitelist()
def get_aircraft_by_name(*args, **kwargs):
    model = kwargs
    aircraft_name = model.get("aircraft_name")
    user = get_current_user_doc()
    user_email = user.email
    aircraft = frappe.get_all(
        "Aircraft",
        filters={"aircraft_name": aircraft_name, "user_email": user_email},
        fields=["name", "aircraft_name", "is_active", "last_coordinate"],
    )
    if not aircraft:
        frappe.throw("Aircraft not found")
    return aircraft


@frappe.whitelist()
def test():
    frappe_server_url = "http://localhost:8000"
    endpoint = "/api/method/start_location_sharing"
    payload = {"aircraft_name": "Test", "latitude": 53, "longitude": 13}
    headers = {
        "Content-Type": "application/json",
        "Authorization": "token 6b9b7359220e4b7:b51075e49724a58",
    }
    response = requests.post(
        f"{frappe_server_url}{endpoint}", headers=headers, json=payload
    )
    if response.status_code == 200:
        print(response.json())
    else:
        print("Error")
    pass
