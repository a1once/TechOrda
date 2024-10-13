def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

n = int(input("Введите число n: "))
if 1 <= n <= 10860:
    print(sum_of_squares(n))
else:
    print("число должно быть от 1 до 10860.")