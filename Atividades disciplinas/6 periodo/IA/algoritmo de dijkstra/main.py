from dijkstra import Dijkstra
from location import Location
from map.draw_locations import test_default_map

def test_1():
    location = Location.load_from_json("tests/basic_test.json")
    return location


if __name__ == "__main__":
    
    test_default_map()