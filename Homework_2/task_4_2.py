# 4.Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

sentence_str = input("Введите несколько слов разделенныеми пробелами: ")

for num, i in enumerate(sentence_str.split(), 1):
    if len(i) < 10:
        print(f'#{num}: {i}')
    else:
        print(f'#{num}: {i[0:10]}')