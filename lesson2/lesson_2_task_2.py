y = int(input('Какой год високосный?'))
def is_year_leap(y):
    if (y % 4 == 0):
        return True
    else:
        return False
result = is_year_leap(y)
print(f'год {y}: {result}')