"""Module provides function to generate fake car insurance data."""

from src.policy_number import generate_policy_number


def generate_fake_data():
    """Generate fake car insurance data.

    :return: A dictionary containing fake car insurance data.
    """
    return {
        "policy_number": generate_policy_number(),
        "owner": {
            "first_name": "",
            "last_name": "fake.last_name()",
            "birth_date": "",
            "address": "",
            "phone": "",
        },
        "car": {
            "vin": "",
        },
        "insurance": {
            "start_date": "",
            "end_date": "",
        },
    }
