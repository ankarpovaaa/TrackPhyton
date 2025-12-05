numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим


numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Находим индекс None
none_index = numbers.index(None)

# Сумма всех чисел, кроме None
sum_without_none = sum(num for num in numbers if num is not None)

# Среднее арифметическое: сумма без None делится на общее количество элементов
average = sum_without_none / len(numbers)

# Заменяем None на среднее арифметическое
numbers[none_index] = average

print("Измененный список:", numbers)