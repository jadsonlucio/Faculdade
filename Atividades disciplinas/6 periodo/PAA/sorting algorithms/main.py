from results import Results
from paper_graphs import barplot_complexity_algorithms_attributes
from paper_experiments import test_sort_algorithms_with_synthetic_arrays, test_sort_algorithms_with_shuffle_arrays


def plot_synthetic_arrays(attribute):
    selected_algorithms = ["tim sort", "merge sort"]
    arrays_size = [1000, 10000, 100000, 1000000]
    results = test_sort_algorithms_with_synthetic_arrays(selected_algorithms, arrays_size)
    filters = {
        "Nome do algoritmo" : selected_algorithms,
        "Tipo array" : "Ordem decrescente", 
    }

    results.plot_attribute_line_plot(filters, "Tamanho entrada", attribute)

def plot_algorithms_with_shuffle_arrays(attribute):
    selected_algorithms = ["bubble sort", "insertion sort", "quick sort", "merge sort", "heap sort", "selection sort"]
    array_size = 500
    shuffle_percentages = [0, 10, 15, 25, 40, 50, 65, 75, 100]
    results = test_sort_algorithms_with_shuffle_arrays(selected_algorithms, array_size, shuffle_percentages)

    results.plot_attribute_line_plot({}, "Porcentagem de desordenação", attribute)

def barplot_algorithms_std_with_shuffle_arrays(attribute):
    selected_algorithms = ["bubble sort", "insertion sort", "quick sort", "merge sort", "heap sort", "selection sort"]
    array_size = 500
    shuffle_percentages = [0, 10, 15, 25, 40, 50, 65, 75, 100]
    results = test_sort_algorithms_with_shuffle_arrays(selected_algorithms, array_size, shuffle_percentages)
    dataframe = results.dataframe
    dataframe = dataframe[dataframe["atributo"] == attribute]

    for algorithm, dataframe in results.dataframe.groupby("Nome do algoritmo"):
        print(algorithm, dataframe["Valor"].std() / dataframe["Valor"].mean())

if __name__ == "__main__":
    plot_synthetic_arrays("Tempo de execução")
    
