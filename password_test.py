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
        self.new_user = Credentials(1, "dickson", "kiriu")

    def tearDown(self):
        """
        Teardown method that clean up after running each testcase
        """
        Credentials.users_list = []

    def test_init(self):
        """
        test_init test case to test if the objects are initialized correctly
        """
        self.assertEqual()
