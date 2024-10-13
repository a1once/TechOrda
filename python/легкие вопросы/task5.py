def power(a, b):
    if b <= 0:
        return "Ошибка: степень должна быть больше 0."
    
    result = 1
    for _ in range(b):
        result *= a
    return result

a = int(input("Введите число a: "))
b = int(input("Введите степень b: "))

print(power(a, b))