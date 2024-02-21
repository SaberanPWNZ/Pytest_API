HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

BODY = {
    "firstname": "sssss",
    "lastname": "DOE",
    "totalprice": 999,
    "depositpaid": "True",
    "bookingdates": {
        "checkin": "2020-01-01",
        "checkout": "202021-01-01"
    },
    "additionalneeds": "NONAME"
}

BASE_URL = "https://restful-booker.herokuapp.com/booking"
