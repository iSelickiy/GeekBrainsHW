# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road():

    def __init__(self, length, width):
        try:
            self.__length = int(length)
        except: raise ValueError('Length must be number')
        try:
            self.__width = width
        except: raise ValueError('Width must be number')
        self.__asph_mass = 25
        self.__asph_thick = 5

    def road_calc(self):
        return int((self.__asph_mass*self.__asph_thick*self.__length*self.__width)/100)

# test
# a = Road(20, 500)
# print(a.road_calc())
# res 12500

