import threading, sys, os
import json
import numpy as np

from functools import partial

from neuron.accuracy import mse
from neuron.neuron import BaseNeuron
from neuron.activations import limiar
from neuron.data_transformation import dict_transf_funcs

from graphs.classification_plot import PygameClassifierPlot

 

def train_neuron(neuron, screen, n_iterations, train_x, train_y):
    screen.add_prediction_points(train_x, train_y)

    for i in range(n_iterations):
        pred = []
        for x, y in zip(train_x, train_y):
            neuron.train_step(x, y)
        for x in train_x:
            pred.append(neuron.output(x))

        screen.update_screen_predictions()

        print(neuron.log(train_x, train_y))

        if mse(train_y, pred) == 0:
            print(f"pesos : {neuron._weights}")
            print(f"previsões : {pred}")
            break

    print("terminou")
    q = input()
    os._exit(1)

def pygame_classifier_plot(train_x, train_y, transform_func):
    def limiar_0_5(value):
        return limiar(value, 0.5)

    n_neurons = len(train_x[0])
    neuron = BaseNeuron(n_neurons, limiar_0_5, transform_func)
    screen = PygameClassifierPlot(neuron)

    thread = threading.Thread(target = train_neuron, args = (neuron, screen, 30, train_x, train_y))
    thread.start()

    screen.run()

if __name__ == "__main__":
    args = sys.argv
    file_name = args[1]
    input_file = json.load(open(f"dados/{file_name}", "r"))
    train_x = input_file["inputs"]
    train_y = input_file["outputs"]

    if len(args) == 3:
        transform_func = args[2]
        transform_func = dict_transf_funcs[transform_func]
    else:
        transform_func = lambda x : x
    
    pygame_classifier_plot(train_x, train_y, transform_func)