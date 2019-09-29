import numpy as np
from numpy import random
from sample.sample_citys import SampleCityPath
from sample.population import Population

def generate_init_population(number_citys, size, matrix_dist, citys_pos):
    population = Population([])
    arr = np.arange(number_citys)
    for cont in range(size):
        np.random.shuffle(arr)
        population.append(SampleCityPath(np.copy(arr), citys_pos, matrix_dist))
    
    return population


def generate_cits_dist_matrix(number_citys, x_max = 100, y_max = 100):
    def euclidian_dist(array_1, array_2):
        return sum((np.array(array_1) - np.array(array_2))**2)**0.5

    citys_pos = [(np.random.randint(0, x_max), np.random.randint(0, x_max)) for cont in range(number_citys)]
    matrix_dist = []
    for city_pos_1 in citys_pos:
        row = []
        for city_pos_2 in citys_pos:
            row.append(euclidian_dist(city_pos_1, city_pos_2))
        
        matrix_dist.append(row)
    
    return citys_pos, matrix_dist