import threading
from functools import partial

from neuron.accuracy import mse
from neuron.neuron import BaseNeuron
from neuron.activations import limiar

from graphs.classification_plot import PygameClassifierPlot

 

def test_neuron(neuron, screen):
    train_x = [[-1, -1], [0, 1], [-1,-3], [5,1], [3, -3], [1, -1]]
    train_y = [1, 0, 1, 0, 1, 0]
    
    screen.add_prediction_points(train_x, train_y)

    while(True):
        pred = []
        for x, y in zip(train_x, train_y):
            neuron.train_step(x, y)
        for x in train_x:
            pred.append(neuron.output(x))

        screen.update_screen_predictions()

        print(neuron.log(train_x, train_y))

        if mse(train_y, pred) == 0:
            print(neuron._weights)
            print(pred)
            break

def test_pygame_classifier_plot():
    def limiar_0_5(value):
        return limiar(value, 0.5)

    neuron = BaseNeuron(2, limiar_0_5)
    screen = PygameClassifierPlot(neuron)

    thread = threading.Thread(target = test_neuron, args = (neuron, screen))
    thread.start()

    screen.run()

if __name__ == "__main__":
    test_pygame_classifier_plot()