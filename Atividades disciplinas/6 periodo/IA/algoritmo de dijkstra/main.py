from dijkstra import Dijkstra
from location import Location

def build_road_struct(locations, road_matrix):
    for ind_location, location in enumerate(locations):
        for ind_dest_location, cost in enumerate(road_matrix[ind_location]):
            if cost != 0:
                location.add_conection(locations[ind_dest_location], cost)

def test_1():
    locations = [["a", (0,0)], ["b", (1,1)], ["c", (0,1)], ["d", (1,0)]]
    locations = [Location(*c) for c in locations]
    print(locations[1].conections)
    road_matrix = [[0, 1, 0, 3], [0, 0, 3, 2], [1, 1, 0, 0], [0, 0, 1, 0]]
    build_road_struct(locations, road_matrix)
    obj = Dijkstra(locations)
    print(obj.best_path(locations[0], locations[2]))


if __name__ == "__main__":
    test_1()