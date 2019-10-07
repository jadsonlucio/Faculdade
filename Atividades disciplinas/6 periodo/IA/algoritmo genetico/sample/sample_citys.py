import numpy as np
from sample.sample import Sample
from sample.population import Population

class SampleCityPath(Sample):
    def __init__(self, path, citys_pos, matrix_dist, fitness = None):
        self.path = list(path)
        self.matrix_dist = matrix_dist
        self.citys_pos = citys_pos
        super().__init__(fitness)

        self.fitness_func()
    
    def fitness_func(self):
        self.fitness = 0
        prev_idx = self.path[0]

        for idx in self.path[1:]:
            self.fitness = self.fitness + self.matrix_dist[prev_idx][idx]
            prev_idx = idx
    
    def join_path(self, other, choiced_city):
        new_sample = self.copy()
        index_ele = new_sample.path.index(choiced_city)
        index_ele_other = other.path.index(choiced_city)
        if index_ele < len(new_sample.path) - 2 and index_ele_other < len(other.path) - 2:
            next_city_other = other.path[index_ele_other + 1]
            index_next_city_other = new_sample.path.index(next_city_other)
            aux = new_sample.path[index_ele + 1]
            new_sample.path[index_ele + 1] = new_sample.path[index_next_city_other]
            new_sample.path[index_next_city_other] = aux

        return new_sample

    def crossover(self, other):
        best_ind = self
        worst_ind = other
        if self.fitness > other.fitness:
            best_ind = other
            worst_ind = self

        change_rate = 0.2
        number_changes = int(len(self.path) * change_rate)

        for c in range(number_changes):
            choice_city = np.random.choice(best_ind.path[:-1])
            best_ind = best_ind.join_path(worst_ind, choice_city)
        
        return best_ind


    def mutate(self, mutate_rate):
        number_changes = int(len(self.path) * mutate_rate)
        path = self.path
        for cont in range(number_changes):
            a, b = np.random.choice(range(0, len(path)), 2, False)
            aux = self.path[a]
            path[a] = self.path[b]
            path[b] = aux
        
        return SampleCityPath(path, self.citys_pos, self.matrix_dist)

    def copy(self):
        return self.__copy__()

    def __copy__(self):
        return SampleCityPath(self.path.copy(), self.citys_pos, self.matrix_dist, self.fitness)
    

    @classmethod
    def crossover_population(cls, population):
        population = population.sort()

        number_choose_samples = int(len(population) ** 0.5)
        choose_population = population[:number_choose_samples]
        random_samples = np.random.choice(population[number_choose_samples:], 
                                                number_choose_samples - 1, False)

        
        new_population = Population([])
        new_population.append(choose_population)
        for s1 in choose_population:
            for s2 in random_samples:
                #print(s1.path)
                #print(s1.crossover(s2).path)
                new_population.append(s1.crossover(s2.mutate(0.4)))

        """ for s1, mutate_rate in zip(population, population.mutate_rates):
            new_population.append(s1.mutate(mutate_rate))"""
        
        return new_population.sort()