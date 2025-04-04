"""Module provides tests for generate fake data."""

from pydantic import BaseModel, ValidationError
from pytest import fail, fixture

from src.fake_data import generate_fake_data


class OwnerModel(BaseModel):
    """Pydantic model for the owner of the car.

    :param first_name: The first name of the owner.
    :param last_name: The last name of the owner.
    :param birth_date: The birthdate of the owner in MM/DD/YYYY format.
    :param address: The address of the owner.
    :param phone: The phone number of the owner.
    """

    first_name: str
    last_name: str
    birth_date: str
    address: str
    phone: str


class CarModel(BaseModel):
    """Pydantic model for the car.

    :param vin: The Vehicle Identification Number (VIN) of the car.
    """

    vin: str


class InsuranceModel(BaseModel):
    """Pydantic model for the insurance details.

    :param start_date: The start date of the insurance in MM/DD/YYYY format.
    :param end_date: The end date of the insurance in MM/DD/YYYY format.
    """

    start_date: str
    end_date: str


class FakeDataModel(BaseModel):
    """Pydantic model for the fake car insurance data.

    :param policy_number: The policy number of the insurance.
    :param owner: The owner details as an instance of OwnerModel.
    :param car: The car details as an instance of CarModel.
    :param insurance: The insurance details as an instance of InsuranceModel.
    """

    policy_number: str
    owner: OwnerModel
    car: CarModel
    insurance: InsuranceModel


@fixture
def fake_data() -> dict:
    """Fixture to generate fake car insurance data.

    :return: A dictionary containing fake car insurance data.
    """
    return generate_fake_data()


def test_generate_fake_data_schema(fake_data):
    """Test the generate_fake_data function to ensure it returns data matching the defined pydantic model.

    :param fake_data: Fixture providing fake car insurance data.
    """
    try:
        FakeDataModel(**fake_data)
    except ValidationError as e:
        fail(f"Pydantic validation failed: {e}")
