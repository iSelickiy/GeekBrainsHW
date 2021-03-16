# 3. Написать декоратор для логирования типов позиционных аргументов функции
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; 
# можете ли вы вывести тип значения функции? 
# Сможете ли решить задачу для именованных аргументов? 
# Сможете ли вы замаскировать работу декоратора?
from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = str(func).split()[1]
        res = ', '.join(f'{func_name} ({i}: {type(i)})' for i in args)
        return(res)
    return wrapper
    

@type_logger
def calc_cube(x):
   return x ** 3
