from math import exp
from functools import partial

import numpy as np
from time import sleep

def learning_rate_decal(iteration, learning_rate, t1):
    return learning_rate*exp(-iteration/t1)

def neighborhood_rate_decal(iteration, neighborhood, t2):
    return neighborhood*exp(-iteration/t2)


class NetworkSOM():
    def __init__(self, sizeX, sizeY, learning_rate, neighborhood_rate, 
                    t1, t2, similarity_func, neighborhood_kernel_func):
        """
        sizeX : sizeX of output neurons
        sizeY : sizeY of output neurons
        t1 : normalization factor in learning rate decal
        t2 : normalization faction in neighborhood size decal
        """
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.t1 = t1
        self.t2 = t2
        self.learning_rate_ini = learning_rate
        self.neighborhood_rate_ini = neighborhood_rate
        self.similarity_func = similarity_func
        self.neighborhood_kernel_func = partial(neighborhood_kernel_func, similarity_func = similarity_func)

        self.learning_rate = partial(learning_rate_decal, learning_rate=learning_rate, t1 = t1)
        self.neighborhood_rate = partial(neighborhood_rate_decal, neighborhood = neighborhood_rate, t2 = t2)
        self.fitted = False
        self.neurons = None


    def start_neurons(self, widghts_dim):
        size_array = self.sizeX * self.sizeY
        self.neurons = np.random.uniform(size = (size_array, widghts_dim))

    def update_neurons(self, x, iteration):
        similaritys = list(map(partial(self.similarity_func, y = x), self.neurons))
        most_similar_neurons_idxs = np.argsort(similaritys)[:10]
        chosen_neuron_idx = most_similar_neurons_idxs[0]
        chosen_neuron = self.neurons[chosen_neuron_idx]

        for neuron_idx in most_similar_neurons_idxs:
            neuron = self.neurons[neuron_idx]
            neighborhood_decal = self.neighborhood_rate(iteration)
            neighborhood_kernel_rate = self.neighborhood_kernel_func(chosen_neuron, neuron, neighborhood_decal)
            self.neurons[neuron_idx] += self.learning_rate(iteration) * neighborhood_kernel_rate * (x - neuron)

    def fit(self, trainX, max_iteration = 1000, callback_func = lambda x : x):
        self.trainX = np.array(trainX)

        x, widghts_dim = self.trainX.shape
        self.start_neurons(widghts_dim)

        for i in range(max_iteration):
            for x in trainX:
                self.update_neurons(x, i)
                callback_func(self)

                sleep(0.25)

