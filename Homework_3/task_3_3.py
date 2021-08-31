# 3. done Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func_sum_max(x, y, z, *args, **kwargs):
    """
    Функция my_func_sum_max принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
    :param *args: запаковывает лишние аргуемнты в кортеж
    :param **kwargs: запаковывает лишние аргуемнты в виде словаря
    :param x: int
    :param y: int
    :param z: int
    :return: sum_max
    """
    list_1 = [x, y, z]
    list_2 = []

    max_1 = max(list_1)
    list_2.append(max_1)
    list_1.remove(max_1)
    max_2 = max(list_1)
    list_2.append(max_2)
    sum_max = sum(list_2)

    return sum_max


print(my_func_sum_max(98, 0, 1))
# print(my_func_sum_max.__doc__)