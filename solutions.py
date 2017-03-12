import math
# 1
def arithmetic(x,y,oper):
    if oper == "+":
        return x+y
    if oper == "-":
        return x-y
    if oper == "*":
        return x*y
    else:
        return "Неизвестная операция"
# 2
def is_year_leap(year):
    if year % 400 == 0 or (year % 4 ==0 and year %100 != 0):
        return "Год высокосный"
    else:
        return "No"

# 3

def square(a):
    return a**2, 4*a, 2*math.sqrt(2)
# 4

def season(num):
    if num in (1,2) or num == 12:
        return "Winter"
    if 3 <= num <= 5:
        return "Spring"
    if 6 <= num <= 8:
        return "Summer"
    else:
        return "Autumn"
# 5

def bank(a, years):
    i = 0.1
    for year in range(years):
        a *= (1 + i)
    return a
# 6

def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
    
