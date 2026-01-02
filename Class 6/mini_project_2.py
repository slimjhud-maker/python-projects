class Flight:
    def __init__(self, flight_number, destination, seats_available, base_price):
        self.flight_number = flight_number
        self.destination = destination
        self.seats_available = seats_available
        self.base_price = base_price

    def book_ticket(self, passenger_name):
        if self.seats_available > 0:
            self.seats_available -= 1
            print("Ticket booked for", passenger_name)
        else:
            print("No seats available for this flight.")

    def ticket_price(self):
        print(self.base_price)

    def display_flight_info(self):
        print(f"""
Flight Number: {self.flight_number}
Destination: {self.destination}
Seats Available: {self.seats_available}
Ticket Price: {self.base_price}
""")


class DomesticFlight(Flight):
    def __init__(self, flight_number, destination, seats_available, base_price):
        super().__init__(flight_number, destination, seats_available, base_price)

    def ticket_price(self):
        price = self.base_price + (0.05 * self.base_price)
        print(price)

    def display_flight_info(self):
        price = self.base_price + (0.05 * self.base_price)
        print(f"""
Flight Number: {self.flight_number}
Destination: {self.destination}
Seats Available: {self.seats_available}
Ticket Price: {price}
""")


class InternationalFlight(Flight):
    def __init__(self, flight_number, destination, seats_available, base_price):
        super().__init__(flight_number, destination, seats_available, base_price)

    def ticket_price(self):
        price = self.base_price + (0.10 * self.base_price) + (0.20 * self.base_price)
        print(price)

    def display_flight_info(self):
        price = self.base_price + (0.10 * self.base_price) + (0.20 * self.base_price)
        print(f"""
Flight Number: {self.flight_number}
Destination: {self.destination}
Seats Available: {self.seats_available}
Ticket Price: {price}
""")


class Passenger:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number

    def book_flight(self, flight):
        flight.book_ticket(self.name)


d = DomesticFlight("AI-101", "Dubai", 3, 5000)
i = InternationalFlight("AI-202", "London", 2, 15000)

p1 = Passenger("Jhud", "A11111")
p2 = Passenger("Akash", "B22222")

d.display_flight_info()
p1.book_flight(d)
d.display_flight_info()

i.display_flight_info()
p2.book_flight(i)
i.display_flight_info()

i.display_flight_info()
p2.book_flight(i)
i.display_flight_info()
