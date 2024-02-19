from api_classes.base_api import BaseAPI


class MainAPI(BaseAPI):
    def __init__(self):
        super().__init__(route="qotd")
        self.user = User()

