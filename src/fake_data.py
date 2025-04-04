"""Module provides function to generate fake car insurance data."""

from src.car import generate_vin
from src.insurance import generate_end_date, generate_start_date
from src.owner import generate_address, generate_birthdate, generate_first_name, generate_last_name, generate_phone
from src.policy_number import generate_policy_number


def generate_fake_data():
    """Generate fake car insurance data.

    :return: A dictionary containing fake car insurance data.
    """
    return {
        "policy_number": generate_policy_number(),
        "owner": {
            "first_name": generate_first_name(),
            "last_name": generate_last_name(),
            "birth_date": generate_birthdate(),
            "address": generate_address(),
            "phone": generate_phone(),
        },
        "car": {
            "vin": generate_vin(),
        },
        "insurance": {
            "start_date": generate_start_date(),
            "end_date": generate_end_date(),
        },
    }
