"""Module provides functions to generate data for insurance part in fake car insurance data."""

from datetime import datetime, timedelta

from src.singleton import FakerSingleton

fake = FakerSingleton.get_instance()


def generate_start_date() -> str:
    """This function returns the start date of car insurance in MM/DD/YYYY format.

    :return: A string representing the start date of car insurance in MM/DD/YYYY format.
    """
    return datetime.now().strftime("%m/%d/%Y")


def generate_end_date() -> str:
    """This function returns the end date of car insurance in MM/DD/YYYY format.

    :return:  string representing the end date of car insurance in MM/DD/YYYY format.
    """
    next_year_date = datetime.now() + timedelta(days=365)
    return next_year_date.strftime("%m/%d/%Y")
