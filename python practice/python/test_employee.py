import unittest
from employee import Employee

class RaiseTestCase(unittest.TestCase):
    """test for the raise function"""
    def setUp(self):
        self.new_employee = Employee('migs', 'triaca', 100000)
        

    def test_default_raise(self):
        self.new_employee.give_raise()

        self.assertEqual(105000, self.new_employee.annual_salary)

    def test_custom_amount(self):
        self.new_employee.give_raise(10000)
        self.assertEqual(self.new_employee.annual_salary, 110000)

unittest.main()