"""Module provides tests for testing generate_policy_number() function."""

from re import match

from pytest import fixture

from src.policy_number import generate_policy_number


@fixture
def policy_number_fx():
    """Fixture to generate a policy number.

    :return: A string representing the generated policy number.
    """
    return generate_policy_number()


def test_generate_policy_number_format(policy_number_fx):
    """Test that the generated policy number matches the required format.

    :param policy_number_fx: The generated policy number from the fixture.
    """
    pattern = r"^PL\d{9}[A-Z]{2}$"
    assert match(pattern, policy_number_fx), (
        f"Policy number format mismatch. "
        f"Actual: '{policy_number_fx}', Expected: format 'PL' + 9 digits + 2 uppercase letters."
    )


def test_generate_policy_number_length(policy_number_fx):
    """Test that the generated policy number has a length of 13 characters.

    :param policy_number_fx: The generated policy number from the fixture.
    """
    expected_length = 13
    actual_length = len(policy_number_fx)
    assert actual_length == expected_length, (
        f"Policy number length mismatch. "
        f"Actual: {actual_length}, Expected: {expected_length}. "
        f"Policy number: '{policy_number_fx}'."
    )


def test_generate_policy_number_prefix(policy_number_fx):
    """Test that the generated policy number starts with the prefix 'PL'.

    :param policy_number_fx: The generated policy number from the fixture.
    """
    assert policy_number_fx.startswith("PL"), (
        f"Policy number prefix mismatch. Actual: '{policy_number_fx[:2]}', Expected: 'PL'."
    )


def test_generate_policy_number_last_two_characters(policy_number_fx):
    """Test that the last two characters of the policy number are uppercase letters.

    :param policy_number_fx: The generated policy number from the fixture.
    """
    last_two_characters = policy_number_fx[-2:]
    assert last_two_characters.isalpha() and last_two_characters.isupper(), (
        f"Policy number last two characters mismatch. Actual: '{last_two_characters}', Expected: two uppercase letters."
    )


def test_generate_policy_number_middle_digits(policy_number_fx):
    """Test that the middle part of the policy number consists of 9 digits.

    :param policy_number_fx: The generated policy number from the fixture.
    """
    middle_digits = policy_number_fx[2:-2]
    assert middle_digits.isdigit() and len(middle_digits) == 9, (
        f"Policy number middle digits mismatch. Actual: '{middle_digits}', Expected: 9 digits."
    )
