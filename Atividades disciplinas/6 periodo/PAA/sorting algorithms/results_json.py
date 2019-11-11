import json 
import pandas as pd


def get_result_attributes(attrs, result_json):
    response_dict = {}
    for key,value in result_json.items():
        if key in attrs:
            response_dict[key] = value
        elif isinstance(value, dict):
            _response_dict = get_result_attributes(attrs, value)
            if _response_dict:   
                response_dict[key] = _response_dict

    return response_dict

def json_to_list(json_dict):
    results = []
    for key, value in json_dict.items():
        if not isinstance(value, dict):
            results.append([key,*value]) if isinstance(value,list) else results.append([key,value])
        else:
            _results = json_to_list(value)
            for result in _results:
                results.append([key,*result])

    
    return results

def attributes_to_dataframe(attrs, columns, result_json):
    if attrs == [""]:
        response_dict = result_json
    else:
        response_dict = get_result_attributes(attrs, result_json)
    
    list_attributes = json_to_list(response_dict)
    
    dataframe = pd.DataFrame(data = list_attributes, columns = columns)
    #dataframe = dataframe.drop(labels = ["None"], axis = 1)

    return dataframe