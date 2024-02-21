from http import HTTPStatus

import pytest

from api_classes.main_api import BookingAPI
from api_classes.response_classes.response import ResponseData


@pytest.mark.parametrize("headers", [])
def test_response_status():
    booking = BookingAPI()
    response = booking.get_response_with_booking_id(booking_id=1, headers=None)
    assert response.status_code == HTTPStatus.OK, "Error, status code not 200"


def test_check_response_data(test_open_url):
    json_object = test_open_url
    response_data = ResponseData()  # incorrect example, database missing
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



