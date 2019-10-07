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

    def setUp(self):
        """
        Setting up the structure before each test
        """
        self.new_data = UsersInfo(1, 1, "gmail.com", "kiriu")

    def tearDown(self):
        """
        cleans up the test after the test is complete
        """
        UsersInfo.data_list = []

    def test_init(self):
        """
        Test to check if the objects have been initialized appropriately
        """
        self.assertEqual(self.new_data.ident, 1)
        self.assertEqual(self.new_data.data_id, 1)
        self.assertEqual(self.new_data.website, "gmail.com")
        self.assertEqual(self.new_data.web_key, "kiriu")

    def test_add_password(self):
        '''
        Testing if the new website and password can be saved
        '''
        self.new_data.add_password()
        self.assertEqual(len(UsersInfo.data_list), 1)

    def test_display_data(self):
        '''
        Testing if the data can be displayed.
        '''
        self.new_data.add_password()
        test_data = UsersInfo(1, 1, "gmail.com", "kiriu")
        test_data.add_password()

        data_found = UsersInfo.display_data(1, 1)
        self.assertEqual(data_found.website, test_data.website)

    def test_data_exists(self):
        '''
        Testing to check if the function for checking data works well
        '''
        self.new_data.add_password()
        test_data = UsersInfo(1, 1, "gmail.com", "kiriu")
        test_data.add_password()

        data_exists = UsersInfo.existing_data(1)
        self.assertTrue(data_exists)

    def test_copy_password(self):
        '''
        Testing if the copy password function works
        '''
        self.new_data.add_password()
        UsersInfo.copy_password(1, 1)

        self.assertEqual(self.new_data.web_key, pyperclip.paste())


if __name__ == "__main__":
    unittest.main()
