from math import e

def relu(x):
    return max([0, x])


def identity(x):
    return x

def sigmoid(x):
    return 1/(1 + e**(-x))


def limiar(x , limiar_value = 0.5):
    if x <= limiar_value:
        return 0 
    else:
        return 1