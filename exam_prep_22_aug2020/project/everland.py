from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms: [Room()] = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        result = 0
        for room in self.rooms:
            result += room.expenses
            result += room.room_cost
        return f"Monthly consumtion: {result:.2f}$."

    def pay(self):
        result = []
        rooms_to_remove = []
        for room in self.rooms:
            total_room_cost = room.expenses + room.room_cost
            if room.budget >= total_room_cost:
                result.append(f"{room.family_name} paid {total_room_cost:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                rooms_to_remove.append(room)
        for room in self.rooms:
            if room in rooms_to_remove:
                self.rooms.remove(room)
                
        return "\n".join(result)

    def status(self):
        s = ""
        all_people_in_the_hotel = sum(r.members_count for r in self.rooms)
        s += f"Total population: {all_people_in_the_hotel}\n"
        for room in self.rooms:
            current_budget = room.budget - room.expenses - room.room_cost
            s += f"{room.family_name} with {room.members_count} members. Budget: {current_budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            total_children_expenses = 0
            for index, child in enumerate(room.children, 1):
                total_children_expenses += child.get_monthly_expense()
                s += f"--- Child {index} monthly cost: {child.get_monthly_expense():.2f}$\n"
            cost_of_all_appliances_for_one_month = room.expenses - total_children_expenses
            s += f"--- Appliances monthly cost: {cost_of_all_appliances_for_one_month:.2f}$\n"
            result = s.rstrip()
        return result