# from car import Car

# my_new_car = Car('audi', 'a4',2016)
# print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

#importing more than one module
# from car import ElectricCar, Car

# my_tesla = ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

# my_car = Car('toyota', 'corola', 2009)
# print(my_car.get_descriptive_name())

#importing entire module, using dot notation
# import car

# my_car = car.Car('toyota', 'camry', 2009)
# my_tesla = car.ElectricCar('tesla', 'roadster', 2017)
# print(my_car.get_descriptive_name())
# print(my_tesla.get_descriptive_name())

#importing from 2 separate files
from car import Car
from electric_car import ElectricCar

my_car = Car('toyota', 'camry', 2009)
print(my_car.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2017)
print(my_tesla.get_descriptive_name())
