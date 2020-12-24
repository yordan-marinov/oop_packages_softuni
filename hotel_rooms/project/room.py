class Room:
    def __init__(self, number: int, capacity: int):
        self.number: int = number
        self.capacity: int = capacity
        self.guests: int = 0
        self.is_taken: bool = False

    def can_take_room(self, people: int) -> bool:
        return not self.is_taken and not people > self.capacity

    def can_be_released(self):
        return self.is_taken

    def take_room(self, people):
        if not self.can_take_room(people):
            return f"Room number {self.number} cannot be taken"

        self.is_taken = True
        self.guests = people

    def free_room(self):
        if not self.can_be_released():
            return f"Room number {self.number} is not taken"

        self.is_taken = False
        self.guests = 0
