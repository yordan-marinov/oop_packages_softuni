class Equipment:
    _autoincremented_equipment_id = 0

    def __init__(self, name: str):
        self.name: str = name
        Equipment._autoincremented_equipment_id += 1
        self.id = Equipment._autoincremented_equipment_id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment._autoincremented_equipment_id + 1
