"""Module provides tests for owner part in fake car insurance data."""

from pytest import fixture

from src.owner import generate_first_name, generate_last_name


@fixture
def first_name_fx() -> str:
    """Fixture to generate a first name.

    :return: A string representing a first name.
    """
    return generate_first_name()


@fixture
def last_name_fx() -> str:
    """Fixture to generate a last name.

    :return: A string representing a last name.
    """
    return generate_last_name()


def test_generate_first_name_is_string(first_name_fx):
    """Test that the generate_first_name function returns a string.

    :param first_name_fx: The generated first name from the fixture.
    """
    assert isinstance(first_name_fx, str), f"Expected a string, but got {type(first_name_fx)}"


def test_generate_first_name_not_empty(first_name_fx):
    """Test that the generated first name is not an empty string.

    :param first_name_fx: The generated first name from the fixture.
    """
    assert len(first_name_fx) > 0, "First name should not be an empty string"


def test_generate_last_name_is_string(last_name_fx):
    """Test that the generate_last_name function returns a string.

    :param last_name_fx: The generated last name from the fixture.
    """
    assert isinstance(last_name_fx, str), f"Expected a string, but got {type(last_name_fx)}"


def test_generate_last_name_not_empty(last_name_fx):
    """Test that the generated last name is not an empty string.

    :param last_name_fx: The generated last name from the fixture.
    """
    assert len(last_name_fx) > 0, "Last name should not be an empty string"
