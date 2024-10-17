def is_valid_date(date):
    day, month, year = map(int, date.split('.'))
    
    if not (1 <= month <= 12):
        return False
    
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif month in [4, 6, 9, 11]:
        max_day = 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            max_day = 29
        else:
            max_day = 28
    
    return 1 <= day <= max_day

date_input = input("Введите дату в формате дд.мм.гггг: ")

if is_valid_date(date_input):
    print("Дата корректна")
else:
    print("Дата некорректна")