"""This module provide functions to manipulate with policy number."""

from src.singleton import FakerSingleton

fake = FakerSingleton.get_instance()


def generate_policy_number():
    """Generate a policy number.

    The format is 'PL' + 9 random digits + 2 random uppercase letters.

    :return: A string representing the policy number.
    """
    random_digits = fake.random_number(digits=9, fix_len=True)
    random_letters = fake.random_uppercase_letter() + fake.random_uppercase_letter()
    policy_number = f"PL{random_digits}{random_letters}"
    return policy_number
