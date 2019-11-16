import seaborn as sns
import matplotlib.pyplot as plt 

sns.set_style("darkgrid")
sns.set_context("notebook", font_scale=2, rc={"lines.linewidth": 2.5})

def plot_attribute_results_line_plot(results, filters, x_label, y_label):
    dataframe = results.dataframe

    for name, value in filters.items():
        if  not isinstance(value, list):
            dataframe = dataframe[dataframe[name] == value]
        else:
            dataframe = dataframe[dataframe[name].isin(value)]
    
    dataframe = dataframe[dataframe["atributo"] == y_label]
    dataframe[y_label] = dataframe["Valor"]

    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111)
    sns.lineplot(x = x_label, y = y_label, hue = "Nome do algoritmo", data = dataframe, ax = ax)
    plt.show()