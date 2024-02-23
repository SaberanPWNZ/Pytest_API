from api_classes.base_api import BaseAPI
from utilities.configuration import AUTH_DATA, HEADERS


class AuthAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.url = "auth"

    def get_auth_token(self, json=None, headers=None):
        response = self.post(url=self.url, json=json, headers=headers)
        return response
