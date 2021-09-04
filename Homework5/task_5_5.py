# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

num = '1 2 3 4 5 6 7 8 9 10 7 666.90'
with open('text_5.txt', 'w') as file:
    file.writelines(num)

with open('text_5.txt') as file:
    sum_num = file.readlines()
    for i in sum_num:
        num = i.split()
    print(sum(map(float, num)))
