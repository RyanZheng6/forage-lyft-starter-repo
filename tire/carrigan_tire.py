from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tiles_arr):
        self.tiles_arr = tiles_arr

    def needs_service(self):
        return max(self.tiles_arr) >= 0.9