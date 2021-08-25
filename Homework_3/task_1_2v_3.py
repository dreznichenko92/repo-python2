# 1. done Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.


def my_func_division(num_1, num_2):
    """
        Функция my_func_division принимающая два числа (позиционные аргументы) и выполняющая их деление.
        Предусмотрена обработка ситуации деления на ноль
        :param num_1: int
        :param num_2: int
        :return: division (int)
        """
    try:
        division = num_1 // num_2
    except ZeroDivisionError:
        return 'На ноль делить нельзя'

    return division


user_num_1 = int(input('Введите число числителя: '))
user_num_2 = int(input('Введите число знаменателя: '))

print(my_func_division(user_num_1, user_num_2))
# print(my_func_division.__doc__)