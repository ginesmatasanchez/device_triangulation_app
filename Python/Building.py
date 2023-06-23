class Building:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.floors = []

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_latitude(self):
        return self.latitude

    def set_latitude(self, latitude):
        self.latitude = latitude

    def get_longitude(self):
        return self.longitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def get_floors(self):
        return self.floors

    def set_floors(self, floors):
        self.floors = floors
