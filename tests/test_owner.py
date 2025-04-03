"""Module provides tests for owner part in fake car insurance data."""

from datetime import datetime
from re import match

from dateutil.relativedelta import relativedelta
from pytest import fail, fixture, mark, raises

from src.owner import generate_address, generate_birthdate, generate_first_name, generate_last_name, generate_phone


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


@fixture
def birthdate_fx(request) -> str:
    """Fixture to generate a birthdate with custom age range.

    :param request: Pytest request object for accessing parameters.
    :return: A string representing the generated birthdate.
    """
    if hasattr(request, "param"):
        minimum_age, maximum_age = request.param
        return generate_birthdate(minimum_age=minimum_age, maximum_age=maximum_age)
    else:
        return generate_birthdate()


@fixture
def age_fx(request) -> str:
    """Fixture that calculates age based on the birthdate_fx fixture."""
    birth_date_str = request.getfixturevalue("birthdate_fx")
    birth_date_obj = datetime.strptime(birth_date_str, "%m/%d/%Y")
    today = datetime.today()
    age = relativedelta(today, birth_date_obj).years
    return age


@fixture
def address_fx() -> str:
    """Fixture to generate a realistic address.

    :return: A string representing the generated address.
    """
    return generate_address()


@fixture
def phone_fx():
    """Fixture to generate a phone number.

    :return: A string representing the generated phone number.
    """
    return generate_phone()


def test_generate_first_name_is_string(first_name_fx):
    """Test that the generate_first_name function returns a string.

    :param first_name_fx: The generated first name from the fixture.
    """
    assert isinstance(first_name_fx, str), f"Expected a string, but got '{type(first_name_fx)}'."


def test_generate_first_name_not_empty(first_name_fx):
    """Test that the generated first name is not an empty string.

    :param first_name_fx: The generated first name from the fixture.
    """
    assert len(first_name_fx) > 0, "First name should not be an empty string."


def test_generate_last_name_is_string(last_name_fx):
    """Test that the generate_last_name function returns a string.

    :param last_name_fx: The generated last name from the fixture.
    """
    assert isinstance(last_name_fx, str), f"Expected a string, but got '{type(last_name_fx)}'"


def test_generate_last_name_not_empty(last_name_fx):
    """Test that the generated last name is not an empty string.

    :param last_name_fx: The generated last name from the fixture.
    """
    assert len(last_name_fx) > 0, "Last name should not be an empty string."


def test_generate_birthdate_format(birthdate_fx):
    """Test that the generate_birthdate function returns a date in the format 'mm/dd/yyyy'.

    :param birthdate_fx: The generated birthdate from the fixture.
    """
    try:
        datetime.strptime(birthdate_fx, "%m/%d/%Y")
    except ValueError:
        fail(f"Birth date '{birthdate_fx}' does not match the format 'mm/dd/yyyy'.")


def test_generate_birthdate_type(birthdate_fx):
    """Test that the generate_birthdate function returns a value of type str.

    :param birthdate_fx: The generated birthdate from the fixture.
    """
    assert isinstance(birthdate_fx, str), f"Expected type 'str', but got '{type(birthdate_fx)}'."


def test_generate_birthdate_default_range(birthdate_fx):
    """Test that the birthdate_fx fixture works with default age range.

    :param birthdate_fx: The generated birthdate from the fixture.
    """
    assert isinstance(birthdate_fx, str), f"Expected type 'str', but got '{type(birthdate_fx)}'."


@mark.parametrize(
    "birthdate_fx",
    [
        (18, 63),
        (20, 30),
        (50, 60),
        (0, 100),
        (18, 18),
        (63, 63),
        (25, 40),
        (1, 10),
        (90, 100),
        (0, 0),
    ],
    indirect=True,
)
def test_generate_birthdate_custom_range(birthdate_fx):
    """Test that the birthdate_fx fixture works with custom age ranges.

    :param birthdate_fx: The generated birthdate from the fixture.
    """
    assert isinstance(birthdate_fx, str), f"Expected type 'str', but got '{type(birthdate_fx)}'."


@mark.parametrize(
    "minimum_age, maximum_age",
    [
        (-1, 63),
        (18, -5),
        (-10, -1),
        (100, 50),
    ],
)
def test_generate_birthdate_negative_value_error(minimum_age, maximum_age):
    """Test that generate_birthdate raises exceptions for invalid age ranges.

    :param minimum_age: The minimum age to test.
    :param maximum_age: The maximum age to test.
    """
    with raises(ValueError):
        generate_birthdate(minimum_age=minimum_age, maximum_age=maximum_age)


