from plots import plot_attribute_results_line_plot

def plot_synthetic_arrays_attribute(results, algorithms, attribute):
    filters = {
        "Nome do algoritmo" : algorithms,
        "Tipo array" : "info_shuffle_order", 
    }
    plot_attribute_results_line_plot(results, filters, "Tamanho entrada", attribute)