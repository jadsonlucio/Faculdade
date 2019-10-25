class Conection:
    def __init__(self, location_a, location_b, cost):
        self.start_location = location_a
        self.dest_location = location_b
        self.traveled = False
        self._cost = cost

    @property
    def cost(self):
        return self._cost
