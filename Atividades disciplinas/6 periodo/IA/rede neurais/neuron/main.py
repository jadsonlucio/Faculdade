from functools import partial

from accuracy import mse
from neuron import BaseNeuron
from activations import limiar


train_x = [[0, 0], [0, 1], [1,0], [1,1]]
train_y = [0, 1, 1, 1]
 
if __name__ == "__main__":
    neuron = BaseNeuron(2, partial(limiar, limiar_value = 0.5))
    
    while(True):
        pred = []
        for x, y in zip(train_x, train_y):
            neuron.train_step(x, y)

        for x in train_x:
            pred.append(neuron.output(x))


        if mse(train_y, pred) == 0:
            print(neuron._weights)
            print(pred)
            break
