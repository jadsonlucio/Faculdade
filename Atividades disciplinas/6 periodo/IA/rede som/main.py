import threading, sys, os
import json
import numpy as np

from graphs.som_graph import PygameSOM

from self_organized_map.self_organized_map import NetworkSOM

from self_organized_map.similarity_functions import euclidian_distance
from self_organized_map.neighborhood_kernel_functions import neighborhood_kernel_1

from datasets import *

if __name__ == "__main__":
    screen = PygameSOM()

    som = NetworkSOM(4, 4, 0.8, 0.8, 100, 100, euclidian_distance, neighborhood_kernel_1)

    thread = threading.Thread(target = som.fit, args = (RANDOM_DATASET, 20, screen.update_screen))
    thread.start()

    screen.run()