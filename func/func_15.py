"""
Даны три слова.
Выяснить, является ли хоть одно из них палиндромом ("перевертышем"),
т. е. таким, которое читается одинаково слева направо и справа налево.
(Определить функцию, позволяющую распознавать слова палиндромы.)
"""


def checkIfPolyndrom(s):
    if s == s[::-1]:
        return True
    return False


def main():
    arr = input("Введите 3 слова через пробел:\n").split(" ")
    for word in arr:
        if checkIfPolyndrom(word):
            print(f"{word} - полиндром")
        else:
            print(f"{word} - не полиндром")


if __name__ == "__main__":
    main()
