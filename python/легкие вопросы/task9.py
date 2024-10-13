def sum_custom(arr):
    total = 0
    for num in arr:
        total += num
    return total

n = int(input("Сколько чисел вы хотите ввести? "))
array = []

for i in range(n):
    num = int(input(f"Введите число {i + 1}: "))
    array.append(num)

print(sum_custom(array))  