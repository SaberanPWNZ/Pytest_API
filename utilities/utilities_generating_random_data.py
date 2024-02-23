import random
from faker import Faker

fake = Faker(locale="en")


class User:
    def __init__(self):
        self.username = fake.user_name()
        self.password = fake.password()

    def new_user(self):
        return {str(self.username): str(self.password)}
