"""
Пользователь вводит три числа. Увеличьте первое число в два раза, второе числа уменьшите на 3,
третье число возведите в квадрат и затем найдите сумму новых трех чисел.
"""
a, b, c = float(input()), float(input()), float(input())
a *= 2
b -= 3
c **= 2
print(a, b, c)
sum = a + b + c
print(sum)
