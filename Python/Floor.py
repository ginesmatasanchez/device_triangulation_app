class Floor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.zones = []

    def get_floor_number(self):
        return self.floor_number

    def set_floor_number(self, floor_number):
        self.floor_number = floor_number

    def get_zones(self):
        return self.zones

    def set_zones(self, zones):
        self.zones = zones

    def add_zone(self, zone):
        self.zones.append(zone)
        
    def remove_zone(self, zone):
        self.zones.remove(zone)
