import unittest
from tests.de2 import *


class DE2TestCase(unittest.TestCase):
    def test_de2_create_token(self):
        response = de2_upload_de_file('beaconama+freshwaterde2@gmail.com', 'Badger_67$123', '6872150474507220434', 'accounts_and_assets', 'test.csv')
        self.assertEqual(response.status_code, 200)
