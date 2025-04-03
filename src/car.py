"""Module provides functions to generate data for car part in fake car insurance data."""

from string import ascii_uppercase, digits

from src.singleton import FakerSingleton

fake = FakerSingleton.get_instance()


def generate_vin():
    """Generates a random Vehicle Identification Number (VIN).

    A VIN is a 17-character string that includes uppercase letters (excluding I, O, Q)
    and digits.

    :return: A string representing a VIN.
    """
    # VIN consists of 17 characters
    vin_length = 17

    # Allowed characters for VIN (excluding I, O, Q)
    allowed_chars = ascii_uppercase.replace("I", "").replace("O", "").replace("Q", "") + digits

    # Generate random VIN
    vin = "".join(fake.random_element(allowed_chars) for _ in range(vin_length))

    return vin
