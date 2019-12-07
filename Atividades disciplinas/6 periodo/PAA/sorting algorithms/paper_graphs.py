import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from tables import build_code_complexity_table


def barplot_complexity_algorithms_attributes(selected_attributes):
    complexity_dataframe = build_code_complexity_table()
    columns = {
        "Nome algoritmo" : [],
        "Nome atributo" : [],
        "Valor" : []
    }

    for selected_attribute in selected_attributes:
        columns["Nome algoritmo"] = columns["Nome algoritmo"] + list(complexity_dataframe["Nome"].values)
        columns["Nome atributo"] = columns["Nome atributo"] + [selected_attribute for c in range(len(complexity_dataframe))]
        columns["Valor"] = columns["Valor"] + list(complexity_dataframe[selected_attribute].values)


    dataframe_attibutes = pd.DataFrame.from_dict(columns)
    
    sns.barplot(data = dataframe_attibutes, x = "Nome algoritmo", y = "Valor", hue = "Nome atributo")
    plt.show()