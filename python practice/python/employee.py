class Employee():
    """class that has info on employees"""

    def __init__(self, first, last, annual_salary):
        self.first = first
        self.last = last
        self.annual_salary = annual_salary
    
    def give_raise(self, amount=5000):
        """method adds to the annual salary"""
        self.annual_salary += amount
    
