def range_custom(n):
    arr = []
    for i in range(1, n + 1):
        arr.append(i)
    return arr

n = int(input("Введите размер массива: "))

if 0 < n <= 10000:
    result = range_custom(n)
    print(result)
else:
    print("Ошибка: n должно быть от 1 до 10000.")