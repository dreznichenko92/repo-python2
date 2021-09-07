# 1. Создать класс TrafficLight (светофор)
# и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния
# (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между
# режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
from time import sleep

class TrafficLight:
    __color = ('Red', 'Yellow', 'Green')
    __time = (7, 5, 2)

    def running(self):
        i = 0
        while i < 3:
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(TrafficLight.__time[0])
            elif i == 1:
                sleep(TrafficLight.__time[1])
            elif i == 2:
                sleep(TrafficLight.__time[2])
            i += 1

TrafficLight = TrafficLight()
TrafficLight.running()

