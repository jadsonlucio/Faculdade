import numpy as np

from test import get_map_test_1
from draw_map import MapDraw

def test_map(map, map_draw):
    print(map_draw.real_pixel_height)
    print(map_draw.real_pixel_width)
    print(map.top_left_location.real_pos)
    for location in map.locations:
        print(location.relative_x_y_coor(map.top_left_location))
        print(location.real_pos)
        print(location.virtual_pos)

   

if __name__ == "__main__":  
    mapa = get_map_test_1()
    map_draw = MapDraw(1200, 600, mapa)
    map_draw.on_execute()
    