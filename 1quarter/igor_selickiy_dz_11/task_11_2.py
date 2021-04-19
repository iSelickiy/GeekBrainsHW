# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
# Проверьте его работу на данных, вводимых пользователем. 
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyZeroDivision(ZeroDivisionError):

    def __str__(self) -> str:
        return f'ZeroDivisionError'

class MyClass:

    def __init__(self,num: int):
        self.num = int(num)

    def __truediv__(self, num: int):
        try:
            if num.num == 0:
                raise MyZeroDivision
            else: 
                return self.num / num.num
        except MyZeroDivision as e:
            print(e)
            return 0

    def __floordiv__(self, num: int):
        try:
            if num.num == 0:
                raise MyZeroDivision
            else: 
                return self.num // num.num
        except MyZeroDivision as e:
            print(e)
            return 0

    def __str__(self):
        return str(self.num)


#Tests
a = MyClass(1)
b = MyClass(2)

print(f'{a/b}\n{a//b}')

b = MyClass(0)
print(f'{a/b}\n{a//b}')





