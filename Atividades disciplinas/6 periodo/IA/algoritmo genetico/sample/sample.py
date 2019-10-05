class Sample():
    def __init__(self, fitness = None):
        self.fitness = fitness
        self._mutate_rate = None
    
    def __gt__(self, other):
        return self.fitness > other.fitness
    
    def __iter__(self):
        return iter(self.path)

    @property
    def mutate_rate(self):
        if self._mutate_rate == None:
            raise Exception("Mutate rate is none, please call the method\
                            mutate_rates of population object that this sample\
                            belongs before calling this method")
        
        return self._mutate_rate

    def mutate(self, mutate_rate):
        raise NotImplementedError("Method mutate func not implemented")

    def fitness_func(self, *args, **kwargs):
        raise NotImplementedError("Method fitness func not implemented")

    def crossover(self, other):
        raise NotImplementedError("Method fitness func not implemented")
    
    def __copy__(self):
        raise NotImplementedError("Copy not implemented")

    @classmethod
    def crossover_population(cls, population):
        raise NotImplementedError("Method crossover_population func not implemented")
