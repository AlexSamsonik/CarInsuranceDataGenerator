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


def generate_birthdate(minimum_age: int = 18, maximum_age: int = 63) -> str:
    """Generate a birthdate for a person aged between 18 (default) and 63 (default) years.

    :return: A string representing the birth ate in the format 'mm/dd/yyyy'.
    """
    birth_date = Faker().date_of_birth(minimum_age=minimum_age, maximum_age=maximum_age)
    return birth_date.strftime("%m/%d/%Y")
