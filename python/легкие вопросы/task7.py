def find_min(arr):
    if len(arr) == 0:
        return 0
    else:
        min_value = arr[0]
        for num in arr[1:]:
            if num < min_value:
                min_value = num
        return min_value

# Примитивный ввод чисел
array = []
n = int(input("Сколько чисел вы хотите ввести? "))

for i in range(n):
    num = int(input(f"Введите число {i + 1}: "))
    array.append(num)

print("Mинимальноe значениe: ", find_min(array))