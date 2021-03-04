class Customer:
    _autoincremented_customer_id = 0

    def __init__(self, name: str, address: str, email: str):
        self.name: str = name
        self.address: str = address
        self.email: str = email
        Customer._autoincremented_customer_id += 1
        self.id = Customer._autoincremented_customer_id

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

    @staticmethod
    def get_next_id():
        return Customer._autoincremented_customer_id + 1
