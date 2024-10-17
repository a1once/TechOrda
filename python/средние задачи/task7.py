def is_perfect_number(num):
    if num < 2:
        return False
    
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

num = int(input("Введите число: "))

if is_perfect_number(num):
    print(f"{num} является совершенным числом.")
else:
    print(f"{num} не является совершенным числом.")