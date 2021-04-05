from project.system import System
from project.software.software import Software
from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware
from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware


def zero_test():
    System.register_power_hardware("HDD", 200, 200)
    System.register_heavy_hardware("SSD", 400, 400)
    print(System.analyze())
    System.register_light_software("HDD", "Test", 0, 10)
    print(System.register_express_software("HDD", "Test2", 100, 100))
    System.register_express_software("HDD", "Test3", 50, 100)
    System.register_light_software("SSD", "Windows", 20, 50)
    System.register_express_software("SSD", "Linux", 50, 100)
    System.register_light_software("SSD", "Unix", 20, 50)
    print(System.analyze())
    System.release_software_component("SSD", "Linux")
    print(System.system_split())

def test_software_init():
    sofrware = Software("ABC", "a", 10, 10)
    print(sofrware.name)
    print(sofrware.type)
    print(sofrware.capacity_consumption)
    print(sofrware.memory_consumption)

def test_light_software_init():
    sofrware = LightSoftware("ABC", "a", 10, 10)
    print(sofrware.name)
    print(sofrware.type)
    print(sofrware.capacity_consumption)
    print(sofrware.memory_consumption)

def test_express_software_init():
    sofrware = ExpressSoftware("ABC", "a", 10, 10)
    print(sofrware.name)
    print(sofrware.type)
    print(sofrware.capacity_consumption)
    print(sofrware.memory_consumption)

def test_hardware_init():
    h = Hardware("ABC", "a", 10, 10)
    print(h.name)
    print(h.type)
    print(h.capacity)
    print(h.memory)
    print(h.software_components)

def test_heavy_hardware_init():
    h = HeavyHardware("ABC", "a", 10, 10)
    print(h.name)
    print(h.type)
    print(h.capacity)
    print(h.memory)
    print(h.software_components)
    
def test_power_hardware_init():
    h = PowerHardware("ABC", "a", 10, 10)
    print(h.name)
    print(h.type)
    print(h.capacity)
    print(h.memory)
    print(h.software_components)
    
def test_system_init():
    s = System()
    print(s._software)
    print(s._hardware)


if __name__ == "__main__":
    zero_test()
    # test_software_init()
    # test_light_software_init()
    # test_express_software_init()
    # test_hardware_init()
    # test_heavy_hardware_init()
    # test_power_hardware_init()
    # test_system_init()
