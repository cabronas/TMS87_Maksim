"""
Создать множество произвольного содержания. После каждой операции выводить множество на экран
Создать еще одно множество произвольного содержания.  Часть элементов должна совпадать с первым множеством.
Объединить множества.
Найти пересечение множеств.
Найти разницу между первым и вторым, и вторым и первым.
Объеденить два множества без общих элементов.
"""
set1 = {1, 2, 3}
print(set1)
set2 = {3, 4, 5}
print(set2)
set3 = set1 | set2
print(set3)
set3 = set1 & set2
print(set3)
set3 = set1 - set2
print(set3)
set3 = set2 - set1
print(set3)
set3 = set1 ^ set2
print(set3)
