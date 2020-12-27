class Customer:
    auto_id_numbers_creator = 1

    def __init__(self, name: str, address: str, email: str):
        self.name: str = name
        self.address: str = address
        self.email: str = email
        self.id: int = Customer.auto_id_numbers_creator
        Customer.auto_id_numbers_creator += 1

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; " \
               f"Address: {self.address}; " \
               f"Email: {self.email}"

    @staticmethod
    def get_next_id():
        return Customer.auto_id_numbers_creator

# customer = Customer("John", "Maple Street", "john.smith@gmail.com")
# print(customer)
# customer2 = Customer("Johny", "Apple Street", "johny.s@gmail.co.uk")
# print(customer2)
