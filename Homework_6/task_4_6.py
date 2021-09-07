# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
# (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Скорость {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')
        else:
            print(f'Скорость {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')
        else:
            print(f'Скорость {self.speed}')


class PoliceCar(Car):
    pass


townCar = TownCar(40, 'red', 'BMW')
sportCar = SportCar(200, 'red', 'Audi')
workCar = WorkCar(35, 'red', 'Ford')
policeCar = PoliceCar(70, 'red', 'Lada')

townCar.show_speed()
workCar.show_speed()
sportCar.turn('направо')
print(policeCar.name)



