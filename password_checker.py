import os
from pprint import pprint
import pandas as pd


class ReadPassword:

    def __init__(self,  filename, path = os.getcwd(), search_password = '1234'):
        self.filename = filename
        self.path = path
        self.search_password = search_password

    def read_file(self):
        try:
            with open(os.path.join(self.path, self.filename)) as f:
                list_of_passwords: list[str] = f.read().splitlines()
            return  list_of_passwords
        except OSError:
            print('couldn open and read files')
            return None

    def check_passwords(self):

        _password = self.read_file()

        for idx, password_common in enumerate(_password, start=1):
            if password_common == self.search_password:
                return f'this is password: {password_common} and it is located in the line of {idx}'
        return None


if __name__ == "__main__":
    rp = ReadPassword("password.text")
    pprint(rp.check_passwords())
    # enter_password= input("Please enter your search password")



