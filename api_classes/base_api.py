import requests

from utilities.configuration import HEADERS, API_KEY


class BaseAPI:

    def __init__(self, route: str):
        self.url = f"https://favqs.com/api/{route}"
        self.cookies = ""
        self.headers = HEADERS
        self.api_key = API_KEY
        self.body = ""

    def get_url(self):
        return requests.get(url=self.url, headers=self.headers, cookies=None, data=None)

    def post_url(self):
        return requests.post(self.url, headers=self.headers, cookies=None, data=None)



