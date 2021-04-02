# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). 
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) 
# должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. 
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.


class Car():
    def __init__(self, speed, color, name, is_police = False):
        self.__speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    

    def go(self):
        return f'Car start ride'
    

    def stop(self):
        return f'Car stop ride'

    
    def turn_direct(self, direct):
        return f'car turn to {direct}'

    
    def show_speed(self):
        return f'car speed: {self.__speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        self.car_type = 'towncar'
        super().__init__(speed, color, name, is_police)


    def show_speed(self):
        if self._Car__speed > 60:
            return f'overspeed'
        else:
            return super().show_speed()


class SportCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        self.car_type = 'sportcar'
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        self.car_type = 'workcar'
        super().__init__(speed, color, name, is_police)


    def show_speed(self):
        if self._Car__speed > 40:
            return f'overspeed'
        else:
            return super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        self.car_type = 'PoliceCar'
        self.is_police = True
        super().__init__(speed, color, name, is_police = self.is_police)





# Test
# cart = WorkCar(speed = 50, color = 'red', name = 'red')
# print(cart.is_police)
# print(cart.turn_direct('left'))
# print(cart.show_speed())

