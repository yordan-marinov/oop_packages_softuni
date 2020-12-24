class Hotel:
    def __init__(self, name: str, ):
        self.name: str = name
        self.rooms: list = []
        self.guests: int = 0

    @classmethod
    def from_stars(cls, stars_count):
        hotel_name = f"{stars_count} stars Hotel"
        return cls(hotel_name)

    def getting_room_by_number(self, room_number):
        return [
            room
            for room in self.rooms
            if room_number == room.number
        ][0]

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        current_room = self.getting_room_by_number(room_number)
        return current_room.take_room(people)

    def free_room(self, room_number):
        current_room = self.getting_room_by_number(room_number)
        return current_room.free_room()

    def print_status(self):
        free_rooms = ", ".join(str(room.number) for room in self.rooms if room.is_taken)
        taken_rooms = ", ".join(str(room.number) for room in self.rooms if not room.is_taken)
        self.guests = sum([room.guests for room in self.rooms])

        print(f"Hotel {self.name} has {self.guests} total guests")
        if free_rooms:
            print(f"Free rooms: {free_rooms}")
        if taken_rooms:
            print(f"Taken rooms: {taken_rooms}")
