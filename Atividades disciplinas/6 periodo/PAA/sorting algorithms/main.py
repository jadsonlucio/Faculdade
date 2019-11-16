from paper_graphs import plot_synthetic_arrays_attribute, plot_attribute_results_line_plot
from paper_experiments import test_sort_algorithms_with_synthetic_arrays, test_sort_algorithms_with_shuffle_arrays


def plot_synthetic_arrays(attribute):
    selected_algorithms = ["bubble sort", "tree sort avl", "heap sort"]
    arrays_size = [10, 100, 1000, 2000]
    results = test_sort_algorithms_with_synthetic_arrays(selected_algorithms, arrays_size)

    plot_synthetic_arrays_attribute(results, selected_algorithms, attribute)


def plot_algorithms_with_shuffle_arrays(attribute):
    selected_algorithms = ["bubble sort", "insertion sort", "quick sort", "merge sort", "heap sort", "selection sort"]
    array_size = 500
    shuffle_percentages = [0, 10, 15, 25, 40, 50, 65, 75, 100]
    results = test_sort_algorithms_with_shuffle_arrays(selected_algorithms, array_size, shuffle_percentages)

    plot_attribute_results_line_plot(results, {}, "Porcentagem de desordenação", attribute)

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
    barplot_algorithms_std_with_shuffle_arrays("time to run")