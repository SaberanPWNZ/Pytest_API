import json


class ResponseData:
    def __init__(self, **kwargs):
        self.firstname = "Eric" if "text" not in kwargs.keys() else kwargs["firstname"]
        self.lastname = "Ericsson" if "year" not in kwargs.keys() else kwargs["lastname"]
        self.totalprice = "827" if "number" not in kwargs.keys() else kwargs["total_price"]
        self.depositpaid = "True" if "found" not in kwargs.keys() else kwargs["depositpaid"]
        self.bookingdates = {'checkin': '2022-09-25', 'checkout': '2022-10-06'} if "type" not in kwargs.keys() else \
        kwargs["bookingdates"]
        self.additionalneeds = "Breakfast" if "type" not in kwargs.keys() else kwargs["additionalneeds"]

    def get_update_data(self, **kwargs):
        self.__dict__.update(**kwargs)

    def get_json(self):
        return json.dumps(self.__dict__)

    def get_dict(self):
        return self.__dict__
