import unittest
from july23 import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Test for fname formatter"""
    def test_first_last_name(self):
        formatted_name = get_formatted_name('migs', 'triaca')
        self.assertEqual(formatted_name, 'Migs Triaca')
        
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('migs', 'triaca','beast')
        self.assertEqual(formatted_name, 'Migs Beast Triaca')

unittest.main()