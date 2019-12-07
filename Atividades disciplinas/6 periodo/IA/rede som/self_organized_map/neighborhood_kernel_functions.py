from math import exp

def neighborhood_kernel_1(w1, w2, neighborhood_decal, similarity_func):
    return exp(-similarity_func(w1, w2)**2/(2*neighborhood_decal**2))