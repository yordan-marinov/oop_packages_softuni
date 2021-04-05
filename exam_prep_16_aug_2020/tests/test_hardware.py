# from project.system import System
# from project.software.software import Software
# from project.software.light_software import LightSoftware
# from project.software.express_software import ExpressSoftware
# from project.hardware.hardware import Hardware
# from project.hardware.heavy_hardware import HeavyHardware
# from project.hardware.power_hardware import PowerHardware


# System.register_power_hardware("HDD", 200, 200)
# System.register_heavy_hardware("SSD", 400, 400)
# print(System.analyze())
# System.register_light_software("HDD", "Test", 0, 10)
# print(System.register_express_software("HDD", "Test2", 100, 100))
# System.register_express_software("HDD", "Test3", 50, 100)
# System.register_light_software("SSD", "Windows", 20, 50)
# System.register_express_software("SSD", "Linux", 50, 100)
# System.register_light_software("SSD", "Unix", 20, 50)
# print(System.analyze())
# System.release_software_component("SSD", "Linux")
# # print(System.system_split())
from unittest import TestCase, main

from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware


class HardwareTests(TestCase):
    def setUp(self):
        self.h = Hardware("Hardware", "SSD", 100, 100)

    def test_correct_inint(self):
        self.assertEqual("Hardware", self.h.name)
        self.assertEqual("SSD", self.h.type)
        self.assertEqual(100, self.h.capacity)
        self.assertEqual(100, self.h.memory)
        self.assertEqual([], self.h.software_components)

    def test_install_if_valid_should_append_software_components(self):
        self.s = ExpressSoftware("Expres", 100, 50)
        self.h.install(self.s)
        self.assertIn(self.s, self.h.software_components)
    
    def test_install_if_not_valid_memory_consuption_should_raises(self):
        self.s = ExpressSoftware("Expres", 100, 51)
        with self.assertRaises(Exception) as e:
            self.h.install(self.s)

        self.assertEqual("Software cannot be installed", str(e.exception))

    def test_install_if_not_valid_capacity_consuption_should_raises(self):
        self.s = ExpressSoftware("Expres", 101, 50)
        with self.assertRaises(Exception) as e:
            self.h.install(self.s)

        self.assertEqual("Software cannot be installed", str(e.exception))
    
    def test_uninstall_should_remove_software_from_software_components(self):
        self.s = ExpressSoftware("Expres", 100, 50)
        self.h.install(self.s)
        self.h.uninstall(self.s)
        self.assertNotIn(self.s, self.h.software_components)
    

if __name__ == "__main__":
    main()