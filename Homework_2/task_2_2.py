# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

a_list = input('Введите элемента списка через пробел: ')
b_list = a_list.split()
elem = 0

for i in range(int(len(b_list) / 2)):
    b_list[elem],b_list[elem + 1] = b_list[elem + 1], b_list[elem]
    elem = elem + 2

print(b_list)