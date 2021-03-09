from project.animal import Animal
from project.reptile import Reptile
from project.lizard import Lizard
from project.snake import Snake
from project.mammal import Mammal
from project.gorilla import Gorilla
from project.bear import Bear

import unittest


class Tests(unittest.TestCase):
   def test(self):
       mammal = Mammal("Stella")
       self.assertEqual(mammal.__class__.__bases__[0].__name__, "Animal")
       self.assertEqual(mammal.name, "Stella")
       self.assertEqual(mammal._Animal__name, "Stella")
       lizard = Lizard("John")
       self.assertEqual(lizard.__class__.__bases__[0].__name__, "Reptile")
       self.assertEqual(lizard .name, "John")
       self.assertEqual(lizard ._Animal__name, "John")



if __name__ == "__main__":
   unittest.main()
    
    # mammal = Mammal("Stella")
    # print(mammal.__class__.__bases__[0].__name__)
    # print(mammal.name)
    # print(mammal._Animal__name)
    # lizard = Lizard("John")
    # print(lizard.__class__.__bases__[0].__name__)
    # print(lizard.name)
    # print(lizard._Animal__name)
