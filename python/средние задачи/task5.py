def find_perfect_numbers(limit):
    perfect_numbers = []
    for num in range(2, limit + 1):
        divisors_sum = sum([i for i in range(1, num) if num % i == 0])
        if divisors_sum == num:
            perfect_numbers.append(num)
    return perfect_numbers

limit = 1000
perfect_numbers = find_perfect_numbers(limit)
print(perfect_numbers)