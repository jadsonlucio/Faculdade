import json
import numpy as np

from conection import Conection

from math import cos, sin, asin, sqrt, radians

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
    a = sin(dlat / 2) * 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) * 2
    c = 2 * asin(sqrt(a))
    km = 6371 * c
    return km

def calc_x_y_points(lat, lon, center_lat = 0, center_lon = 0):
    x = calc_distance(center_lat, center_lon, center_lat, lon)
    y = calc_distance(center_lat, center_lon, lat, center_lon)

    return x,y

def dist(coor_1, coor_2):
    return sum((np.array(coor_1) - np.array(coor_2))**2) ** 0.5

def build_road_struct(locations, road_matrix):
    for ind_location, location in enumerate(locations):
        for ind_dest_location, conected in enumerate(road_matrix[ind_location]):
            if conected:
                cost = calc_distance(*location.pos, *locations[ind_dest_location].pos)
                location.add_conection(locations[ind_dest_location], cost)


class Location():
    def __init__(self, name, pos, conections = []):
        self.name = name
        self.pos = pos
        self.small_path = None
        self.location_pos = pos
        self.conections = conections.copy()
        self.closed = False

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

    def get_x_y_coor(self, center_lat, center_lon):
        return calc_x_y_points(self.pos[0], self.pos[1], center_lat, center_lon)

    @classmethod
    def load_from_json(cls, json_path):
        with open(json_path, "r") as f:
            locations_json = json.load(f)
            locations = []
            for name, pos in zip(locations_json["locations"], locations_json["positions"]):
                locations.append(Location(name, pos))
            
            build_road_struct(locations, locations_json["road_matrix"])

            return locations



