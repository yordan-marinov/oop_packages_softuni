class Survivor:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age
        self.health: int = 100
        self.needs: int = 100

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not new_name:
            raise ValueError("Name not valid!")
        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise ValueError("Age not valid!")
        self.__age = new_age
        
    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, new_health):
        if new_health < 0:
            raise ValueError("Health not valid!")
        elif new_health > 100:
            new_health = 100
        self.__health = new_health
        
    @property
    def needs(self):
        return self.__needs

    @needs.setter
    def needs(self, new_needs):
        if new_needs < 0:
            raise ValueError("Needs not valid!")
        elif new_needs > 100:
            new_needs = 100
        self.__needs = new_needs
        
    @property
    def needs_sustenance(self):
        if self.needs < 100:
            return True
        return False
        
    @property
    def needs_healing(self):
        if self.health < 100:
            return True
        return False