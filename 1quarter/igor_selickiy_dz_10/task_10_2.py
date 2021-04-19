# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. 
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название. 
# К типам одежды в этом проекте относятся пальто и костюм. 
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: 
# для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. 
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def calc(self):
        pass

class Coat(Clothes):

    type = 'Пальто'

    def calc(self, V, quant):
        return (V/6.5 + 0.5)*quant


    @property
    def show_type(self):
        return self.type


class Suit(Clothes):

    type = 'Костюм'

    def calc(self, H, quant):
        return (2*H + 0.3)*quant


    @property
    def show_type(self):
        return self.type
# Tests
c1 = Coat()
print(c1.calc(V = 15, quant = 15))
print(c1.show_type)
s1 = Suit()
print(s1.calc(H = 160, quant = 10))
print(s1.show_type)
