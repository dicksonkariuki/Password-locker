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
        self.assertEqual(self.new_user.authenticate, 1)
        self.assertEqual(self.new_user.username, "dickson")
        self.assertEqual(self.new_user.password, "kiriu")

    def test_create(self):
        """
        Testing if the new credential is saved in the list.
        """
        self.new_user.create_account()
        self.assertEqual(len(Credentials.users_list), 1)

    def test_authenticate(self):
        """
        Testing if the authenticate function can sign in a user appropriately.
        """
        self.new_user.create_account()
        test_account = Credentials(1, "Test", "password")
        test_account.create_account()

        found_user = Credentials.authenticate_account("Test", "password")
        self.assertEqual(found_user.authenticate, test_account.authenticate)


class UsersInfo(unittest.TestCase):
    """
    Test class that defines test cases for UsersInfo class
    """


if __name__ == "__main__":
    unittest.main()
