# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open('text_salary.txt') as file:
    list_a = file.read()
    salary = []
    employess = []
    for elem in list_a.split('\n'):
        i = elem.split()
        salary.append(i[1])
        if int(i[1]) < 20000:
           employess.append(i[0])
           list_emloyess = ', '.join(employess)

print('Оклад меньше 20 тысяч у сотрудника(ов): ', list_emloyess)
print('Средняя величина дохода сотрудника: ', sum(map(int, salary)) / len(salary))

