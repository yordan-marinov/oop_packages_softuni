from project.animal import Animal
from project.dog import Dog
from project.cat import Cat
from project.kitten import Kitten
from project.tomcat import Tomcat


if __name__ == "__main__":
    dog = Dog("Sharo", 4, "Male")
    print(dog)
    print(dog.make_sound())
    cat = Cat("Tom", 3, "Male")
    print(cat)
    print(cat.make_sound())
    kitten = Kitten("Kity", 2)
    print(kitten.gender)
    print(kitten.make_sound())
    tomcat = Tomcat("Tomas", 1,)
    print(tomcat)
    print(tomcat.make_sound())