import json

from dijkstra import Dijkstra
from map.location import Location, calc_distance

class Map():
    def __init__(self, locations, latitude_min, latitude_max, 
                                longitude_min, longitude_max):
        
        center_latitude = latitude_min + (latitude_max - latitude_min) // 2
        center_longitude = longitude_min + (longitude_max - longitude_min) // 2
        self.top_left_location = Location("top_left", latitude_min, longitude_min)
        self.bottom_right_location = Location("bottom_right", latitude_max, longitude_max)
        self.center_location = Location("center", center_latitude, center_longitude)
        
        self.width = calc_distance(latitude_min, center_longitude, latitude_max, center_longitude)
        self.height = calc_distance(center_latitude, longitude_min, center_latitude, longitude_max)

        self.locations = locations
        self.dijkstra = Dijkstra(self.locations)
        self.selected_citys = []
        self.road_paths = []

    def run_dijkstra_algoritm(self):
        self.road_paths = []
        if len(self.selected_citys) > 1:
            for i in range(0,len(self.selected_citys) - 1, 1):
                self.road_paths.append(self.dijkstra.best_path(self.selected_citys[i], self.selected_citys[i+1]))
            for path in self.road_paths:
                for conection in path.conections:
                    conection.traveled = True

    
    @classmethod
    def load_from_json(self, json_path):
        with open(json_path, "r") as f:
            map_json = json.load(f)
            locations_name, locations_pos = map_json["locations"], map_json["positions"]
            road_matrix = map_json["road_matrix"]

            locations = Location.build_locations(locations_name, locations_pos, road_matrix)

            return Map(locations, **map_json["coordinates"])
