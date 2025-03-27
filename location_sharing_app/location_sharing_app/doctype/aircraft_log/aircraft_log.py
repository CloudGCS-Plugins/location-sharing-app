# Copyright (c) 2025, CloudGCS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AircraftLog(Document):
    pass


@frappe.whitelist()
def bulk_aircraft_log_insert(*args, **kwargs):
    try:
        model = kwargs
        aircraft_logs = model.get("aircraft_logs")
        for aircraft_log in aircraft_logs:
            location = {
                "type": "Feature",
                "properties": {"altitude": aircraft_log.get("altitude")},
                "geometry": {
                    "coordinates": [
                        aircraft_log.get("longitude"),
                        aircraft_log.get("latitude"),
                    ],
                    "type": "Point",
                },
            }
            create_aircraft_log(
                aircraft_log.get("name"), location, aircraft_log.get("timestamp")
            )
        return True
    except Exception as e:
        return False
