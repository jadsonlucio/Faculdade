from .conection import Conection

class City():
    def __init__(self, name, pos, conetions):
        self.small_path = None
        self.city_pos = pos
        self.conetions = []
        self.closed = False

    def add_conection(self, city, cost):
        if city != self:
            self.conetions.append(Conection(self, city, cost))
