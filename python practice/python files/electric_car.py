"""classes for electric car"""

from car import Car

class Battery():
    """models a battery for an electric car"""
    def __init__(self, battery_size=60):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f'this car has a {self.battery_size} -kwh battery!')
    
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size >70:
            range = 300
        else:
            range = 180
    
        print(f'this car can go approximately {range} miles')

class ElectricCar(Car):
    """car class specific for eletric cars"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
