"""
Просуммировать неопределенное количество чисел, вводимых пользователем, суммировать до тех пор,
пока пользователь не введёт слово «стоп». Не учитывать числа кратные 5
"""
summ = 0
while True:
    a = input()
    if a != "stop":
        if int(a) % 5 == 0:
            continue
        else:
            summ += int(a)
    else:
        break
print(summ)