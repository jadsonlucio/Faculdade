from .conection import Conection

class Location():
    def __init__(self, name, pos, conetions = []):
        self.small_path = None
        self.location_pos = pos
        self.conetions = conetions
        self.closed = False

    def set_small_path(self, path):
        if not self.small_path:
            self.small_path = path
        elif(self.small_path.cost > path.cost):
            self.small_path = path

    def reset(self):
        self.small_path = None
        self.closed = False

    def add_conection(self, location, cost):
        if location != self:
            self.conetions.append(Conection(self, location, cost))

