from zoo.project.animal import Animal
from zoo.project.bear import Bear
from zoo.project.gorilla import Gorilla
from zoo.project.lizard import Lizard
from zoo.project.mammal import Mammal
from zoo.project.reptile import Reptile
from zoo.project.snake import Snake


if __name__ == '__main__':
    mammal = Mammal("Stella")
    print(mammal.__class__.__bases__[0].__name__)
    print(mammal.name)
    print(mammal._Animal__name)
    lizard = Lizard("John")
    print(lizard.__class__.__bases__[0].__name__)
    print(lizard.name)
    print(lizard._Animal__name)