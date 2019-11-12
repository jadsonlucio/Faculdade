import pytest 
from math import e
from neuron import BaseNeuron
from activations import identity, relu, sigmoid


def test_neuron_output_with_identity_activation():
    neuron = BaseNeuron(3, identity)
    neuron.weights = [1, 1, 1]

    output = neuron.output([1,2,3])
    assert output == 6

def test_neuron_output_with_relu_activation():
    neuron = BaseNeuron(3, relu)
    neuron.weights = [-1, -1, 1]

    output_1 = neuron.output([1, 1, 1])
    output_2 = neuron.output([-1, -1, 1])

    assert output_1 == 0 
    assert output_2 == 3

def test_neuron_output_with_sigmoid_activation():
    neuron = BaseNeuron(3, sigmoid)
    neuron.weights = [1, 1, 1]

    output_1 = neuron.output([0, 0, 0])
    output_2 = neuron.output([-1, 0, 0])

    assert output_1 == 0.5
    assert output_2 == 1 / (1 + e)