class Device:
    def __init__(self, device_type, battery_level):
        self.device_type = device_type
        self.battery_level = battery_level

    def get_device_type(self):
        return self.device_type

    def set_device_type(self, device_type):
        self.device_type = device_type

    def get_battery_level(self):
        return self.battery_level

    def set_battery_level(self, battery_level):
        self.battery_level = battery_level
