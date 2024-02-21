from http import HTTPStatus

from api_classes.main_api import BookingAPI


def test_response_status():
    booking = BookingAPI()
    response = booking.get_response_with_booking_id(booking_id=1, headers=None)
    assert response.status_code == HTTPStatus.OK, "Error, status code not 200"


def test_check_response_data(test_open_url):
    json_object = test_open_url
    assert json_object.firstname == "Eric"
    assert json_object.lastname == "Ericsson"
    assert json_object.total_price == "827"
    assert json_object.deposit_paid == "True"
    assert json_object.booking_dates == {'checkin': '2022-09-25', 'checkout': '2022-10-06'}
    assert json_object.additional_needs == "Breakfast"


def test_create_booking(test_post):
    response = test_post
    print(response.text)
    assert response.status_code == HTTPStatus.OK, "Invalid status code, new book was not created"






