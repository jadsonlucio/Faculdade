from .dijkstra import Dijkstra
from .location import Location

def build_road_struct(locations, road_matrix):
    for ind_location, location in enumerate(locations):
        for ind_dest_location, cost in road_matrix[ind_location]:
            if cost != 0:
                location.add_conection(locations[ind_dest_location], cost)

def test_1():
    locations = [["a", (0,0)], ["b", (1,1)], ["c", (0,1)], ["d", (1,0)]]
    locations = [Location(*c) for c in locations]
    road_matrix = [[1, 0, 2, 3], [0, 0, 2, 2], [1, 1, 0, 0], [0, 0, 1, 0]]
    build_road_struct(locations, road_matrix)
    obj = Dijkstra(locations)


if __name__ == "__main__":
    test_1()