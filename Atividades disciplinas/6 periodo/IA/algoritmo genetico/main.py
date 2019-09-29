import threading
from time import sleep

from draw_citys import DisplayCitys
from genetic_algorithm import Genetic
from citys_func import *

NUMBER_CITYS = 20
POPULATION_SIZE = 25
MAP_X_SIZE = 500
MAP_Y_SIZE = 500

def change_display_city_wrapper(display_city):
    def wrapper(cont, history, population):
        display_city.best_path = population[0].path
    
    return wrapper

if __name__ == "__main__":
    citys_pos, matrix_dist = generate_cits_dist_matrix(NUMBER_CITYS, MAP_X_SIZE, MAP_Y_SIZE)

    initial_population = generate_init_population(NUMBER_CITYS, POPULATION_SIZE, matrix_dist, citys_pos)
    display_city = DisplayCitys(citys_pos, initial_population[0].path, MAP_X_SIZE, MAP_Y_SIZE)
    

    callback_display_citys = change_display_city_wrapper(display_city)
    genetic = Genetic(initial_population)

    thread1 = threading.Thread(target = genetic.evolve, args = (callback_display_citys,))
    thread1.start()
    display_city.run()