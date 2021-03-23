from project.software.software import Software


class Hardware:
    def __init__(self, name, type_hardware: str, capacity: int, memory: int):
        self.name: str = name
        self.type: str = type_hardware
        self.capacity: int = capacity
        self.memory: int = memory
        self.software_components = []

        
    def install(self, software: Software):
        if self.memory < software.memory_consumption:
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    
    def uninstall(self, software: Software):
        pass