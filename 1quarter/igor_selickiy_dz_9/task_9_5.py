# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery():

    def __init__(self, title):
        self._title = title


    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):

    def draw(self):
        return f'Запуск отрисовки {self._title}'


class Pencil(Stationery):

    def draw(self):
        return f'Запуск отрисовки {self._title}'


class Handle(Stationery):

    def draw(self):
        return f'Запуск отрисовки {self._title}'


# test

# pen = Pen(title = 'Ручка')
# pencil = Pencil(title = 'Карандаш')
# handle = Handle(title = 'Маркер')

# print(pen.draw())
# print(pencil.draw())
# print(handle.draw())