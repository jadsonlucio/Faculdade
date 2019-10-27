import json
import numpy as np

from map.conection import Conection

from math import sin, cos, sqrt, atan2, radians

def calc_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    km = 6371 * c
    return km

def build_road_struct(locations, road_matrix):
    for ind_location, location in enumerate(locations):
        for ind_dest_location, conected in enumerate(road_matrix[ind_location]):
            if conected:
                cost = calc_distance(*location.real_pos, *locations[ind_dest_location].real_pos)
                location.add_conection(locations[ind_dest_location], cost)


class Location():
    def __init__(self, name, latitude, longitude, conections = []):
        self.name = name
        self._latitude = latitude
        self._longitude = longitude

        self.small_path = None
        self.conections = conections.copy()
        self.closed = False

        self._virtual_pos = None

    def set_small_path(self, path):
        if not self.small_path:
            self.small_path = path
        elif(self.small_path.cost > path.cost):
            self.small_path = path

    def reset(self):
        self.small_path = None
        self.closed = False

        for conection in self.conections:
            conection.traveled = False

    def add_conection(self, location, cost, dual_road = True):
        if location != self:
            if dual_road:
                location.conections.append(Conection(location, self, cost))
                self.conections.append(Conection(self, location, cost))

    def relative_x_y_coor(self, location):
        latitude, longitude = location.real_pos
        x = calc_distance(latitude, longitude, self.real_pos[0], longitude)
        y = calc_distance(latitude, longitude, latitude, self.real_pos[1])

        return x,y
    
    def distance(self, location):
        return calc_distance(*self.pos, *location.pos)
    
    @property
    def virtual_pos(self):
        return int(self._virtual_pos[0]), int(self._virtual_pos[1])

    @property
    def real_pos(self):
        return self._latitude, self._longitude

    @classmethod
    def build_locations(cls, locations_name, locations_pos, road_matrix):
        locations = []
        for name, pos in zip(locations_name, locations_pos):
            latitude, longitude = pos
            locations.append(Location(name, latitude, longitude))
        
        build_road_struct(locations, road_matrix)

        return locations

