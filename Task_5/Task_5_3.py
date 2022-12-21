""" Написать функцию, которая возвращает заданное число Фибоначчи. Обязательно через рекурсию. """

def f(x):
    """ Вычисления числа Фибоначчи.
    Принимает:
        х - номер числа в последовательности Фибоначчи
    """
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return f(x-1) + f(x-2)

try:
    n = int(input("Введите номер числа в последовательности Фибоначчи\n"))
    if n < 0:
        print("Число должно быть больше 0 или равно ему")
    else:
        print("Число Фибоначчи равно {0} для числа с номером {1}".format(f(n), n))
except ValueError:
    print("Это должно быть целое число")
