class Equipment:
    auto_equipment_id_creator = 1

    def __init__(self, name: str):
        self.name: str = name
        self.id: int = Equipment.auto_equipment_id_creator
        Equipment.auto_equipment_id_creator += 1

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment.auto_equipment_id_creator


# equipment = Equipment("Treadmill")
# print(equipment.__dict__)
# equipment2 = Equipment("Rope")
# print(equipment2)
# print(Equipment.get_next_id())
