"""
Создать список произвольного содержания. После каждой операции выводить список на экран
Создать еще один список произвольного содержания.
Расширить первый список вторым.
Вставить 123 пятым элементом.
Вывести на экран длину итогового списка.
"""

list1 = [0, 1, 2]
print(list1)
list2 = [3, 4, 5]
print(list2)
list1.extend(list2)
print(list1)
list1.insert(4, 123)
print(list1)
print(len(list1))
