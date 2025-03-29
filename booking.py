from models.invoice import Invoice

class Booking:
    # Constructor to initialize a booking instance with guest, room, and dates
    def __init__(self, check_in, check_out, guest, room):
        self.check_in = check_in                  # Check-in date
        self.check_out = check_out                # Check-out date
        self.guest = guest                        # Guest who is making the booking
        self.room = room                          # Room that is being booked
        self.invoice = Invoice(self)              # Automatically generate invoice for the booking
        guest.reservations.append(self)           # Add this booking to the guest's reservation history

    # Method to confirm the booking if the room is available
    def confirm_booking(self):
        if self.room.is_available():              # Check if room is still available
            self.room.update_status(False)        # Mark the room as booked (not available)
            self.guest.add_points(1)              # Add loyalty points (1 night = 10 points in Guest class)
            return (
                f"Booking confirmed for {self.guest._name} in Room {self.room.room_number}\n"
                f"Email sent to {self.guest._email} with booking confirmation."
            )
        return "Room is not available."

    # Method to cancel the booking and make the room available again
    def cancel_booking(self):
        self.room.update_status(True)             # Mark the room as available again
        return f"Booking for {self.guest._name} cancelled. Room {self.room.room_number} is now available."

    # String representation of the booking object
    def __str__(self):
        return (
            f"Booking: {self.guest._name} in Room {self.room.room_number}, "
            f"Check-in: {self.check_in}, Check-out: {self.check_out}"
        )
