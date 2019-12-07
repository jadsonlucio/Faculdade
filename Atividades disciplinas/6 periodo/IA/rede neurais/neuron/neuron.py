import numpy as np

class BaseNeuron:
    def __init__(self, input_size, activation_func, 
            transformation_func = lambda x : x,  learning_rate = 0.1):

        self.input_size = len(transformation_func(list(range(input_size))))
        self.learning_rate = learning_rate
        self.activation_func = activation_func
        self.transformation_func = transformation_func
        self._weights = np.array([np.random.random() for c in range(self.input_size)])

    @property
    def weights(self):
        return self._weights

    @weights.setter
    def weights(self, weights):
        if isinstance(weights, list):
            self._weights = np.array(weights)

    def output(self, X):
        X = self.transformation_func(X)
            
        return self.activation_func(sum(self._weights * X))

    def train_step(self, X, y):
        output = self.output(X)
        X = np.array(X)
        X = np.array(self.transformation_func(X))
        erro = y - output
    
        self._weights += X * erro * self.learning_rate

    
    def log(self, X, y):
        text = ""
        weights = [round(weight, 3) for weight in self._weights]

        for inputs, output in zip(X, y):
            prediction = self.output(inputs)
            text += f"entrada : {inputs}, pesos : {weights}, ativação : {self.activation_func.__name__},  saida : {prediction}, esperado : {output}" + "\n"
        
        return text