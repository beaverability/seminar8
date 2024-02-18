def filter_strings_array(input_array):
    output_array = []
    for string in input_array:
        if len(string) <= 3:
            output_array.append(string)
    return output_array


def main():
    input_array = input("Введите строки через запятую: ").split(", ")
    filtered_array = filter_strings_array(input_array)
    print("Исходный массив:", input_array)
    print("Новый массив (длина <= 3):", filtered_array)


if __name__ == "__main__":
    main()
