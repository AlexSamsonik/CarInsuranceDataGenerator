"""Module provides tests for car part in fake car insurance data."""

from pytest import fixture

from src.car import generate_vin


@fixture
def vin_fx():
    """Fixture to generate a random VIN.

    :return: A string representing a VIN.
    """
    return generate_vin()


def test_vin_length(vin_fx):
    """Test to ensure the generated VIN has a length of 17 characters.

    :param vin_fx: The generated VIN from the fixture.
    """
    assert len(vin_fx) == 17, f"VIN length should be 17, but got '{len(vin_fx)}'."


def test_vin_type(vin_fx):
    """Test to ensure the generated VIN is a string.

    :param vin_fx: The generated VIN from the fixture.
    """
    assert isinstance(vin_fx, str), f"VIN should be a string, but got '{type(vin_fx)}'."


def test_vin_allowed_chars(vin_fx):
    """Test to ensure the generated VIN contains only allowed characters.

    Allowed characters are uppercase letters (excluding I, O, Q) and digits.

    :param vin_fx: The generated VIN from the fixture.
    """
    allowed_chars = set("ABCDEFGHJKLMNPRSTUVWXYZ0123456789")
    for char in vin_fx:
        assert char in allowed_chars, f"VIN contains invalid character: '{char}'."
