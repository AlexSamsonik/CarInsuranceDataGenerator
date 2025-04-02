"""Module provides functions to generate data for owner part in fake car insurance data."""

from src.singleton import FakerSingleton

fake = FakerSingleton.get_instance()


def generate_first_name() -> str:
    """Generate a realistic first name.

    :return: A string representing a first name.
    """
    return fake.first_name()


def generate_last_name() -> str:
    """Generate a realistic last name.

    :return: A string representing a last name.
    """
    return fake.last_name()


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
    birth_date = fake.date_of_birth(minimum_age=minimum_age, maximum_age=maximum_age)

    # Convert the date to the 'mm/dd/yyyy' string format
    return birth_date.strftime("%m/%d/%Y")


def generate_address() -> str:
    """Generate a realistic address.

    :return: A string representing an address.
    """
    return fake.address().replace("\n", ", ")


def generate_phone() -> str:
    """Generate a phone number in the format +48 xxx xxx xxx.

    The prefix (first two digits) is chosen from a predefined list, and the rest
    of the digits are generated randomly.

    :return: A string representing a phone number.
    """
    prefixes = ["45", "50", "51", "53", "57", "60", "66", "69", "72", "73", "78", "79", "88"]

    prefix = fake.random_element(prefixes)
    random_digit = fake.random_digit()
    middle_digits = fake.random_number(digits=3, fix_len=True)
    last_digits = fake.random_number(digits=3, fix_len=True)

    phone_number = f"+48 {prefix}{random_digit} {middle_digits} {last_digits}"
    return phone_number
