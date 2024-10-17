def is_palindrome(str):
    low_input = str.lower()
    
    return low_input == low_input[::-1]

input = input("Введите строку: ")

if is_palindrome(input):
    print("Строка является палиндромом.")
else:
    print("Строка не является палиндромом.")