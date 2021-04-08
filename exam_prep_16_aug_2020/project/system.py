from project.software.software import Software
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware


class System:
    _hardware: [Hardware] = []
    _software: [Software] = []

    @classmethod
    def hardware_names(cls):
        return [h.name for h in cls._hardware]

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        ph = PowerHardware(name, capacity, memory)
        System._hardware.append(ph)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hh = HeavyHardware(name, capacity, memory)
        System._hardware.append(hh)

    @staticmethod
    def register_light_software(
        hardware_name: str,
        name: str,
        capacity_consumption: int,
        memory_consumption: int,
    ):
        try:
            hardware = [h for h in System._hardware if hardware_name == h.name][0]
            ls = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(ls)
        except IndexError:
            return "Hardware does not exist"
        except Exception as e:
            return str(e)
        else:
            System._software.append(ls)

    @staticmethod
    def register_express_software(
        hardware_name: str,
        name: str,
        capacity_consumption: int,
        memory_consumption: int,
    ):
        try:
            hardware = [h for h in System._hardware if hardware_name == h.name][0]
            es = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(es)
            
        except IndexError:
            return f"Hardware does not exist"

        except Exception as e:
            return str(e)

        else:
            System._software.append(es)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
        except IndexError:
            return "Some of the components do not exist"
        else:
            hardware.uninstall(software)
            System._software.remove(software)

    @staticmethod
    def analyze():
        result = f"System Analysis\n"
        result += f"Hardware Components: {len(System._hardware)}\n"
        result += f"Software Components: {len(System._software)}\n"
        result += f"Total Operational Memory: {sum(h.used_memory for h in System._hardware)} / {sum(h.memory for h in System._hardware)}\n"
        result += f"Total Capacity Taken: {sum(h.used_capacity for h in System._hardware)} / {sum(h.capacity for h in System._hardware)}"
        return result

    @staticmethod
    def system_split():
        pass
