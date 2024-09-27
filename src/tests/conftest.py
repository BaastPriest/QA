import pytest
from src import data

@pytest.fixture()
def booking_body():
    return data.booking_body.copy()