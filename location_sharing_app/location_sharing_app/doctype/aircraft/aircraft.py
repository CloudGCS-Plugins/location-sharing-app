import frappe
import json
from frappe.model.document import Document

class Aircraft(Document):

    def validate(self):
        aircrafts = get_user_aircrafts()
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
        self.aircraft_owner = user.email


def has_role(user_data, param):
    for role in user_data.get("roles"):
        if role["role"] == param:
            return True
    return False

def get_aircraft_query(user):
    user_data = frappe.get_doc("User", user).as_dict()
    if has_role(user_data, "System Manager"):
        return ""

    return f"""(`tabAircraft`.aircraft_owner = '{user}')"""


def get_current_user_doc():
    user = frappe.session.user
    user = frappe.get_doc("User", user)
    return user


def get_aircraft_doc_by_name(aircraft_name):
    aircraft_owner = get_current_user_doc()
    aircrafts = frappe.get_all(
        "Aircraft",
        filters={"aircraft_name": aircraft_name, "aircraft_owner": aircraft_owner.email},
        fields=["name", "aircraft_name", "is_active", "last_coordinate"],
    )
    if not aircrafts:
        return None
    doc = frappe.get_doc("Aircraft", aircrafts[0].name)
    return doc


def get_user_aircrafts():
    aircraft_owner = get_current_user_doc()
    aircrafts = frappe.get_all(
        "Aircraft",
        filters={"aircraft_owner": aircraft_owner.email},
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
    if not aircraft:
        frappe.throw("Aircraft not found")
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
    aircraft_owner = get_current_user_doc()
    aircraft = frappe.get_all(
        "Aircraft",
        filters={"aircraft_name": aircraft_name, "aircraft_owner": aircraft_owner.email},
        fields=["name", "aircraft_name", "is_active", "last_coordinate"],
    )
    if not aircraft:
        frappe.throw("Aircraft not found")
    return aircraft
