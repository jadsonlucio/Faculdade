import json
import os
from results_json import attributes_to_dataframe

RESULTS_FOLDER_NAME = "results"

class Results():
    def __init__(self, results_dict = {}, columns = []):
        self.results_dict = results_dict
        self.columns = columns
        self.dataframe = attributes_to_dataframe([""], columns, self.results_dict)

    def plot_attribute(self, seleted_algorithms, select_metric, metric = "mean"):
        
        """print(seleted_algorithms)
        dataframe = self.dataframe[self.dataframe["Nome do algoritmo"].isin(seleted_algorithms)]
        dataframe = dataframe[dataframe["Tipo array"] == "info_shuffle_order"]
        dataframe = dataframe[dataframe["atributo"] == select_metric]
        dataframe[select_metric] = dataframe["Valor"]

        print(dataframe)

        fig = plt.figure(figsize=(15,15))
        ax = fig.add_subplot(111)
        sns.lineplot(x="Tamanho entrada", y = select_metric, hue = "Nome do algoritmo", data = dataframe, ax = ax)
        plt.show()"""
        pass

    def save(self, file_name):
        file_path = os.path.join(RESULTS_FOLDER_NAME, file_name)
        results = {
            "results_dict" : self.results_dict,
            "columns" : self.columns
        }
        print(file_path)
        with open(file_path, "w") as f:
            json.dump(results, f)

    @classmethod
    def load_results(self, results_file_name):
        file_path = os.path.join(RESULTS_FOLDER_NAME, results_file_name)

        with open(file_path, "r") as f:
            return Results(**json.load(f))