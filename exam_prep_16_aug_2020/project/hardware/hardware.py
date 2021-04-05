from project.software.software import Software


class Hardware:
    def __init__(self, name, type: str, capacity: int, memory: int):
        self.name: str = name
        self.type: str = type
        self.capacity: int = capacity
        self.memory: int = memory
        self.software_components: [Software] = []

    @property
    def used_memory(self):
        return sum(c.memory_consumption for c in self.software_components)

    @property
    def used_capacity(self):
         return sum(c.capacity_consumption for c in self.software_components)
    
    def is_valid_to_install(self, obj):
        return (
            obj.memory_consumption <= self.memory - self.used_memory
            and obj.capacity_consumption <= self.capacity - self.used_capacity
        )

    def install(self, software: Software):
        if not self.is_valid_to_install(software):
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)