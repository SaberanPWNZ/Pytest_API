import requests
from utilities.configuration import HEADERS


class BaseAPI:

    def __init__(self):
        self.__base_url = f"https://restful-booker.herokuapp.com"
        self.__headers = HEADERS
        self.__request = requests

    def get(self, url: str, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__request.get(f"{self.__base_url}/{url}", headers=headers)
        return response

    def post(self, url, json=None, data=None, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__request.post(f"{self.__base_url}/{url}", headers=headers, json=json, data=data)
        return response

    def patch(self, url, data, headers=None, cookies=None, ):
        if headers is None:
            headers = self.__headers
        response = self.__request.patch(f"{self.__base_url}/{url}", headers=headers, data=data, cookies=cookies, )
        return response
