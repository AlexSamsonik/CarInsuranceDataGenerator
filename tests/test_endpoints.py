"""The module with unit tests."""

from fastapi.testclient import TestClient
from pydantic import ValidationError
from pytest import fail, fixture

from main import app
from tests.test_generate_fake_data import FakeDataModel

client = TestClient(app)


@fixture
def root_response():
    """Fixture to send a GET request to the root endpoint and return the response.

    :return: Response object from the root endpoint.
    """
    return client.get("/")


@fixture
def generate_response():
    """Fixture to send a GET request to the generate endpoint and return the response.

    :return: Response object from the root endpoint.
    """
    return client.get("/generate")


def test_read_root_status_code(root_response):
    """Test that the root endpoint returns a 200 status code."""
    assert root_response.status_code == 200


def test_read_root_response_content(root_response):
    """Test that the root endpoint returns the correct JSON response."""
    assert root_response.json() == {"message": "Welcome to the Car Insurance Generator API!"}


def test_read_generate_status_code(generate_response):
    """Test that the generate endpoint returns a 200 status code."""
    assert generate_response.status_code == 200


def test_read_generate_response_content(generate_response):
    """Test that the generate endpoint returns the correct JSON response."""
    try:
        FakeDataModel(**generate_response.json())
    except ValidationError as e:
        fail(f"Pydantic validation failed: {e}")
