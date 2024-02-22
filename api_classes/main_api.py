import random

from api_classes.base_api import BaseAPI
from api_classes.response_classes.response import ResponseData


class BookingAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.booking_url = "booking"

    def get_response_with_booking_id(self, booking_id, headers=None):
        response = self.get(f'{self.booking_url}/{booking_id}', headers=headers)
        return response

    def post_create_booking(self, body):
        post_request = self.post(url=f"{self.booking_url}", headers=None, body=body)
        return post_request

    def patch_data_booking(self, booking_id, body, headers=None):
        patch_response = self.put(url=f'{self.booking_url}/{booking_id}', body=body, headers=headers)
        return patch_response
