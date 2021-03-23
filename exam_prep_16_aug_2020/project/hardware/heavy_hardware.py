from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name, type: str, capacity: int, memory: int):
        super().__init__(name, type, capacity, memory)
        self.type = "Heavy"
        self.capacity *= 2
        self.memory *= 0.75
