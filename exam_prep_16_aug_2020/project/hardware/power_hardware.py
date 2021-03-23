from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name, type: str, capacity: int, memory: int):
        super().__init__(name, type, capacity, memory)
        self.type = "Power"
        self.capacity *= 0.25
        self.memory *= 1.75
