import numpy as np

class Population():
    def __init__(self, samples):
        self.samples = samples
    
    @property
    def fitness(self):
        _population_fitness = []
        for sample in self:
            _population_fitness.append(sample.fitness)
        
        return _population_fitness

    def fitness_statistics(self):
        """ Return mean and std of population fitness """
        population_fitness = self.fitness

        return (np.mean(population_fitness), np.std(population_fitness))

    
    def __iter__(self):
        return iter(self.samples)

    def __len__(self):
        return len(self.samples)
    
    def __getitem__(self, key):
        if isinstance(key, int) or isinstance(key,slice):
            return self.samples[key]
        elif isinstance(key, Slice):
            raise Exception("error")
    
    def append(self, sample):
        self.samples.append(sample)
    
    def sort(self):
        self.samples = sorted(self.samples)

        return self