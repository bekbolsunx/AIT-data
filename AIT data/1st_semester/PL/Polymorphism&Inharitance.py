# class Items:
#     def __init__(self,brand,price,weight, location):
#         self.brand = brand
#         self.price = price
#         self.weight = weight
#         self.location = location

#     def get_location(self):
#         return self.location
    
#     def set_location(self, location):
#         self.location = location

#     def show_info(self):
#         pass

# # # class Car_v1(Items):
# # #     def set_cartype(self, type):
# # #         self.car_type = type

# # #     def set_color(self, color):
# # #         self.color = color

# # #     def show_info(self):
# # #         print(self.brand,self.price, self.weight, self.location, self.car_type, self.color )


# class Car(Items):
#     def _init_(self, brand, price, weight, location, type, color):
#         super()._init_(brand, price, weight, location)
#         self.color = color
#         self.car_type = type
  
#     def show_info(self):
#         print(self.brand,self.price, self.weight, self.location, self.car_type, self.color)



# class Shampoo(Items):
#     def _init_(self, brand, price, weight, location, compound, gender):
#         super()._init_(brand, price, weight, location)
#         self.gender = gender
#         self.compound = compound

#     def show_info(self):
#         print(self.brand,self.price, self.weight, self.location, self.gender, self.compound)



# class TShirt(Items):
#     def _init_(self, brand, price, weight, location,material):
#         super()._init_(brand, price, weight, location)
#         self.material = material

#     def show_info(self):
#         print(self.brand,self.price, self.weight, self.location, self.material)

    
    
# def add_item(cart, item):
#     cart.append(item)

# def move(cart, location):
#     for item in cart:
#         item.set_location(location)



# car = Car('BMW', 5000, 1500, 'Bishkek','sedan','black')
# tshirt = TShirt('nike', 15,0.1, 'Bishkek','cotton') 
# shampoo = Shampoo('Clear',5,1,'Bishkek','water','male')
# cart = []


# add_item(cart,car)
# add_item(cart,tshirt)
# add_item(cart,shampoo)


# move(cart,'New York')

# tshirt.show_info()


class Items:
    def __init__(self, brand, price, weight, location):
        self.brand = brand
        self.price = price
        self.weight = weight
        self.location = location

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def show_info(self):
        pass

class Car(Items):
    def __init__(self, brand, price, weight, location, car_type, color):
        super().__init__(brand, price, weight, location)
        self.color = color
        self.car_type = car_type

    def show_info(self):
        print(self.brand, self.price, self.weight, self.location, self.car_type, self.color)

class Shampoo(Items):
    def __init__(self, brand, price, weight, location, compound, gender):
        super().__init__(brand, price, weight, location)
        self.gender = gender
        self.compound = compound

    def show_info(self):
        print(self.brand, self.price, self.weight, self.location, self.gender, self.compound)

class TShirt(Items):
    def __init__(self, brand, price, weight, location, material):
        super().__init__(brand, price, weight, location)
        self.material = material

    def show_info(self):
        print(self.brand, self.price, self.weight, self.location, self.material)

def add_item(cart, item):
    cart.append(item)

def move(cart, location):
    for item in cart:
        item.set_location(location)

car = Car('BMW', 5000, 1500, 'Bishkek', 'sedan', 'black')
tshirt = TShirt('nike', 15, 0.1, 'Bishkek', 'cotton')
shampoo = Shampoo('Clear', 5, 1, 'Bishkek', 'water', 'male')
cart = []

add_item(cart, car)
add_item(cart, tshirt)
add_item(cart, shampoo)

move(cart, 'New York')

tshirt.show_info()




####################################################################################################################################################################################################



#LAB 07.12.2023


class AirTicket:
    def __init__(self,price,seat,type):
        self.price = price
        self.seat = seat
        self.type = None
        
        
class Economy(AirTicket):
    def __init__(self,price,seat,):
        super().__init__(self,price,seat)
        self.type = "economy"
        
class Business(AirTicket):
    def __init__(self,price,seat):
        super().__init__(self,price,seat)
        self.type = "business"
        
        
        
class AviaKassa:
    def __init__(self,economy_seats,business_seats,economy_price = 1000,business_price = 3000):
        self.economy_price = economy_price
        self.business_price = business_price
        
        self.business_seat = [["" for i in range(2)] for e in economy_seats]
        self.economy_seat = [["" for i in range(3)]for b in business_seats]
        
        self.revenue = 0
    
    
    
    
    def show_availibiity_seat(self,row, column,seat_type):
        if seat_type.lower() == 'economy':
            if self.economy_seat[row][column] != "∎":
                print(f'(Эконом) Места на {row} : ряду и {column}:колонне свободны .')
            else:
                print('К сожилению мест нет')
        elif seat_type.lower() == 'business':
            if self.business_seat[row][column] != "∎":
                print(f'(Бизнес) Места на {row} : ряду и {column}:колонне свободны .') 
            else:
                print('К сожилению мест нет ')
    




    def buy_ticket(self,seat_type, row, column):
        if seat_type.lower() == "economy":
            if self.economy_seat[row][column] != "∎":
                # self.economy_seat[row][column] = "∎" 
                self.revenue += self.economy_price
                print(f"Продано в ряду {row} места {column} (Эконом)")
                
        if seat_type.lower() == "business":
            if self.business_seat[row][column] != "∎":
                # self.business_seat[row][column] = "∎"
                self.revenue += self.business_price
                print(f"Продано в ряду {row} места {column} (Бизнес)")





    def change_seats(self,seat_type,p_row,p_column,new_row,new_column):
        if seat_type.lower() == "business":
            if (
                self.business_seat[p_row][p_column] == "∎"
                and self.business_seat[new_row][new_column] != "∎"
                ):
                self.business_seat[p_row][p_column] = p_column
                self.business_seat[new_row][new_column] = "∎"




avia_kassa = AviaKassa(economy_seats=[1, 2, 3], business_seats=['A', 'B'])

print()


print("###################### СВОБОДНЫЕ МЕСТА #############################")

# Display the initial seat availability for economy class
avia_kassa.show_availibiity_seat(row=0, column=1, seat_type='economy')


# Display the updated seat availability for business class
avia_kassa.show_availibiity_seat(row=1, column=0, seat_type='business')


print()

print("###################### ПОКУПКА БИЛЕТОВ #############################")

# Buy an economy ticket
avia_kassa.buy_ticket(seat_type='economy', row=0, column=1)
# Buy a business ticket
avia_kassa.buy_ticket(seat_type='business', row=1, column=0)


print()


# Change a business seat
avia_kassa.change_seats(seat_type='business', p_row=1, p_column=0, new_row=1, new_column=1)


print("###################### ИЗМЕНЕННОЕ МЕСТО #############################")

# Display the final seat availability and revenue
avia_kassa.show_availibiity_seat(row=1, column=1, seat_type='business')
print("Место которое поменяли  ")

print()

print("###################### ВЫРУЧКА #############################")

print(f'Total revenue: ${avia_kassa.revenue}')



####################################################################################################################################################################################################
