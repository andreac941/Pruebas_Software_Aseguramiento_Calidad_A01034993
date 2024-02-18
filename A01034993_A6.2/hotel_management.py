# -*- coding: utf-8 -*-
""" hotel_management:
	Clases created for creating basic hotel reservations.
"""

# CLASSES DEFINITION:
import datetime


class Hotel:
    """ 
    Class Hotel:
    To create hotel instances.
    """
    def __init__(self, name, location, rooms):
        """ __init__:
	To create Hotel instances with attributes.
        """
        self.name = name
        self.location = location
        self.rooms = rooms
        self.reservations = []

    def create_reservation(self, customer, room_number, start_date, end_date):
        """ create_reservation:
	Function to create reservations.
        """
        if not self.is_valid_room_number(room_number):
            raise ValueError("Invalid room number")

        if not self.is_valid_date(start_date):
            raise ValueError("Invalid start date")

        if not self.is_valid_date(end_date):
            raise ValueError("Invalid end date")

        if not self.is_room_available(room_number, start_date, end_date):
            raise ValueError("Room not available for the given period")

        reservation = Reservation(customer, self, room_number, start_date, end_date)
        self.reservations.append(reservation)
        return reservation

    def cancel_reservation(self, reservation):
        """ cancel_reservation:
 	Function to cancel reservations.
        """
        if reservation not in self.reservations:
            raise ValueError("Reservation does not exist")

        if reservation.is_canceled():
            raise ValueError("Reservation is already canceled")

        self.reservations.remove(reservation)
        return True

    def display_information(self):
        """ display_information:
	Function to display hotel information.
        """
        return f"Hotel: {self.name}, Location: {self.location}, Rooms: {self.rooms}"

    def modify_information(self, name=None, location=None, rooms=None):
        """ modify_information:
	Function to modify hotel information.
        """
        if name:
            self.name = name
        if location:
            self.location = location
        if rooms:
            self.rooms = rooms

    def reserve_room(self, customer, room_number, start_date, end_date):
        """ reserve_room:
	Function to reserve a hotel room.
        """
        if not self.is_valid_room_number(room_number):
            raise ValueError("Invalid room number")

        if not self.is_valid_date(start_date):
            raise ValueError("Invalid start date")

        if not self.is_valid_date(end_date):
            raise ValueError("Invalid end date")

        if not self.is_room_available(room_number, start_date, end_date):
            raise ValueError("Room not available for the given period")

        reservation = self.create_reservation(customer, room_number, start_date, end_date)
        return True, reservation

    def cancel_room_reservation(self, reservation):
        """ cancel_room_reservation:
	Function to cancel a hotel room.
        """
        if reservation not in self.reservations:
            raise ValueError("Reservation does not exist")

        if not self.is_valid_room_number(reservation.room_number):
            raise ValueError("Invalid room number")

        if not self.is_valid_date(reservation.start_date):
            raise ValueError("Invalid start date")

        if not self.is_valid_date(reservation.end_date):
            raise ValueError("Invalid end date")

        self.reservations.remove(reservation)
        return True

    def is_valid_room_number(self, room_number):
        """ is_valid_room_number:
	Function to validate the room number.
        """
        return 1 <= room_number <= self.rooms

    def is_valid_date(self, date):
        """ is_valid_date:
	Function to validate the date.
        """
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            return True
        except ValueError:
            raise ValueError("Invalid date format. Please use the format YYYY-MM-DD.") from None

    def is_room_available(self, room_number, start_date, end_date):
        """ is_room_available:
	Function to validate if there is a room available.
        """
        for reservation in self.reservations:
            if reservation.room_number == room_number:
                if reservation.start_date <= start_date < reservation.end_date or \
                    reservation.start_date < end_date <= reservation.end_date:
                    return False
        return True


class Reservation:
    """ Class Reservation:
	To create reservation instances.
    """
    def __init__(self, customer, hotel, room_number, start_date, end_date):
        """ __init__:
	Function to create reservation instances.
        """
        self.customer = customer
        self.hotel = hotel
        self.room_number = room_number
        self.start_date = start_date
        self.end_date = end_date
        self.canceled = False  # Initialize the canceled attribute

    @classmethod
    def create_reservation(cls, customer, hotel, room_number, start_date, end_date):
        """ create_reservation:
	Function to create a reservation.
        """
        if not cls.is_valid_date(start_date):
            raise ValueError("Invalid start date. Start date must be in the future.")

        if not cls.is_valid_date(end_date):
            raise ValueError("Invalid end date. End date must be in the future and after the start date.")

        if start_date >= end_date:
            raise ValueError("Invalid date range. End date must be after the start date.")

        return cls(customer, hotel, room_number, start_date, end_date)

    def cancel_reservation(self):
        """ cancel_reservation:
	Function to cancel a reservation.
        """
        # Check if the reservation is already canceled
        if self.is_canceled():
            raise ValueError("Reservation is already canceled")

        # Implement cancellation logic based on your requirements
        # For example, you could mark the reservation as canceled
        self.canceled = True

        # Or you could remove the reservation from the hotel's list of reservations
        self.hotel.cancel_reservation(self)

        return True, "Reservation successfully canceled"

    def is_canceled(self):
        """ is_canceled:
	Function to validate if reservation is canceled.
        """
        # Check if the reservation is already canceled
        return getattr(self, 'canceled', False)

    @staticmethod
    def is_valid_date(date):
        """ is_valid_date:
	Function to validate the date.
        """
        try:
            parsed_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            today = datetime.date.today()
            if parsed_date <= today:
                return False
            return True
        except ValueError:
            raise ValueError("Invalid date format. Please use the format YYYY-MM-DD.") from None


class Customer:
    """ Class Customer:
	To create customer instances.
    """
    all_customers = []

    def __init__(self, name, email, phone):
        """ __init__:
	Function to create customer instances.
        """
        self.name = name
        self.email = email
        self.phone = phone
        Customer.all_customers.append(self)  # Add the newly created customer to the global list

    @classmethod
    def create_customer(cls, name, email, phone):
        """ create_customer:
	Function to create a customer.
        """
        if not name or not email or not phone:
            raise ValueError("Missing information. Name, email, and phone number are required.")

        if not cls.is_valid_email(email):
            raise ValueError("Invalid email format. Please provide a valid email address.")

        return cls(name, email, phone)

    def delete_customer(self):
        """ delete_customer:
	Function to delete a customer.
        """
        if self not in Customer.all_customers:
            raise ValueError("Customer does not exist.")

        Customer.all_customers.remove(self)
        return True

    def display_information(self):
        """ display_information:
	Function to display customer information.
        """
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}"

    def modify_information(self, name=None, email=None, phone=None):
        """ modify_information:
	Function to modify customer information.
        """
        if email and not self.is_valid_email(email):
            raise ValueError("Invalid email format. Please provide a valid email address.")

        if self not in Customer.all_customers:
            raise ValueError("Customer does not exist.")

        if name:
            self.name = name
        if email:
            self.email = email
        if phone:
            self.phone = phone

    @staticmethod
    def is_valid_email(email):
        """ is_valid_email:
	Function to validate customer email.
        """
        # Add your email validation logic here
        # For simplicity, let's just check if the email contains '@'
        return '@' in email