@mark.parametrize(
    "minimum_age, maximum_age",
    [
        ("one", 63),
        (18, "sixty-three"),
        (18.5, 63),
        ("two", "fife"),
        (64, "ten"),
        ("sixty-three", 22),
        (18.5, 63),
        (1.5, 6.3),
    ],
)
def test_generate_birthdate_negative_type_error(minimum_age, maximum_age):
    """Test that generate_birthdate raises exceptions for invalid age ranges.

    :param minimum_age: The minimum age to test.
    :param maximum_age: The maximum age to test.
    """
    with raises(TypeError):
        generate_birthdate(minimum_age=minimum_age, maximum_age=maximum_age)


@mark.parametrize(
    "birthdate_fx",
    [
        (0, 0),
        (0, 1),
        (0, 100),
        (1, 10),
        (18, 18),
        (18, 63),
        (20, 30),
        (25, 40),
        (50, 60),
        (63, 63),
        (90, 100),
    ],
    indirect=True,
)
def test_generate_birthdate_age_range(birthdate_fx, age_fx, request):
    """Test that the generated birthdate corresponds to the specified age range.

    :param birthdate_fx: The generated birthdate from the fixture.
    :param age_fx: Calculate age from the fixture.
    """
    minimum_age, maximum_age = request.node.callspec.params["birthdate_fx"]
    assert minimum_age <= age_fx <= maximum_age, (
        f"Generated age '{age_fx}' is not in the range '{minimum_age}-{maximum_age}'. Birth date: '{birthdate_fx}'."
    )


def test_generate_address_type(address_fx):
    """Test that the generate_address function returns a string.

    :param address_fx: The generated address from the fixture.
    """
    assert isinstance(address_fx, str), f"Expected type 'str', but got '{type(address_fx)}'."


def test_generate_address_not_empty(address_fx):
    """Test that the generate_address function returns a non-empty string.

    :param address_fx: The generated address from the fixture.
    """
    assert len(address_fx) > 0, f"Address should not be an empty string. Actual address: '{address_fx}'."


def test_address_contains_house_number(address_fx):
    """Test that the generated address contains a house number.

    :param address_fx: The generated address from the fixture.
    """
    assert any(char.isdigit() for char in address_fx), "Address should contain a house number."


def test_address_contains_zip_code(address_fx):
    """Test that the generated address contains a zip code.

    :param address_fx: The generated address from the fixture.
    """
    assert any(char.isdigit() for char in address_fx.split()[-1]), "Address should contain a zip code."


def test_address_len_zip_code(address_fx):
    """Test that the generated address contains a zip code with len 5.

    :param address_fx: The generated address from the fixture.
    """
    actual_len = len(address_fx.split()[-1])
    assert actual_len == 5, f"Address should contain a zip code with len 5. Actual len: '{actual_len}'."


def test_address_contains_state_code(address_fx):
    """Test that the generated address contains a state as upper two alpha char.

    :param address_fx: The generated address from the fixture.
    """
    assert address_fx.split()[-2].isupper(), "Address should contain a state as upper two alpha char."


def test_generate_phone_type(phone_fx):
    """Test that the generate_phone function returns a string.

    :param phone_fx: The generated phone number from the fixture.
    """
    assert isinstance(phone_fx, str), f"Expected type 'str', but got '{type(phone_fx)}'."


def test_generate_phone_country_code(phone_fx):
    """Test that the generated phone number matches the format +48 xxx xxx xxx.

    :param phone_fx: The generated phone number from the fixture.
    """
    assert phone_fx.startswith("+48"), f"Phone number '{phone_fx}' does not start with '+48'."


def test_generate_phone_len(phone_fx):
    """Test that the generated phone number has 15 char len.

    :param phone_fx: The generated phone number from the fixture.

    """
    assert len(phone_fx) == 15, f"Phone number '{phone_fx}' does not have the correct length."


def test_generate_phone_prefix():
    """Test that the generated phone number has a valid prefix.

    This test generates 20 phone numbers and checks that each prefix is in the allowed list.

    :return: None
    """
    prefixes = ["45", "50", "51", "53", "57", "60", "66", "69", "72", "73", "78", "79", "88"]

    for _ in range(20):
        phone_number = generate_phone()
        generated_prefix = phone_number[4:6]
        assert generated_prefix in prefixes, (
            f"Phone number '{phone_number}' has an invalid prefix '{generated_prefix}'."
        )


def test_generate_phone_format(phone_fx):
    """Test that the generated phone number matches the format +48 xxx xxx xxx using a regular expression."""
    phone_regex = r"^\+48\s\d{3}\s\d{3}\s\d{3}$"
    assert match(phone_regex, phone_fx), f"Phone number '{phone_fx}' does not match the format '+48 xxx xxx xxx'."
