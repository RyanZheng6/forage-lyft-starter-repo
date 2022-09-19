from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tiles_arr):
        self.tiles_arr = tiles_arr

    def needs_service(self):
        return sum(self.tiles_arr) >= 3