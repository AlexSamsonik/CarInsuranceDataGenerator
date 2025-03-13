"""Module provides functions to generate data for owner part in fake car insurance data."""

from faker import Faker


def generate_first_name() -> str:
    """Generate a realistic first name.

    :return: A string representing a first name.
    """
    return Faker().first_name()


def generate_last_name() -> str:
    """Generate a realistic last name.

    :return: A string representing a last name.
    """
    return Faker().last_name()
