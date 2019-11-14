import numpy as np
from map.location import Location, calc_distance
from map.map import Map

COORDINATES_MAP_TEST_1 = {
    "latitude_min" : 0,
    "latitude_max" : 10,
    "longitude_min" : 0,
    "longitude_max" : 10
}

CIDADES_ALAGOAS = list(open("tests/cidades_alagoas.txt", "r").readlines())[:10]

def generate_random_sample(locations_names, latitude_min, latitude_max, 
                        longitude_min, longitude_max):
    locations = []
    for location_name in locations_names:
        latitude = np.random.uniform(latitude_min + 1, latitude_max - 1)
        longitude = np.random.uniform(longitude_min + 1, longitude_max - 1)
        locations.append(Location(location_name, latitude,longitude))
    
    for i in range(len(locations)):
        for j in range(i + 1, len(locations), 1):
            if np.random.random() > 0.7:
                cost = calc_distance(*locations[i].real_pos, *locations[j].real_pos)
                locations[i].add_conection(locations[j], cost)  

    return locations

def get_map_test_1():
    locations = generate_random_sample(CIDADES_ALAGOAS, **COORDINATES_MAP_TEST_1)

    return Map(locations, **COORDINATES_MAP_TEST_1)