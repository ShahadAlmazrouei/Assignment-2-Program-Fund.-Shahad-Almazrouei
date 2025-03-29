# main.py

# Import necessary classes from the models package
from models.guest import Guest
from models.room import Room
from models.booking import Booking
from models.feedback import Feedback
from models.service_request import ServiceRequest

# Function to filter and return only available rooms
def search_rooms(rooms):
    return [room for room in rooms if room.is_available()]

# Function to display the main menu options
def display_menu():
    print("\nRoyal Stay Hotel Management System")
    print("1. Book a Room")
    print("2. Cancel Reservation")
    print("3. Submit Feedback")
    print("4. Request Guest Service")
    print("5. View Reservation History")
    print("6. View Loyalty Points")
    print("7. Exit")

# Main application function
def main():
    # Create a guest with initial information and 50 loyalty points
    guest1 = Guest(input("Name: "), input("Email: "), input("Phone: "), 50)

    # List of rooms available in the hotel
    room_list = [
        Room("101", "Single", ["Wi-Fi", "TV"], 100.0),
        Room("102", "Double", ["Wi-Fi", "Mini-bar"], 150.0),
        Room("103", "Suite", ["Wi-Fi", "TV", "Mini-bar"], 200.0)
    ]

    # List to store current active bookings
    current_bookings = []

    # Main program loop
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        # Option 1: Book a room
        if choice == "1":
            available_rooms = [room for room in room_list if room.is_available()]
            if not available_rooms:
                print("No rooms available at the moment.")
            else:
                # Display available rooms
                print("Available rooms:")
                for i, room in enumerate(available_rooms, start=1):
                    print(f"{i}. {room}")

                # Prompt user to select a room
                while True:
                    try:
                        selected = int(input("Select a room by number: "))
                        if 1 <= selected <= len(available_rooms):
                            selected_room = available_rooms[selected - 1]
                            break
                        else:
                            print("❌ Invalid selection. Please choose from the listed numbers.")
                    except ValueError:
                        print("❌ Invalid input. Please enter a valid number.")

                # Collect booking dates
                check_in = input("Enter check-in date (YYYY-MM-DD): ")
                check_out = input("Enter check-out date (YYYY-MM-DD): ")

                # Create the booking and update room status
                booking = Booking(check_in, check_out, guest1, selected_room)
                selected_room.update_status(False)
                current_bookings.append(booking)

                # Show confirmation and invoice
                print("✅ Room successfully booked!")
                print(booking.confirm_booking())
                print(booking.invoice)

        # Option 2: Cancel a reservation
        elif choice == "2":
            if current_bookings:
                print("Your current bookings:")
                for i, b in enumerate(current_bookings, start=1):
                    print(f"{i}. {b}")
                try:
                    cancel_index = int(input("Select booking to cancel by number: ")) - 1
                    if 0 <= cancel_index < len(current_bookings):
                        cancel_booking = current_bookings.pop(cancel_index)
                        print("⚠ Cancelling reservation...")
                        print(cancel_booking.cancel_booking())
                        guest1.reservations.remove(cancel_booking)
                        cancel_booking.room.update_status(True)
                        print("✅ Reservation successfully canceled!")
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("No active bookings to cancel.")

        # Option 3: Submit feedback
        elif choice == "3":
            rating = int(input("Rate your stay (1-5): "))
            comment = input("Write your feedback: ")
            fb = Feedback(rating, comment, guest1)
            print(fb)

        # Option 4: Request a service (e.g., room cleaning)
        elif choice == "4":
            req_type = input("Enter service request (e.g., Room Cleaning, Transportation): ")
            req = ServiceRequest(req_type, guest1)
            print("Request submitted:", req)
            req.update_status("Completed")
            print("Updated:", req)

        # Option 5: View reservation history
        elif choice == "5":
            print("Reservation History:")
            for b in guest1.view_history():
                print(b)

        # Option 6: View loyalty points
        elif choice == "6":
            print(f"Loyalty Points: {guest1.get_points()}")

        # Option 7: Exit the application
        elif choice == "7":
            print("Thank you for using Royal Stay Hotel System. Goodbye!")
            break

        # Invalid menu option
        else:
            print("Invalid choice. Please try again.")

# Entry point for the program
if __name__ == "__main__":
    main()
