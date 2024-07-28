import json
import os


class DataReader:
    def __init__(self):
        # Load JSON configuration
        with open('./resources/test_data.json', 'r') as config_file:
            self.test_data = json.load(config_file)

    @property
    def login_username_standard(self):
        return self.test_data['login']['username_standard']

    @property
    def login_password_correct(self):
        return self.test_data['login']['password_correct']

    @property
    def login_password_incorrect(self):
        return self.test_data['login']['password_incorrect']

    @property
    def login_username_lockedout(self):
        return self.test_data['login']['username_lockedout']

    @property
    def checkout_first_name(self):
        return self.test_data['checkout_user']['first_name']

    @property
    def checkout_last_name(self):
        return self.test_data['checkout_user']['last_name']

    @property
    def checkout_postal_code(self):
        return self.test_data['checkout_user']['postal_code']


# Instantiate the configuration
data_reader = DataReader()
