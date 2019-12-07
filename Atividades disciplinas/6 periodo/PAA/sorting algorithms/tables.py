import os
import pandas as pd
from radon import metrics, raw
from collections import OrderedDict

latex_tables_folder = "latex tables/"

def build_selected_sorted_algorithms_caract_table():
    columns = ["Nome", "Método", "Melhor caso", "Caso médio", "Pior caso", "in-place", "Memória", "Estável", "Adaptativo"]
    rows = [
        ["tree_sort", "Inserção", "n log(n)", "n log(n)", "n log(n)(balanceada)", "Não", "n", "Sim", "Não"],
        ["tim_sort", "Inserção e mistura", "n", "n log(n)", "n log(n)", "Não", "n", "Sim", "Sim"],
        ["cartesian_tree_sort", "Inserção e troca","n", "n log(n)", "n log(n)", "Não", "n", "Não", "Sim"],
        ["heap_sort", "Seleção", "n log(n)", "n log(n)", "n log(n)", "Sim", "1", "Não", "Não"],
        ["quick_sort", "Particionamento", "n log(n)", "n log(n)", "$n^2$", "Sim", "n", "Não", "Não"]
    ]

    dataframe = pd.DataFrame(data = rows, columns = columns)

    with open(os.path.join(latex_tables_folder,"selected_sorted_algorithms.tex"), "w", encoding="utf-8") as f:
        f.write(dataframe.to_latex())
    
    return dataframe

def build_code_complexity_table():
    def get_code_metrics(sort_name):
        with open(f"sort_algorithms/{sort_name}/code.txt", "r") as f:
            code = "".join(f.readlines())
            metricas =metrics.h_visit(code)
            mi_parameters = metrics.mi_parameters(code)
            analize = raw.analyze(code)

            return OrderedDict({
                "Nome" : sort_name,
                "Número de linhas de código" : analize.lloc,
                "Número de operadores" : metricas.total.N1,
                "Número de operandos" : metricas.total.N2,
                "Dificuldade" : metricas.total.difficulty,
                "Esforço" : metricas.total.effort,
                "Complexidade ciclomática" : mi_parameters[1], 

            })

    selected_algorithms = ["tree_sort", "quick_sort", "heap_sort", "tim_sort", "cartesian_tree_sort"]
    dataframe = pd.DataFrame.from_dict(
        list(map(get_code_metrics, selected_algorithms))
    )

    with open(os.path.join(latex_tables_folder,"code_complexity_algorithms.tex"), "w", encoding="utf-8") as f:
        f.write(dataframe.to_latex())

    return dataframe
