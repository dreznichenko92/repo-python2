# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('text_user.txt', 'w', encoding='utf-8') as file:
    text_user = input('Введите текст: \n')
    while text_user:
        file.write(f' {text_user} \n')
        text_user = input('Введите текст: \n')
        if not text_user:
            break
