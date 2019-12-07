import os
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

from results_json import attributes_to_dataframe

sns.set_style("darkgrid")
sns.set_context("notebook", font_scale=2, rc={"lines.linewidth": 2.5})

RESULTS_FOLDER_NAME = "results"

class Results():
    def __init__(self, results_dict = {}, columns = []):
        self.dataframe = attributes_to_dataframe([""], columns, results_dict)

    def plot_attribute_line_plot(self, filters, x_label, y_label):
        dataframe = self.dataframe

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

    def save(self, file_name):
        file_path = os.path.join(RESULTS_FOLDER_NAME, file_name)
        self.dataframe.to_csv(file_path)

    @classmethod
    def load_results(self, results_file_name):
        file_path = os.path.join(RESULTS_FOLDER_NAME, results_file_name)
        results = Results()
        results.dataframe = pd.read_csv(file_path)

        return results

    def __add__(self, other):
        results = Results()
        results.dataframe = pd.concat(self.dataframe, other.dataframe)