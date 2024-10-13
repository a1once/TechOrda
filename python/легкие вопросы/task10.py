def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

n = int(input("Сколько чисел вы хотите ввести? "))
array = []

for i in range(n):
    num = int(input(f"Введите число {i + 1}: "))
    array.append(num)

print(bubble_sort(array))