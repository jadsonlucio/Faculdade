import numpy as np
import matplotlib.pyplot as plt
from numpy import random


class Genetic:
    def __init__(self, population):
        self.history = {
        "mean_samples_score" : [],
        "std_samples_score" : [],
        "best_sample_score" : []
        }

        self.sample_class = population[0].__class__
        self.population = population


    def evolve(self, generation_callback = None, max_generations = 1000, verbose = False):
        cont = 0
        while(cont < max_generations):
            self.population = self.sample_class.crossover_population(self.population)

            mean_fitness_population, std_fitness_population = self.population.fitness_statistics()

            self.history["mean_samples_score"].append(mean_fitness_population)
            self.history["std_samples_score"].append(std_fitness_population)
            self.history["best_sample_score"].append(self.population[0].fitness)

            cont+=1

            if verbose:
                print(f"generation:{cont}")

            if generation_callback:
                generation_callback(cont, self.history, self.population)

        self.plot_history("best_sample_score")

    
    def plot_history(self, key):
        plt.plot(self.history[key], label = key)
        plt.show()