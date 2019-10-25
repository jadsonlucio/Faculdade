class Dijktra:
    def __init__(self, citys, start_city, end_city):
        pass


    def run(self, city, path):
        for conection in city.conections:
            if not conection.traveled:
                conection.traveled = True
                path_copy = path.__copy__()
                path_copy.append()
                if conection.dest_city.small_path()


def run(city, visited_citys = [], path = []):
    visited_citys.append(city)
    path.append(city)
    for conection in city.conections:
        if conection.end_city.
            