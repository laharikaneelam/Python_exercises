class Flight:
    def __init__(self,capacity):
        self.capacity=capacity
        self.passengers=[]
    def add_passenger(self,name):
        if self.open_seats() == 0:
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity-len(self.passengers)

flight=Flight(8)
passengers_lst=["Laharika","Deepesh","Bindu","Rahul","Varun","Jatin","Aishu","Vinay","Vishal"]
for passenger in passengers_lst:
    if flight.add_passenger(passenger):
        print(f"Added {passenger} into the Flight Passengers List")
    else:
        print(f"No seats Available for {passenger}")
