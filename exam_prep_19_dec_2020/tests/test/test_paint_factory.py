from project.factory.paint_factory import PaintFactory
from project.factory.factory import Factory

from unittest import TestCase, main


class TestsPaintFactory(TestCase):
    name = "pain"
    capacity = 10
    valid_ingredients = ["white", "yellow", "blue", "green", "red"]
    
    def setUp(self):
        self.pf = PaintFactory(self.name ,self.capacity)

    def test_correct_init(self): 
        self.assertEqual(self.name, self.pf.name)
        self.assertEqual(self.capacity, self.pf.capacity)
        self.assertEqual(self.valid_ingredients, self.pf.valid_ingredients)
        self.assertEqual({}, self.pf.ingredients)
        self.assertEqual({}, self.pf.products)

    def test_products_property(self):
        self.assertEqual({}, self.pf.products)
        
    def test_add_ingredient_if_ingredient_not_in_valid_types_raises(self):
        with self.assertRaises(TypeError) as contex:
            self.pf.add_ingredient("black", 1)
        self.assertEqual("Ingredient of type black not allowed in PaintFactory", str(contex.exception))

    def test_add_ingredient_if_quantity_is_bigger_than_capacity_raises(self):
        with self.assertRaises(ValueError) as contex:
            self.pf.add_ingredient("blue", 11)
        self.assertEqual("Not enough space in factory", str(contex.exception))

    def test_add_ingredient_if_ingredient_in_valid_types_but_not_in_self_ingredients(self):
        self.assertEqual({}, self.pf.ingredients)
        self.pf.add_ingredient("blue", 1)
        self.assertEqual({"blue": 1}, self.pf.ingredients)
        
    def test_add_ingredient_if_ingredient_in_valid_types_but_in_self_ingredients(self):    
        self.pf.add_ingredient("blue", 1)
        self.pf.add_ingredient("blue", 1)
        self.assertEqual({"blue": 2}, self.pf.ingredients)
    
    def test_remove_ingredient_if_ingredient_not_in_ingredients_raises(self):
        with self.assertRaises(KeyError) as contex:
            self.pf.remove_ingredient("green", 1)
        self.assertEqual("'No such product in the factory'", str(contex.exception))
    
    def test_remove_ingredient_if_ingredient_quantity_is_less_than_given_raises(self):
        self.pf.add_ingredient("blue", 1)
        with self.assertRaises(ValueError) as contex:
            self.pf.remove_ingredient("blue", 2)
        self.assertEqual("Ingredient quantity cannot be less than zero", str(contex.exception))
    
    def test_correct_deduction_from_ingredient_quantity(self):
        self.pf.add_ingredient("blue", 2)
        self.pf.remove_ingredient("blue", 1)
        self.assertEqual({"blue": 1}, self.pf.ingredients)

    def test_can_add_if_capacity_is_bigger_or_equal_than_sum_of_all_ingredients_values_returns_true(self):
        self.pf.add_ingredient("blue", 9)
        self.assertTrue(self.pf.can_add(1))
        

if __name__ == "__main__":
    main()