# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

# Получаем количество строк в файле:
with open('text_2.txt', encoding='utf-8') as file:
    content = file.readlines()
    print(f'Количество строк в файле - {len(content)}')

# Получаем количество слов в каждой строке файла:
with open('text_2.txt', encoding='utf-8') as file:
    for num, elem in enumerate((file), 1):
        number_of_words = len(elem.split())
        print(f'В строке № {num} количество слов - {number_of_words}')
