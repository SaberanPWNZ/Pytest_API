from http import HTTPStatus
import requests
import pytest

from api_classes.auth_api import AuthAPI
from api_classes.main_api import BookingAPI
from api_classes.response_classes.response import ResponseData
from utilities.configuration import WRONG_HEADERS, WRONG_AUTH_DATA


@pytest.mark.parametrize("wrong_headers", WRONG_HEADERS, ids=str)
def test_response_status(wrong_headers):
    booking = BookingAPI()
    response = booking.get_response_with_booking_id(booking_id=1, headers=wrong_headers)
    assert response.status_code == HTTPStatus.OK, "Error, status code not 200"


def test_check_response_data(test_open_url):
    json_object = test_open_url
    response_data = ResponseData()  # incorrect example, that must be database request
    assert json_object.firstname == response_data.firstname, "ERROR, wrong firstname"
    assert json_object.lastname == response_data.lastname, "ERROR, wrong lastname"
    assert json_object.totalprice == response_data.totalprice, "ERROR, wrong total price"
    assert json_object.depositpaid == response_data.depositpaid, "ERROR, wrong deposit paid"
    assert json_object.bookingdates == response_data.bookingdates, "ERROR, wrong booking dates"
    assert json_object.additionalneeds == response_data.additionalneeds, "ERROR, wrong additional needs"


def test_create_booking(test_post):
    response = test_post
    response_id = test_post.json()
    assert response.status_code == HTTPStatus.OK, "Invalid status code, new book was not created"
    assert "bookingid" in response_id, "Booking_id is absent"
    assert response_id["bookingid"] > 1, "ERROR, 'bookingid' < 1"


@pytest.mark.parametrize("wrong_auth_data", WRONG_AUTH_DATA, ids=str)
def test_auth(wrong_auth_data):
    auth = AuthAPI()
    response = auth.get_auth_token(json=wrong_auth_data)
    assert response.status_code == 200
    if "token" in response.json():
        assert len(response.json()["token"]) == 15, "token wasn't created"
    else:
        assert response.json() == {'reason': 'Bad credentials'}, "Error, cookie was created with wrong aut data"
