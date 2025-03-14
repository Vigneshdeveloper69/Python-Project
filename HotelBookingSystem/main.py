import json, os

class Room:

    def __init__(self, room_id, room_type, price, available=True):

        self.room_id = room_id
        self.room_type = room_type
        self.price = price
        self.available = available

class Customer:

    def __init__(self, customer_id, name, phone):

        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.booked_room = None

class Hotel:

    def __init__(self, db_file="hotel_data.json"):

        self.db_file = db_file
        self.rooms, self.customers = self.load_data()

    def load_data(self):

        if os.path.exists(self.db_file):

            with open(self.db_file, "r") as file:

                data = json.load(file)

                return data.get("rooms", {}), data.get("customers", {})
            
        return {}, {}
    
    def save_data(self):

        with open(self.db_file, "w") as file:

            json.dump({"rooms" : self.rooms, "customers" : self.customers}, file, indent=4)


    def add_room(self, room_id, room_type, price, availability=True):

        if room_id in self.rooms:

            return f"Room : {room_id} is already exist!"
        
        self.rooms[room_id] = {"room_type" : room_type, "price" : price, "availability" : availability}

        self.save_data()

        return f"Room : {room_id} was added successfully!"
    
    def remove_room(self, room_id):

        if room_id not in self.rooms:

            return f"Room : {room_id} is not exist!"
        
        del self.rooms[room_id]

        self.save_data()

        return f"Room : {room_id} was removed successfully!"
    
    def register_customer(self, customer_id, name, phone):

        if customer_id in self.customers:

            return f"Customer : {customer_id} is already exists!"
        
        self.customers[customer_id] = {"name" : name, "phone" : phone, "booked_room" : None}

        self.save_data()

        return f"Customer : {customer_id} was registered successfully!"
    
    def book_room(self, customer_id, room_id):

        if customer_id in self.customers and room_id in self.rooms:

            if self.rooms[room_id]['availability']:

                self.customers[customer_id]["booked_room"] = room_id

                self.rooms[room_id]['availability'] = False

                self.save_data()

                return f"Customer : {self.customers[customer_id]['name']} booked Room : {room_id}" 
            
            return f"Room {room_id} was already booked!"
        
        return f"Invalid customer id or room id"
    
    def cancel_room(self, customer_id):

        if customer_id in self.customers:

            if self.customers[customer_id]['booked_room']:

                room = self.customers[customer_id]['booked_room']

                self.rooms[room]['availability'] = True

                self.customers[customer_id]['booked_room'] = None

                self.save_data()

                return f"Customer : {self.customers[customer_id]['name']} was cancelled Room  : {room}"
            
            return f"Customer : {self.customers[customer_id]['name']} not yet booked any room!"
        
        return "Customer id was not found!"
    
    def view_rooms(self):

        if not self.rooms:

            return "No Rooms are exists!"
        
        return '\n'.join([f"ID : {r} | room_type : {self.rooms[r]['room_type']} | price : {self.rooms[r]['price']} | availability : {self.rooms[r]['availability']}" for r in self.rooms])
    
    def view_customers(self):

        if not self.customers:

            return "No Customers are exists!"
        
        return '\n'.join([f"ID : {c} | name : {self.customers[c]['name']} | phone : {self.customers[c]['phone']} | booked_room : {self.customers[c]['booked_room']}" for c in self.customers])
    

def main():

    hotel = Hotel()

    while True:

        print("------Welcome to the hotel Heaven------")
        print("1.Add Room")
        print("2.Remove Room")
        print("3.Register Customer")
        print("4.Book Room")
        print("5.Cancel Room")
        print("6.View Rooms")
        print("7.View Customers")

        choice = input("Enter your choice :")

        if choice == '1':

            room_id = int(input("Enter room id :"))
            room_type = input("Enter room type :")
            price = int(input("Enter room price :"))

            print(hotel.add_room(room_id, room_type, price))

        elif choice == '2':

            room_id = int(input("Enter room id :"))

            print(hotel.remove_room(room_id))

        elif choice == '3':

            customer_id = int(input("Enter customer id :"))
            name = input("Enter customer name :")
            phone = int(input("Enter customer phone no :"))

            print(hotel.register_customer(customer_id, name, phone))

        elif choice == '4':

            customer_id = int(input("Enter customer id :"))
            room_id = int(input("Enter room id :"))

            print(hotel.book_room(customer_id, room_id))

        elif choice == '5':

            customer_id = int(input("Enter customer id :"))

            print(hotel.cancel_room(customer_id))

        elif choice == '6':

            print(hotel.view_rooms())

        elif choice == '7':

            print(hotel.view_customers())

        elif choice == '8':

            print("Thanks for visiting. come back again !!")

            break

if __name__ == '__main__':

    main()
