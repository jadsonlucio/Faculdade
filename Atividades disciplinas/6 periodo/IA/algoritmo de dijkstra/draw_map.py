import pygame
import numpy as np

from text import PyGameText
from dijkstra import Dijkstra
from map.location import Location

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
TEXT_CITY_COLOR = 235, 137, 52

class MapDraw():
    def __init__(self, width, height, map):
        pygame.init()
        pygame.font.init()

        self.running = False
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.pygame_text = PyGameText("freesansbold.ttf", 14, TEXT_CITY_COLOR, 0)

        self.map = map
        self.real_pixel_width = self.width / self.map.width
        self.real_pixel_height = self.height / self.map.height
    
    def on_init(self):
        self.set_vitual_positions()

    def on_loop(self):
        self.draw_locations()


    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for location in self.map.locations:
                pos = location.virtual_pos
                x_0, y_0 = pos[0] - CITY_SIMBOL_SIZE, pos[1] - CITY_SIMBOL_SIZE
                x_1, y_1 = pos[0] + CITY_SIMBOL_SIZE, pos[1] + CITY_SIMBOL_SIZE

                if x >= x_0 and x <= x_1 and y >= y_0 and y <= y_1:
                    if location in self.map.selected_citys:
                        self.map.selected_citys.remove(location)
                        self.map.run_dijkstra_algoritm()
                    else:
                        self.map.selected_citys.append(location)
                        self.map.run_dijkstra_algoritm()


    def on_execute(self):
        self.on_init()
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
    
    def set_vitual_positions(self):
        for location in self.map.locations:
            ref_loc = self.map.top_left_location
            x_pos, y_pos = location.relative_x_y_coor(ref_loc)
            location._virtual_pos = x_pos * self.real_pixel_width, y_pos * self.real_pixel_height

    def draw_locations(self):
        for location in self.map.locations:
            self.draw_roads(location)

        self.draw_road_paths()
        for location in self.map.locations:
            self.draw_location(location)

        self.draw_locations_names()


    def draw_location(self, location):
        pos = location.virtual_pos
        text_posx, text_posy = pos[0], pos[1]
        pygame.draw.circle(self.screen, CITY_COLOR_1, pos, CITY_SIMBOL_SIZE)
        pygame.draw.circle(self.screen,SELECTED_CITY_COLOR if location in 
                        self.map.selected_citys else CITY_COLOR_2, pos, CITY_SIMBOL_SIZE // 2)
        self.pygame_text.render(self.screen, location.name, text_posx, text_posy)

    def draw_roads(self, location):
        for conection in location.conections:
            pygame.draw.line(self.screen, ROAD_COLOR,
                conection.start_location.virtual_pos, conection.dest_location.virtual_pos, 10)

    def draw_road_paths(self):
        for path in self.map.road_paths:
            for conection in path.conections:
                pygame.draw.line(self.screen, COLOR_CONECTION_USED,
                    conection.start_location.virtual_pos, conection.dest_location.virtual_pos, 10)

    
    def draw_locations_names(self):
        city_names = ""
        surface_text_roads = pygame.Surface((200, self.height))
        surface_text_roads.fill((0, 0, 0))
        
        for location in self.map.selected_citys[1:]:
            for conection in location.small_path:
                city_names += conection.dest_location.name[:-1] + "  " +str(int(conection.cost)) + "km" + "\n"


        #font = pygame.font.Font("freesansbold.ttf", 12)
        #font_surface = font.render(city_names, True, (255, 0, 255))
        surface_text_roads.set_alpha(150)
        self.pygame_text.render(surface_text_roads, city_names, 0, 0, False)
        self.screen.blit(surface_text_roads, (0, 0))
        
        #self.screen.blit(font_surface, (0, 0))

        