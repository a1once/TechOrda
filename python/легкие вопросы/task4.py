def get_even_in_range(a, b):
    even_numbers = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print(get_even_in_range(a, b))