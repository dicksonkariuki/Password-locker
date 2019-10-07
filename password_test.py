import unittest  # importing the unittest module
import pyperclip  # importing the pyperclip module
from password import Credentials, UsersInfo  # importing user defined classes


class TestCredentials(unittest.TestCase):
    """
        Test class that defines the test cases for Credentials class.
    """

    def setUp(self):
        """
        Set up method to run before each test case
        """
