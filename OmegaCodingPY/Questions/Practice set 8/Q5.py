#  Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways. 

class Train:
    def __init__(self,name,price,total_seats):
        self.name = name
        self.price = price
        self.total_seats = total_seats
        self.available_seats = total_seats

    def book_ticket(self,num_tickets=1):
        if(num_tickets<=self.available_seats):
            self.available_seats -= num_tickets
            print(f"{num_tickets} tickets booked successfully")
        else:
            print("Seats not Available")
    
    def get_status(self):
        print(f"Train : {self.name}")
        print(f"Availabe seats : {self.available_seats}/{self.total_seats}")
    
    def fare_info(self):
        print(f"Price per ticket : ₹{self.price}")


train = Train("Vande Bharat Express",700,1500)

train.get_status()
train.book_ticket(3)
train.fare_info()
train.get_status()