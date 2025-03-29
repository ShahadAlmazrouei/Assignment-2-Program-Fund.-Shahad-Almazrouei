class Invoice:
    # Constructor to initialize the invoice using details from a booking
    def __init__(self, booking):
        self.total_amount = booking.room.price        # Base amount from the room's price
        self.taxes = self.total_amount * 0.1          # Tax calculated at 10% of the total
        self.discounts = 0                            # Discount applied (set to 0 by default)

    # Method to generate a formatted invoice string
    def generate_invoice(self):
        return (
            f"Invoice\n"
            f"--------\n"
            f"Total: ${self.total_amount}\n"
            f"Taxes: ${self.taxes}\n"
            f"Discounts: ${self.discounts}\n"
            f"Final Amount: ${self.total_amount + self.taxes - self.discounts}"
        )

    # String representation of the invoice object
    def __str__(self):
        return self.generate_invoice()
