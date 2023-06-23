class Point:
    def __init__(self, x, y, z, device):
        self.x = x
        self.y = y
        self.z = z
        self.device = device

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_z(self):
        return self.z

    def set_z(self, z):
        self.z = z

    def get_device(self):
        return self.device

    def set_device(self, device):
        self.device = device



