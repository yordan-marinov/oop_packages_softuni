class System:
    def __init__(self):
        self._hardware = []
        self._software = []

    @staticmethod
    def register_power_hardware(name:str, capacity:int, memory:int):
        pass

    @staticmethod
    def register_heavy_hardware(name:str, capacity:int, memory:int):
        pass

    @staticmethod
    def register_express_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        pass
    
    @staticmethod
    def register_light_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        pass

    @staticmethod
    def release_software_component(hardware_name:str, software_name:str):
        pass
    
    
    @staticmethod
    def analyze():
        pass
    
    @staticmethod
    def system_split():
        pass