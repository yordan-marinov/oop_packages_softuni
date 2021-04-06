class Person:
    min_age = 16
    max_age = 80
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def __validate_age(cls, age):
        return cls.min_age <= age < cls.max_age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if self.__validate_age(new_age):
            self.__age = new_age

    def say_hello(self):
        return f"Hello my name is {self.name} and I' {self.age} years old."


class Employee(Person):
    min_age = 18
    
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 100:
            raise ValueError("Salary is too low")
        self.__salary = new_salary

    def say_hello(self):
        return super().say_hello() + f" And my salary is {self.salary}."



e = Employee("Jordan", 18, 110)
print(e.__dict__)
# print(Employee.__dict__)
# print(help(e))
# print(e.age)
# print(e.age)
print(e.salary)
# print(e.say_hello())

p = Person("Martin", 17)
print(p.__dict__)
