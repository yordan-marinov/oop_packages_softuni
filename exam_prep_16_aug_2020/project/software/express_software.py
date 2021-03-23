from project.software.software import Software


class ExpressSoftware(Software):
    def __init__(self, name, type_software, capacity_consumption, memory_consumption):
        super().__init__(name, type, capacity_consumption, memory_consumption)
        self.type = "Express"
        self.memory_consumption *= 2