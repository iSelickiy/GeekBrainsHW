# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. 
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». 
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
# Проверить работу полученной структуры на реальных данных.

class Date:

    def __init__(self, date):
        self.__date = date

    def __str__(self) -> str:
        return str(self.__date)

    @classmethod
    def date_to_int(cls, param):
        date_lst = str(param).split('-')
        if len(date_lst) == 3: return map(int, date_lst)
        else: return 'invalid date'


    @staticmethod
    def valid(day: int, mounth: int, year: int):
        if day not in range(1,31): return 'invalid day'
        elif mounth not in range(1,12): return 'invalid mounth'
        elif year not in range(0, 9999): return 'invalid year'
        else: return 'All good'
        
#test
a = Date('15-10-2021')
print(Date.valid(*Date.date_to_int(a)))


    