from models.user import User

class Staff(User):
    """Staff class inheriting from User."""

    # Constructor to initialize staff details along with their role
    def __init__(self, name, email, phone, role):
        super().__init__(name, email, phone)  # Call the parent User class constructor
        self.role = role                      # Role of the staff member (e.g., Manager, Receptionist)

    # Method to simulate the staff processing a guest service request
    def process_request(self):
        return f"{self._name} (Role: {self.role}) is processing a request."

    # String representation of the staff object
    def __str__(self):
        return f"Staff: {super().__str__()}, Role: {self.role}"
