# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

# Решения через list
num_month_list = int(input('Введите порядковое число месяца: '))
a_list_season = ['Зима', 'Весна', 'Лето', 'Осень']

if num_month_list == 1 or num_month_list == 2 or num_month_list == 12:
    print('Время года -', a_list_season[0])
elif num_month_list == 3 or num_month_list == 4 or num_month_list == 5:
    print('Время года -', a_list_season[1])
elif num_month_list == 6 or num_month_list == 7 or num_month_list == 8:
    print('Время года -', a_list_season[2])
elif num_month_list == 9 or num_month_list == 10 or num_month_list == 11:
    print('Время года -', a_list_season[3])
else:
    print('Вы ввели неверное порядковое число месяца, в году 12 месяцев')


# Решения через dict

num_month_dict = int(input('Введите порядковое число месяца: '))
season_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень',
               10: 'Осень', 11: 'Осень', 12: 'Зима'}
# print('Время года -', season_dict[num_month_dict]) - еще был вариант сделать так
print('Время года -', season_dict.get(num_month_dict))