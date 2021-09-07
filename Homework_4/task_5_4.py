# 5. Реализовать формирование списка, используя функцию range()
# и возможности генератора. В список должны войти четные числа от 100 до 1000
# (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def mult_nums(a, b):
    """
    Функция mult_nums принимает два числа и выполняет их умножение.
    :param num_1: int
    :param num_2: int
    :return: a * b (int)
    """
    return a * b


list_a = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(mult_nums, list_a))
# print(mult_nums.__doc__)

