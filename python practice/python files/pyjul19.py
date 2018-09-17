# class Dog():
#     """model a dog"""

#     def __init__(self, name, age):
#         """initialize name and age attributes"""
#         self.name = name
#         self.age = age

#     def sit(self):
#         """simulate dog sitting"""
#         print(f'{self.name.title()} is now sitting!')
    
#     def roll_over(self):
#         """simulate roll over"""
#         print(f'{self.name.title()} rolled over!!')

# my_dog = Dog('gibbs', 7)
# my_other_dog = Dog('ducky', 7)
# print(f'My dog\'s name is {my_dog.name.title()} and he is {my_dog.age} years old')
# print(f'My other dog\'s name is {my_other_dog.name.title()} and he is {my_other_dog.age} years old')

# my_dog.sit()
# my_dog.roll_over()

# my_other_dog.sit()
# my_other_dog.roll_over()

# class Car():
#     """class that represents a car"""

#     def __init__(self, make, model, year):
#         """initialize car """
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0 
    
#     def get_descriptive_name(self):
#         """return a descriptive name"""
#         long_name = f'{self.year} {self.make} {self.model}'
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f'this car has {self.odometer_reading} miles on it')

# new_car = Car('toyota', 'camry', 2009)
# print(new_car.get_descriptive_name())

# #directly update a value
# new_car.odometer_reading = 25
# new_car.read_odometer()

#method for update
# class Car():
#     """class that represents a car"""

#     def __init__(self, make, model, year):
#         """initialize car """
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0 
    
#     def get_descriptive_name(self):
#         """return a descriptive name"""
#         long_name = f'{self.year} {self.make} {self.model}'
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f'this car has {self.odometer_reading} miles on it')

#     def update_odometer(self, mileage):
#         """set odometer reading for a car, Reject rolling back of measurements"""

#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print('You cant roll back an odometer!')

#     def increment_odometer(self, miles):
#         if miles < 0:
#             print('Cant increment by negative!')
#         else:
#             self.odometer_reading += miles

# new_car = Car('toyota', 'camry', 2009)
# print(new_car.get_descriptive_name())
# new_car.update_odometer(100)
# new_car.read_odometer()
# new_car.increment_odometer(-25)
# new_car.read_odometer()

# class Restaurant():
#     def __init__(self, name, cuisine_type):
#         self.name = name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         print(f'The restaurant\'s name is {self.name.title()} and the food type is {self.cuisine_type} and has served {self.number_served} customers!')
    
#     def open_restaurant(self):
#         print(f'{self.name.title()} is now open!')
    
#     def set_number_served(self, served):
#         self.number_served = served

#     def increment_numer_served(self, add_served):
#         self.number_served += add_served

# first_restaurant = Restaurant('hello','filipino')
# first_restaurant.describe_restaurant()
# first_restaurant.open_restaurant()
# first_restaurant.set_number_served(25)
# first_restaurant.increment_numer_served(30)
# first_restaurant.describe_restaurant()

#inheritance from another class

# class Restaurant():
#     """class for a restaurant"""
#     def __init__(self, name, cuisine_type):
#         self.name = name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         print(f'The restaurant\'s name is {self.name.title()} and the food type is {self.cuisine_type} and has served {self.number_served} customers!')
    
#     def open_restaurant(self):
#         print(f'{self.name.title()} is now open!')
    
#     def set_number_served(self, served):
#         self.number_served = served

#     def increment_numer_served(self, add_served):
#         self.number_served += add_served

# class FoodTruck(Restaurant):
#     """Stuff for foodtruck"""
#     def __init__(self, name, cuisine_type):
#         super().__init__(name, cuisine_type)
#         self.battery_size = 25
    
#     def describe_battery(self):
#         """this describes battery size"""
#         print(f'This car has a {self.battery_size} kwh battery for the truck')
#     #you can OVVERRIDE A method from the parent class by creating one with the same name for the child class
# my_truck = FoodTruck('taco tuesday', 'korean')
# print(my_truck.describe_restaurant())
# my_truck.describe_battery()

# class Car():
#     """represent a car"""

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
    
#     def get_descriptive_name(self):
#         """return a descriptive name"""
#         long_name = f'{self.year} {self.make} {self.model}'
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f'this car has {self.odometer_reading} miles on it')

#     def update_odometer(self, mileage):
#         """set odometer reading for a car, Reject rolling back of measurements"""

#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print('You cant roll back an odometer!')

#     def increment_odometer(self, miles):
#         if miles < 0:
#             print('Cant increment by negative!')
#         else:
#             self.odometer_reading += miles


# class ElectricCar(Car):
#     """car that is specifically electric"""
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery_size = 70
    
#     def describe_battery(self):
#         print(f'This car has a {self.battery_size} -kwh battery')

# my_tesla = ElectricCar('tesla', 'model s', 2017)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()

#instances as attributes
# class Car():
#     """represent a car"""

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
    
#     def get_descriptive_name(self):
#         """return a descriptive name"""
#         long_name = f'{self.year} {self.make} {self.model}'
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f'this car has {self.odometer_reading} miles on it')

#     def update_odometer(self, mileage):
#         """set odometer reading for a car, Reject rolling back of measurements"""

#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print('You cant roll back an odometer!')

#     def increment_odometer(self, miles):
#         if miles < 0:
#             print('Cant increment by negative!')
#         else:
#             self.odometer_reading += miles

# class Battery():
#     """simple class to describe a battery"""
#     def __init__(self, battery_size=70):
#         self.battery_size = battery_size

#     def describe_battery(self):
#         print(f'This car has a {self.battery_size} -kwh battery')

#     def get_range(self):
#         if self.battery_size >= 75:
#             range = 300
#         else:
#             range = 100
#         range_message = f'this car can go {range} miles on a charge!'
#         print(range_message)

# class ElectricCar(Car):
#     """car that is specifically electric"""
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()
    
# my_tesla = ElectricCar('tesla', 'model s', 2017)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.battery_size = 14
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

# class Restaurant():
#     """class for a restaurant"""
#     def __init__(self, name, cuisine_type):
#         self.name = name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         print(f'The restaurant\'s name is {self.name.title()} and the food type is {self.cuisine_type} and has served {self.number_served} customers!')
    
#     def open_restaurant(self):
#         print(f'{self.name.title()} is now open!')
    
#     def set_number_served(self, served):
#         self.number_served = served

#     def increment_numer_served(self, add_served):
#         self.number_served += add_served

# class IceCreamStand(Restaurant):
#     """specifically ice cream stand"""
#     def __init__(self, name, cuisine_type):
#         super().__init__(name, cuisine_type='ice cream')
#         self.flavors = []

#     def add_flavor(self, *flavor):
#         for flav in flavor:
#             self.flavors.append(flav)
    
#     def display_flavors(self):
#         print('flavors available: ')
#         for flavor in self.flavors:
#             print(flavor)

# new_icecream = IceCreamStand('best cream', 'ice cream')
# new_icecream.add_flavor('chocolate', 'vanilla', 'cookies and cream')
# new_icecream.display_flavors()