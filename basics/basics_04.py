"""
Создать два списка a = [1,2,3,4] и b = [ ]
Вывести на экран id a и b
Присвоить b значение a (b=a)
Вывести на экран id переменных
Добавить элемент в список b
Вывести на экран оба списка
"""
a = [1, 2, 3, 4]
b = []
print(a)
print(b)
print(id(a))
print(id(b))
b = a
print(id(a))
print(id(b))
b.append(5)
print(a)
print(b)
