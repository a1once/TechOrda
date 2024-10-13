def compare_numbers(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print(compare_numbers(a, b))