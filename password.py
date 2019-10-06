class Credentials:
    """
    class that creates a user's account and authentication information.
    """
    users_list = []

    def __init__(self, authenticate, username, password):
        """
        variable initialization.
        """
        self.authenticate = authenticate
        self.username = username
        self.password = password

    def create_account(self):
        """
        A method to create new accounts and saving them in the user's list.
        """
        Credentials.users_list.append(self)
