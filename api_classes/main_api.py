from api_classes.base_api import BaseAPI


class BookingAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.booking_url = "booking"

    def get_response_with_booking_id(self, booking_id, headers=None):
        response = self.get(f'{self.booking_url}/{booking_id}', headers=headers)
        return response

    def post_create_booking(self, json, data):
        post_request = self.post(url=f"{self.booking_url}", headers=None, json=json, data=data)
        return post_request

    def patch_data_booking(self, booking_id, data, headers=None, cookies=None):
        patch_response = self.patch(f'{self.booking_url}/{booking_id}', data=data, headers=headers, cookies=cookies)
        return patch_response
