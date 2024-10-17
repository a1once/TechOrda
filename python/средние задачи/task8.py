def determine_season(month):
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Некорректный месяц"

date_input = input("Введите дату в формате дд.мм: ")

day, month = map(int, date_input.split("."))

season = determine_season(month)
print(f"Дата {date_input} относится к сезону: {season}")