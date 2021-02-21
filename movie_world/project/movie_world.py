from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name: str = name
        self.customers: [Customer] = []
        self.dvds: [DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd_obj = [d for d in self.dvds if d.id == dvd_id][0]
        customer_obj = [c for c in self.customers if c.id == customer_id][0]
        
        if dvd_obj in customer_obj.rented_dvds:
            return f"{customer_obj.name} has already rented {dvd_obj.name}"

        if customer_obj.age < dvd_obj.age_restriction:
            return f"{customer_obj.name} should be at least {dvd_obj.age_restriction} to rent this movie"

        if dvd_obj.is_rented:
            return f"DVD is already rented"

        dvd_obj.is_rented = not dvd_obj.is_rented
        customer_obj.rented_dvds.append(dvd_obj)
        
        return f"{customer_obj.name} has successfully rented {dvd_obj.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer_obj = [c for c in self.customers if c.id == customer_id][0]
        dvd_obj = [d for d in self.dvds if d.id == dvd_id][0]
        
        if dvd_obj in customer_obj.rented_dvds:
            dvd_obj.is_rented = False
            customer_obj.rented_dvds.remove(dvd_obj)
            return f"{customer_obj.name} has successfully returned {dvd_obj.name}"
        
        return f"{customer_obj.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += f"{customer}\n"
        for dvd in self.dvds:
            result += f"{dvd}\n"
        
        return result
