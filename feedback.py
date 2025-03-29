class Feedback:
    # Constructor to initialize feedback details
    def __init__(self, rating, comments, guest):
        self.rating = rating          # Numeric rating (e.g., 1 to 5)
        self.comments = comments      # Textual feedback provided by the guest
        self.guest = guest            # Reference to the Guest object who submitted the feedback

    # Method to return a formatted feedback string
    def submit_feedback(self):
        return f"Feedback from {self.guest._name}: {self.comments} (Rating: {self.rating}/5)"

    # String representation of the feedback object
    def __str__(self):
        return self.submit_feedback()
