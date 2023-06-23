class Zone:
    def __init__(self, name, triangle_position):
        self.name = name
        self.triangle_position = triangle_position

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_triangle_position(self):
        return self.triangle_position

    def set_triangle_position(self, triangle_position):
        self.triangle_position = triangle_position
