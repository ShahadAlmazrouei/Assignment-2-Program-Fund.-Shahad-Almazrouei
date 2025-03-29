class ServiceRequest:
    # Constructor to initialize a new service request made by a guest
    def __init__(self, request_type, guest):
        self.request_type = request_type     # Type of service requested (e.g., Room Cleaning, Transportation)
        self.guest = guest                   # Guest object who made the request
        self.status = "Pending"             # Initial status of the request (default is "Pending")

    # Method to update the status of the service request
    def update_status(self, new_status):
        self.status = new_status            # Update status to new value (e.g., "Completed")

    # String representation of the service request
    def __str__(self):
        return f"Request: {self.request_type}, Guest: {self.guest._name}, Status: {self.status}"
