def filter_strings_array(input_array):
    output_array = []
    for string in input_array:
        if len(string) <= 3:
            output_array.append(string)
    return output_array