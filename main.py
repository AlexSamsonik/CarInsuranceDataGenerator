"""This module defines the main entry point for the Car Insurance Data Generator API.

The API provides endpoints for generating fictional car insurance data, including
details about the policy, car, and owner. It is built using FastAPI and is designed
to be lightweight and easy to use for testing and prototyping purposes.
"""

from fastapi import FastAPI

from src.fake_data import generate_fake_data

app = FastAPI()


@app.get("/")
def read_root():
    """Root endpoint of the API.

    :return: A welcome message indicating that the API is running.
    """
    return {"message": "Welcome to the Car Insurance Generator API!"}


@app.get("/generate")
def generate_data():
    """Generate fake car insurance data.

    This endpoint generates a single set of fictional car insurance data,
    including details about the policy, owner, and car. The data is returned
    in JSON format.

    :return: A dictionary containing fake car insurance data.
    """
    return generate_fake_data()
