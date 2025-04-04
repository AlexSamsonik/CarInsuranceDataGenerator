"""Module provides tests for insurance part in fake car insurance data."""

from datetime import datetime, timedelta

from src.insurance import generate_end_date, generate_start_date


def test_generate_start_date():
    """Test the generate_start_date function to ensure it returns the current date in MM/DD/YYYY format."""
    current_date = datetime.now().strftime("%m/%d/%Y")
    assert generate_start_date() == current_date, f"Expected {current_date}, but got {generate_start_date()}"


def test_generate_end_date():
    """Test the generate_end_date function to ensure it returns the date one year from the current date in MM/DD/YYYY format."""
    current_date = datetime.now()
    next_year_date = (current_date + timedelta(days=365)).strftime("%m/%d/%Y")
    assert generate_end_date() == next_year_date, f"Expected {next_year_date}, but got {generate_end_date()}"
