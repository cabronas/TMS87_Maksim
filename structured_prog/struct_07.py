"""
Ввести строку.
Вывести на экран букву, которая находится в середине этой строки.
Также, если эта центральная буква равна первой букве в строке, то создать и вывести часть строки между первым и последним символами исходной строки.
(подсказка: для получения центральной буквы, найдите длину строки и разделите ее пополам. Для создания результирующий строки используйте срез)
"""
import math

a = input()
middle = a[round(len(a) / 2)]
print(middle)
if middle == a[0]:
    b = a[1:-1]
    print(b)
