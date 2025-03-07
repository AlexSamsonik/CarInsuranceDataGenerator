"""The module with unit tests."""

from fastapi.testclient import TestClient
from pytest import fixture

from src.main import app

client = TestClient(app)


@fixture
def root_response():
    """Fixture to send a GET request to the root endpoint and return the response.

    :return: Response object from the root endpoint.
    """
    return client.get("/")


def test_read_root_status_code(root_response):
    """Test that the root endpoint returns a 200 status code."""
    assert root_response.status_code == 200


def test_read_root_response_content(root_response):
    """Test that the root endpoint returns the correct JSON response."""
    assert root_response.json() == {"message": "Welcome to the Car Insurance Generator API!"}
