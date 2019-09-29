import numpy as np
from sample.sample import Sample
from sample.population import Population

class SampleCityPath(Sample):
    def __init__(self, path, citys_pos, matrix_dist,fitness = None):
        self.path = path
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
    
    def crossover(self, other):
        return self

    def mutate(self, mutate_rate):
        number_changes = int(len(self.path) * mutate_rate)
        path = self.path
        for cont in range(number_changes):
            a, b = np.random.choice(range(0, len(path)), 2, False)
            aux = self.path[a]
            path[a] = self.path[b]
            path[b] = aux
        
        return SampleCityPath(path, self.citys_pos, self.matrix_dist)

    @classmethod
    def crossover_population(cls, population):
        population = population.sort()
        number_choose_samples = int(len(population) ** 0.5)
        choose_samples = population[:number_choose_samples]
        random_samples = np.random.choice(population[number_choose_samples:], 
                                                number_choose_samples, False)
        fitness = np.array(population.fitness)
        mutate_rates = (fitness - min(fitness))/ (max(fitness) - min(fitness))

        new_population = Population([])
        for s1, mutate_rate in zip(population, mutate_rates):
            new_population.append(s1.mutate(mutate_rate))
        
        return new_population.sort()