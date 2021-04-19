

# 4. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». 
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. 
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров. 
# Проверьте корректность полученного результата.

class ComplexNum:

    def __init__(self, num: int):
        self.__num = complex(num)

    def __str__(self):
        return str(self.__num)

    def __add__(self, num: int):
        num.num = complex(str(num))
        return self.__num + num.num
    
    def __mul__(self, num: int):
        num.num = complex(str(num))
        return self.__num * num.num


#test
a = complex(2)
b = complex(3)
print(f'{a+b}/{a*b}')


a = ComplexNum(2)
b = ComplexNum(3)
print(f'{a+b}/{a*b}')