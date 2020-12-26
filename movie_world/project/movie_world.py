class MovieWorld:
    def __init__(self, name: str):
        self.name: str = name
        self.customers = []  # list of Customers obj.
        self.dvds = []  # list of DVDs obj.

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):  # customer: Customer(obj)
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = self.get_customer_by_id(customer_id)
        dvd = self.get_dvd_by_id(dvd_id)
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least " \
                   f"{dvd.age_restriction} to rent this movie"

        if dvd.is_rented:
            return f"DVD is already rented"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = not dvd.is_rented

        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.get_customer_by_id(customer_id)
        dvd = self.get_dvd_by_id(dvd_id)

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = not dvd.is_rented
            return f"{customer.name} has successfully returned {dvd.name}"

        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += customer.__repr__() + "\n"
        for dvd in self.dvds:
            result += dvd.__repr__() + "\n"

        return result

    def get_customer_by_id(self, customer_id):
        customer = [
            customer
            for customer in self.customers
            if customer.id == customer_id
        ][0]
        return customer

    def get_dvd_by_id(self, dvd_id):
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
        return dvd
