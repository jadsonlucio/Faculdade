import json
import os
import seaborn as sns
import matplotlib.pyplot as plt 
from results_json import attributes_to_dataframe

sns.set_style("darkgrid")
sns.set_context("notebook", font_scale=2, rc={"lines.linewidth": 2.5})


RESULTS_FOLDER_NAME = "results"

class Results():
    def __init__(self, results_dict = {}):
        self.results_dict = results_dict
        self.dataframe = attributes_to_dataframe([""], ["Nome do algoritmo", "Tamanho entrada", "Tipo array", "atributo", "Valor"], self.results_dict)
        print(self.dataframe)

    def plot_attribute(self, seleted_algorithms, select_metric, metric = "mean"):
        
        dataframe = self.dataframe[self.dataframe["Nome do algoritmo"].isin(seleted_algorithms)]
        dataframe = dataframe[dataframe["Tipo array"] == "info_shuffle_order"]
        dataframe = dataframe[dataframe["atributo"] == select_metric]
        dataframe[select_metric] = dataframe["Valor"]

        fig = plt.figure(figsize=(15,15))
        ax = fig.add_subplot(111)
        sns.lineplot(x="Tamanho entrada", y = select_metric, hue = "Nome do algoritmo", data = dataframe, ax = ax)
        plt.show()

    def save(self, file_name):
        file_path = os.path.join(RESULTS_FOLDER_NAME, file_name)
        print(file_path)
        with open(file_path, "w") as f:
            json.dump(self.results_dict, f)

    @classmethod
    def load_results(self, results_file_name):
        file_path = os.path.join(RESULTS_FOLDER_NAME, results_file_name)

        with open(file_path, "r") as f:
            return Results(json.load(f))