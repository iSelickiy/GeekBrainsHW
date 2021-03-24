# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), 
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

import random

class Matrix:

    def __init__(self, matrix: list):
        self.matrix = matrix
        self.res = []

    def matrix_gen(self):
        res = []
        for elem in self.matrix:
            col = elem[0]
            row = elem[1]
            res += [[random.randrange(0, 10) for a in range(col)] for b in range(row)]
        return res


    def matrix_to_str(self):
        self.res += [f'| {" ".join(map(str, i))} |' for i in self.matrix_gen()]
        return self.res

    
    def __str__(self):
        res = self.matrix_to_str()
        res_return = '\n'.join(res)
        return res_return
        
#test
matr = Matrix([3,2],[4,3],[2,4])
print(matr)
