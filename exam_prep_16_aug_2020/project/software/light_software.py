from project.software.software import Software


class LightSoftware(Software):
    def __init__(self, name, type, capacity_consumption, memory_consumption):
        super().__init__(name, type, capacity_consumption, memory_consumption)
        self.type = "Light"
        self.capacity_consumption *= 1.5
        self.memory_consumption *= 0.5
        
class LightSoftware(Software):
    def __init__(self, name, type, capacity_consumption, memory_consumption):
        super().__init__(name, type, capacity_consumption, memory_consumption)
        self.type = "Light"
        self.capacity_consumption *= 1.5
        self.memory_consumption *= 0.5