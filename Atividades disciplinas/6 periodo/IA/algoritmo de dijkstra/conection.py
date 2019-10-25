class Conection:
    def __init__(self, city_a, city_b, cost):
        self.start_city = city_a
        self.dest_city = city_b
        self.traveled = False
        self._cost = cost

        self.start_city.conetions.append(self)


    def cost():
        return self._cost
