def is_leap(year):
    if year % 4 == 0:
        leap = True
    else:
        if year % 100 == 0:
            leap = False
        elif year % 400:
            leap = True
    return leap

year = int(input())
print(is_leap(year))