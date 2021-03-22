import unittest
from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.r = Room("Marinov", 10.1, 1)

    def test_corect_initialization_all_properties(self):
        self.assertEqual("Marinov", self.r.family_name)
        self.assertEqual(10.1, self.r.budget)
        self.assertEqual(1, self.r.members_count)
        self.assertEqual(0, self.r.expenses)
        self.assertEqual([], self.r.children)

    def test_expenses_getter_raises_value_error_with_negative_value(self):
        with self.assertRaises(ValueError) as contex:
            self.r.expenses = -1
            
        self.assertEqual("Expenses cannot be negative", str(contex.exception))
    

if __name__ == "__main__":
    unittest.main()
