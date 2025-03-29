class User:
    # Constructor to initialize a user with basic personal information
    def __init__(self, name, email, phone):
        self._name = name              # Protected attribute: user's name
        self._email = email            # Protected attribute: user's email
        self._phone = phone            # Protected attribute: user's phone number

    # Method to update user's profile information
    def update_profile(self, name=None, email=None, phone=None):
        if name:
            self._name = name          # Update name if provided
        if email:
            self._email = email        # Update email if provided
        if phone:
            self._phone = phone        # Update phone number if provided

    # Method to retrieve user's details in a formatted string
    def get_details(self):
        return f"Name: {self._name}, Email: {self._email}, Phone: {self._phone}"

    # String representation of the user object
    def __str__(self):
        return self.get_details()