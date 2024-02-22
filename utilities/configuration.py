HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    'Cookie': 'token=abc123'
}

WRONG_HEADERS = [
    ({"accept": "application/json", "Content-Type": "application/json"}),
    ({"ACCEPT": "application/json", "Content-Type": "application/json"}),
    ({"accept1": "application/json", "Content-Type": "application/json"}),
    ({"ACCEPT1": "application/json", "Content-Type": "application/json"}),
    ({"ACCEPT1": "application/json", "content-type": "application/json"}),
    ({"ACCEPT1": "application/json", "Content-Type": "1"}),
    ({"random": "random", "random1": "random"})

]

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

UPDATED_BODY = {
    "firstname": "update_name",
    "lastname": "update_lastname",
    "totalprice": 1488,
    "depositpaid": "False",
    "bookingdates": {
        "checkin": "2022-01-01",
        "checkout": "2022-01-01"
    },
    "additionalneeds": "UPDATE"
}

BASE_URL = "https://restful-booker.herokuapp.com/booking"
