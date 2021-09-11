# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике
# полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class MyClothes(ABC):

    def __init__(self, some_param):
        self.some_param = some_param

    @abstractmethod
    def fabric_consuption(self):
        pass


class Suit(MyClothes):

    @property
    def fabric_consuption(self):
        return f'Расход ткани на костюм - {round(2 * self.some_param + 0.3)}'


class Coat(MyClothes):

    @property
    def fabric_consuption(self):
        return f'Расход ткани на пальто- {round(self.some_param / 6.5 + 0.5)}'


suit = Suit(1.96)
coat = Coat(50)
print(suit.fabric_consuption)
print(coat.fabric_consuption)


