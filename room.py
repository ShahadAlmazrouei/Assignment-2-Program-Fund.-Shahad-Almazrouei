class Room:
    # Constructor to initialize a room with its details
    def __init__(self, room_number, room_type, amenities, price, available=True):
        self.room_number = room_number      # Unique identifier for the room
        self.room_type = room_type          # Type of the room (e.g., Single, Double, Suite)
        self.amenities = amenities          # List of amenities (e.g., Wi-Fi, TV)
        self.price = price                  # Price per night for the room
        self.available = available          # Room availability status (True by default)

    # Method to check if the room is available
    def is_available(self):
        return self.available

    # Method to update the availability status of the room
    def update_status(self, status):
        self.available = status

    # String representation of the room object
    def __str__(self):
        return f"Room {self.room_number} ({self.room_type}): ${self.price} per night. Available: {self.available}"
