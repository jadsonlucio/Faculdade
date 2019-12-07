def quadratict_transformation(data):
    transformed_data = [c for c in data]

    for i in range(len(data)):
        for j in range(i, len(data), 1):
            transformed_data.append(data[i] * data[j])

    return transformed_data
    


dict_transf_funcs = {
    "quad_transf" : quadratict_transformation
}