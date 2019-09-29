class Sample():
    def __init__(self, fitness = None):
        self.fitness = fitness
    
    def __gt__(self, other):
        return self.fitness > other.fitness
    
    def __iter__(self):
        return iter(self.path)

    def mutate(self, mutate_rate):
        raise NotImplementedError("Method mutate func not implemented")

    def fitness_func(self, *args, **kwargs):
        raise NotImplementedError("Method fitness func not implemented")

    def crossover(self, other):
        raise NotImplementedError("Method fitness func not implemented")



    @classmethod
    def crossover_population(cls, population):
        raise NotImplementedError("Method crossover_population func not implemented")
