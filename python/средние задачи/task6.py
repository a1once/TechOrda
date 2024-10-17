def is_fibonacci(num):
    a, b = 0, 1
    
    while b <= num:
        if b == num:
            return True
        a, b = b, a + b
        
    return False

num = int(input("Введите число: "))
if is_fibonacci(num):
    print(f"{num} является числом Фибоначчи.")
else:
    print(f"{num} не является числом Фибоначчи.")