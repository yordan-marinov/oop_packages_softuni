from project.software.software import Software
from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware
from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware


class System:
    _hardware = []
    _software = []
    
    @staticmethod
    def register_power_hardware(name:str, capacity:int, memory:int):
        ph = PowerHardware(name, capacity, memory)
        System._hardware.append(ph)

    @staticmethod
    def register_heavy_hardware(name:str, capacity:int, memory:int):
        hh = HeavyHardware(name, capacity, memory)
        System._hardware.append(hh)

    @classmethod
    def get_hardware_exist(cls, hardware_name):
        obj =  [h for h in cls._hardware if h.name == hardware_name]
        if obj: 
            return obj[0]
    
    
    @staticmethod
    def register_express_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        hardware = System.get_hardware_exist(hardware_name)
        if not hardware:
            return "Hardware does not exist"
        es = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(es)
            System._software.append(es)
        except Exception as e:
            return str(e)

    
    @staticmethod
    def register_light_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        hardware = System.get_hardware_exist(hardware_name)
        if not hardware:
            return "Hardware does not exist"
        ls = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(ls)
            System._software.append(ls)
        except Exception as e:
            return str(e)


    @staticmethod
    def release_software_component(hardware_name:str, software_name:str):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        software = [s for s in System._software if s.name == software_name]
        if not (hardware and software):
            return "Some of the components do not exist"
        hardware[0].uninstall(software[0])
        System._software.remove(software[0])
        
    
    @staticmethod
    def analyze():
        res = f"System Analysis\n"
        res += f"Hardware Components: {len(System._hardware)}\n"
        res += f"Software Components: {len(System._software)}\n"
        res += f"Total Operational Memory: {sum(c.memory_consumption for c in System._software)} / {sum(c.memory for c in System._hardware)}\n"
        res += f"Total Capacity Taken: {sum(c.capacity_consumption for c in System._software)} / {sum(c.capacity for c in System._hardware)}"
        return res
    
    @staticmethod
    def system_split():
        pass