def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Введите число: "))

if is_prime(num):
    print(f"{num} является простым числом")
else:
    print(f"{num} не является простым числом")