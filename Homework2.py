# Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число неверное,
# и говорите о диапазоне допустимых. И просите ввести заново.
# Допустим, пользователь ввел 2, оно подходит. Возводим его в степень 2 и выводим 4.

# while True:
#     number = int(input("Введите число: "))
#     if number > 0 and number < 10:
#         print(number ** 2)
#         break
#     else:
#         print("Число должно быть >0 и <10")


a = 10
b = 15
print("Переменные a и b - ", a, b)
string1 = input("Введите первую строку ")
number1 = int(input("Введите первое число "))
string2 = input("Введите вторую строку ")
number2 = int(input("Введите второе число "))
print("Введеные значения - %10s %5d %10s %5d" % (string1, number1, string2, number2))