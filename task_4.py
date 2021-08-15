number = int(input("Введите число: "))
maxnumber = -1

while number > 0:
    num = number % 10
    maxnumber = max(maxnumber, num)
    number //= 10
print(maxnumber)