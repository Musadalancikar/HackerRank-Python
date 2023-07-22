import calendar

def find_day_of_week(date_str):
    try:
        month, day, year = date_input
        day_of_week = calendar.weekday(year, month, day)
        return calendar.day_name[day_of_week]
    except ValueError:
        return "Format: MM DD YYYY"

date_input = map(int, input().split())
day_of_week = find_day_of_week(date_input)
print(day_of_week.upper())


