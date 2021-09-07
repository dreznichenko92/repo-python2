# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

translator_rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []

with open('text_4.txt') as file:
    file_rus = file.readlines()
    for i in file_rus:
        i = i.split(' — ')
        new_file.append(translator_rus[i[0]] + ' — ' + i[1])

with open('text_4_rus.txt', 'w') as file:
    file.writelines(new_file)

# Проверка
with open('text_4_rus.txt') as file:
    print(file.read())
