from http import HTTPStatus

import pytest

from api_classes.main_api import BookingAPI
from api_classes.response_classes.response import ResponseData
from utilities.configuration import WRONG_HEADERS, BODY, HEADERS, UPDATED_BODY


@pytest.mark.skip
@pytest.mark.parametrize("wrong_headers", WRONG_HEADERS, ids=str)
def test_response_status(wrong_headers):
    booking = BookingAPI()
    response = booking.get_response_with_booking_id(booking_id=1, headers=wrong_headers)
    assert response.status_code == HTTPStatus.OK, "Error, status code not 200"

@pytest.mark.skip
def test_check_response_data(test_open_url):
    json_object = test_open_url
    response_data = ResponseData()  # incorrect example, that must be database request
    assert json_object.firstname == response_data.firstname, "ERROR, wrong firstname"
    assert json_object.lastname == response_data.lastname, "ERROR, wrong lastname"
    assert json_object.totalprice == response_data.totalprice, "ERROR, wrong total price"
    assert json_object.depositpaid == response_data.depositpaid, "ERROR, wrong deposit paid"
    assert json_object.bookingdates == response_data.bookingdates, "ERROR, wrong booking dates"
    assert json_object.additionalneeds == response_data.additionalneeds, "ERROR, wrong additional needs"

@pytest.mark.skip
def test_create_booking(test_post):
    response = test_post
    response_id = test_post.json()
    assert response.status_code == HTTPStatus.OK, "Invalid status code, new book was not created"
    assert "bookingid" in response_id, "Booking_id is absent"
    assert response_id["bookingid"] > 1, "ERROR, 'bookingid' < 1"


def test_update_booking():
    request = BookingAPI().patch_data_booking(booking_id=1, headers=HEADERS, body=UPDATED_BODY)
    response = request.status_code
    print(response)
    # assert test_update.firstname == "update_name", "first name was not equal to expected"
    # assert test_update.lastname == "update_lastname", "lastnamee was not equal to expected"
    # assert test_update.totalprice == 1488, "totalprice was not equal to expected"
    # assert test_update.depositpaid == "False", "depositpaid was not equal to expected"
    # assert test_update.bookingdates == {
    #     "checkin": "2022-01-01", "checkout": "2022-01-01"}, \
    #     "bookingdates was not equal to expected"
    # assert test_update.additionalneeds == "UPDATE", "additionalneeds was not equal to expected"
