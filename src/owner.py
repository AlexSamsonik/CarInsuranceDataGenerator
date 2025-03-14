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
    """Generate a birthdate for a person within the specified age range.

    :param minimum_age: The minimum age of the person (default is 18).
    :param maximum_age: The maximum age of the person (default is 63).
    :return: A string representing the birthdate in the format 'mm/dd/yyyy'.
    """
    # Ensure that minimum_age and maximum_age are integers
    if not isinstance(minimum_age, int) or not isinstance(maximum_age, int):
        raise TypeError("Both minimum_age and maximum_age must be integers.")

    # Ensure that the values are non-negative
    if minimum_age < 0 or maximum_age < 0:
        raise ValueError("Ages must be non-negative integers.")

    # Ensure that minimum_age is not greater than maximum_age
    if minimum_age > maximum_age:
        raise ValueError("Minimum age cannot be greater than maximum age.")

    # Generate a random birthdate within the specified age range
    birth_date = Faker().date_of_birth(minimum_age=minimum_age, maximum_age=maximum_age)

    # Convert the date to the 'mm/dd/yyyy' string format
    return birth_date.strftime("%m/%d/%Y")
