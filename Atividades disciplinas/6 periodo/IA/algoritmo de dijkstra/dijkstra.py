from path import Path

def small_cost_location(locations):
    locations = [location for location in locations if location.small_path != None]
    location = locations[0]

    for c in locations:
        if c.small_path.cost < location.small_path.cost:
            location = c
    
    return location

class Dijkstra:
    def __init__(self, locations):
        self.locations = locations

    def best_path(self, start_location, end_location):
        self.reset_locations()
        start_location.small_path = Path()

        self.run(start_location)

        if end_location.small_path != None:
            return end_location.small_path

    def run(self, location):
        current_locations = self.locations.copy()

        while current_locations:
            selected_location = small_cost_location(current_locations)
            current_locations.remove(selected_location)
            
            for conection in selected_location.conections:
                path = selected_location.small_path.copy()
                path.add_conection(conection)
                dest_location = conection.dest_location
                dest_location.set_small_path(path)

    def reset_locations(self):
        for location in self.locations:
            location.reset()

            