import pytest
from selenium import webdriver

from api_classes.main_api import BookingAPI
from api_classes.response_classes.response import ResponseData
from utilities.configuration import HEADERS, BODY, UPDATED_BODY


@pytest.fixture
def test_create_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def test_open_url():
    booking = BookingAPI()
    response = booking.get_response_with_booking_id(1)
    response_json = ResponseData(**response.json())
    return response_json


@pytest.fixture()
def test_post():
    body_json = ResponseData().get_json()
    create_new_book = BookingAPI().post_create_booking(json=BODY, data=None)
    return create_new_book



