"""
Создать переменные firstname, lastname, age с соответствующими значениями
Путем сложения получить строку вида:
Привет, меня зовут Иван Иванович, мне 35 лет
Вывести на экран саму строку и длину строки
Примечание: переменную age задавать как строку ‘35’
"""
firstname = "Иван"
lastname = "Иванович"
age = "35"
resultstring = "Привет, меня зовут " + firstname + " " + lastname + ", мне " + age + " лет"
print(resultstring)
print(len(resultstring))
