import numpy as np

class BaseNeuron:
    def __init__(self, input_size, activation_func, learning_rate = 0.1):
        self.input_size = input_size
        self.learning_rate = learning_rate
        self.activation_func = activation_func
        self._weights = np.array([np.random.random() for c in range(input_size)])

    @property
    def weights(self):
        return self._weights

    @weights.setter
    def weights(self, weights):
        if isinstance(weights, list):
            self._weights = np.array(weights)

    def output(self, X):
        X = np.array(X)
        return self.activation_func(sum(self._weights * X))

    def train_step(self, X, y):
        X = np.array(X)
        output = self.output(X)
        erro = y - output
                
        self._weights += X * erro * self.learning_rate

    
    def log(self, X, y):
        text = ""
        for inputs, output in zip(X, y):
            for x, w in zip(inputs[:-1], self._weights[:-1]):
                text += f"{self.activation_func.__name__}({x} * {w} + "

            prediction = self.output(inputs)
            text += f"{inputs[-1]} * {self.weights[-1]}) = {prediction}, esperado : {output} \n"
        
        return text