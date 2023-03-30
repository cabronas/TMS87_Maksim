"""
Рассчитать месячные выплаты (m) и суммарную выплату (s) по кредиту. О кредите известно, что он составляет n рублей,
берется на y лет, под p процентов.  n, y, p - вводятся с клавиатуры. Месячные выплаты находятся по формуле:
m = (n * p * (1 + p)y) / (12 * ((1 + p)y – 1)), где p выражается в долях единицы, а не процентах.
Суммарная выплата представляет собой выплаты за все месяцы каждого года: s = (m * 12) * y
"""
n = float(input())
y = float(input())
p = float(input())
pe = p / 100
m = (n * pe * ((1 + pe) ** y)) / (12 * (((1 + pe) ** y) - 1))
s = (m * 12) * y
print(f'm={m} s={s}')