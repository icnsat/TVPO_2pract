#Функция для поиска максимального значения в массиве
def find_max(arr):
    if not arr:
        raise ValueError("Массив не должен быть пустым")
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value


#Функция для поиска минимального значения в массиве
def find_min(arr):
    if not arr:
        raise ValueError("Массив не должен быть пустым")
    min_value = arr[0]
    for num in arr:
        if num < min_value:
            min_value = num
    return min_value


#Функция для сортировки массива (пузырьковая сортировка)
def sort_array(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


#Функция для разворота массива
def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

#Функция для подсчета суммы элементов массива
def sum_array(arr):
    if not arr:
        raise ValueError("Массив не должен быть пустым")
    return arr[0]