# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: 
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника 
# (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: 
# создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker():
    
    def __init__(self, name, surn, pos, wage, bonus):
        self.name = name
        self.surname = surn
        self.position = pos
        self.__income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f'Name: {self.name}, Surname: {self.surname}'


    def get_total_income(self):
        income = self._Worker__income
        return f'Total wage: {income["wage"] + income["bonus"]}'

# test
# igor = Position(nam = 'Igor', surn = 'Selickiy', pos = 'Programmer', wage = 30000, bonus = 10000)
# print(igor.get_full_name())
# print(igor.get_total_income())

