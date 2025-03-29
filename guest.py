from models.user import User

class Guest(User):
    # Constructor to initialize guest details along with loyalty points
    def __init__(self, name, email, phone, loyalty_points=0):
        super().__init__(name, email, phone)     # Call the parent User constructor
        self.__loyalty_points = loyalty_points   # Private attribute to store guest's loyalty points
        self.reservations = []                   # List to store all bookings made by the guest

    # Method to simulate account creation (returns confirmation message)
    def create_account(self):
        return f"Account created for {self._name}"

    # Method to view guest's past reservation history
    def view_history(self):
        return [str(booking) for booking in self.reservations] if self.reservations else ["No reservations yet."]

    # Method to redeem loyalty points
    def redeem_points(self, points):
        if points <= self.__loyalty_points:
            self.__loyalty_points -= points
            return f"Redeemed {points} points. Remaining: {self.__loyalty_points}"
        return "Not enough points."

    # Method to add loyalty points (e.g., based on number of nights stayed)
    def add_points(self, nights):
        self.__loyalty_points += nights * 10

    # Method to return the current loyalty point balance
    def get_points(self):
        return self.__loyalty_points

    # String representation of the guest object including loyalty points
    def __str__(self):
        return f"Guest: {super().__str__()}, Loyalty Points: {self.__loyalty_points}"
