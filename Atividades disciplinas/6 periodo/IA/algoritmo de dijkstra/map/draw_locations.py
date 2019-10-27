import pygame
import numpy as np

from dijkstra import Dijkstra
from location import Location
from map.text import PyGameText

# map constants 
CITY_SIMBOL_SIZE = 10

# color constants
BLACK = ( 0, 0, 0)
WHITE = (254, 254, 254)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
BLUE = (0, 0, 255)
CITY_COLOR_1 = (64, 235, 52)
CITY_COLOR_2 = WHITE
ROAD_COLOR = WHITE
BACKGROUND_COLOR = (230, 230, 230)
COLOR_CONECTION_USED = 100, 166, 232
SELECTED_CITY_COLOR = 10, 106, 201

class Map():
    def __init__(self, width, height, latitude_min, latitude_max, 
                            longitude_min, longitude_max, locations):
        pygame.init()
        pygame.font.init()

        self.running = False
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.pygame_text = PyGameText("freesansbold.ttf", 14, GREEN, 0)

        self.latitude_min = latitude_min
        self.latitude_max = latitude_max
        self.longitude_min = longitude_min
        self.longitude_max = longitude_max

        self.latitude_center = (latitude_max - latitude_min) / 2
        self.longitude_center = (longitude_max - longitude_min) / 2

        self.pixel_latitude_rate = width / (latitude_max - latitude_min)
        self.pixel_longitude_rate = height / (longitude_max - longitude_min)

        self.locations = locations
        self.selected_citys = []
        self.road_paths = []
        self.dijkstra = Dijkstra(self.locations)

    def on_loop(self):
        self.draw_locations()


    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for location in self.locations:
                x_0, y_0 = location.pos[0] - CITY_SIMBOL_SIZE, location.pos[1] - CITY_SIMBOL_SIZE
                x_1, y_1 = location.pos[0] + CITY_SIMBOL_SIZE, location.pos[1] + CITY_SIMBOL_SIZE

                if x >= x_0 and x <= x_1 and y >= y_0 and y <= y_1:
                    if location in self.selected_citys:
                        self.selected_citys.remove(location)
                        self.run_dijkstra_algoritm()
                    else:
                        self.selected_citys.append(location)
                        self.run_dijkstra_algoritm()


    def on_execute(self):
        self.running = True

        while(self.running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    self.on_event(event)
            
            self.screen.fill(BACKGROUND_COLOR)
            self.on_loop()
            pygame.display.flip()
    
    def run_dijkstra_algoritm(self):
        self.road_paths = []
        if len(self.selected_citys) > 1:
            for i in range(0,len(self.selected_citys) - 1, 1):
                self.road_paths.append(self.dijkstra.best_path(self.selected_citys[i], self.selected_citys[i+1]))
            for path in self.road_paths:
                for conection in path.conections:
                    conection.traveled = True

    def draw_locations(self):
        for location in self.locations:
            self.draw_roads(location)

        self.draw_road_paths()
        for location in self.locations:
            self.draw_location(location)


    def draw_location(self, location):
        text_posx, text_posy = location.pos[0], location.pos[1]
        pygame.draw.circle(self.screen, CITY_COLOR_1, location.pos, CITY_SIMBOL_SIZE)
        pygame.draw.circle(self.screen,SELECTED_CITY_COLOR if location in 
                        self.selected_citys else CITY_COLOR_2, location.pos, CITY_SIMBOL_SIZE // 2)
        self.pygame_text.render(self.screen, location.name, text_posx, text_posy)

    def draw_roads(self, location):
        for conection in location.conections:
            pygame.draw.line(self.screen, ROAD_COLOR,
                conection.start_location.pos, conection.dest_location.pos, 10)

    def draw_road_paths(self):
        for path in self.road_paths:
            for conection in path.conections:
                pygame.draw.line(self.screen, COLOR_CONECTION_USED,
                        conection.start_location.pos, conection.dest_location.pos, 10)

def test_default_map():
    city = Location("Coité do\nNoía", (100, 100))
    city2 = Location("Arapiraca", (300, 300))
    city3 = Location("Palmeiras dos\nindios", (500, 300))
    city4 = Location("Maceio", (500, 500))

    city.add_conection(city3, 10)
    city.add_conection(city2, 20)
    city2.add_conection(city3, 30)
    city3.add_conection(city4, 10)
    test_1 = [city, city2, city3, city4]

    map = Map(1200, 700, 0, 40 , 0, 40,test_1)
    map.on_execute()