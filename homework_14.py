# create 3 classes (Hotel, Taxi, Tour)
# Hotel class should have
# attributes
# name
# place
# rooms_mid as a dictionaries ex. {room1:free, room2:free, room3: free}
# mid_room_price
# rooms_lux as a dictionaries ex. {room1:free, room2:free, room3: free}
# lux_room_price

# methods
# presentation
# booking:  will book a room (makes room:bussy),
# available_room_check: takes (room_type) checks if there is an available(free) room
# discount
# class Hotel:
#     def __init__(self, name, place, rooms_mid, rooms_lux, mid_room_price, lux_room_price):
#         self.name = name
#         self.place = place
#         self.rooms_mid = rooms_mid
#         self.rooms_lux = rooms_lux
#         self.mid_room_price = mid_room_price
#         self.lux_room_price = lux_room_price
#         self.rooms_mid = {room1:free, room2:free, room3: free}
#         self.rooms_lux = {room1:free, room2:free, room3: free}


# hotel_1 = Hotel("Lerane", "Geghard", {'room1':free, 'room2':free, 'room3': free}, {'room1':free, 'room2':free, 'room3': free}, 10000, 20000)    
# print(hotel_1)

# Taxi class should have
# attributes
# name
# car_types
# price_for_tour

# methods
# presentation
# discount
class Taxi:
    def __init__(self, name, car_types, price_for_tour):
        self.name = name
        self.car_types = car_types
        self.price_for_tour = price_for_tour

    def present(self):
        return F"We represent {self.name} company, our cars are {self.car_types}, and the coast per tour is {self.price_for_tour}.\nAlso you can get dscount of 10% if you use min 3 car per tour"

    def discount(self):
        if self.price_for_tour >= 30000:
            disc_price_for_tour = self.price_for_tour - (self.price_for_tour * 0.1)
            return disc_price_for_tour

taxi_1 = Taxi("Taxi Tour", "Mercedes Sprinter", 10000)        
print(Taxi.discount(taxi_1))
print(Taxi.present(taxi_1))

# Tour class should inherit from Hotel and Taxy
# should have attributes
# name
# price_lux = (hotel price lux + taxy price for tour) for one person
# price_mid = …

# methods
# a global presentation of it services (included Hotel and Taxy)

# example
# tour
# name Geghard tour
# price lux 50000 and mid 30000
# including
# taxi
# name ride_over
# type of cars bmw
# price for trip 10000
# hotel
# name Lerane
# place geghard
# rooms rooms middle and rooms lux
# room price 10000(mid) and 20000(lux)
# ex. presentation: Hello we offer Geghard tour we have two options 50000 and 30000,
# which includes transport with ride_over company which provides bmw cars and price for it is 10000,
# we will stay at Lerane which offers two types of rooms middle 10000 and lux 20000