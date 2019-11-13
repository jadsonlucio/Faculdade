import threading
from functools import partial

from neuron.accuracy import mse
from neuron.neuron import BaseNeuron
from neuron.activations import limiar

from graphs.classification_plot import PygameClassifierPlot

 

def test_neuron(neuron, screen):
    train_x = [[0, 0], [0, 1], [1,0], [1,1]]
    train_y = [0, 1, 1, 1]

    while(True):
        pred = []
        for x, y in zip(train_x, train_y):
            neuron.train_step(x, y)
        for x in train_x:
            pred.append(neuron.output(x))

        screen.update_screen_predictions()

        if mse(train_y, pred) == 0:
            print(neuron._weights)
            print(pred)
            break

def test_pygame_classifier_plot():
    neuron = BaseNeuron(2, partial(limiar, limiar_value = 0.5))
    screen = PygameClassifierPlot(neuron)

    thread = threading.Thread(target = test_neuron, args = (neuron, screen))
    thread.start()

    screen.run()

if __name__ == "__main__":
    test_pygame_classifier_plot()