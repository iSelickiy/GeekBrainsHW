# Для чтения данных реализовать в командной строке следующую логику. Предполагаем, что первая запись имеет номер 1.
# 1) просто запуск скрипта — выводить все записи;
# 2) запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# 3) запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму числу, включительно;
# Усложнение Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.

from sys import argv

def show_sales(range_1 = 0, range_2 = None):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for idx in range(0, range_2):
            if idx in range(range_1, range_2): 
                yield f.readline().strip()
            else:
                f.readline()


def print_sales(rng_1 = 0,rng_2 = None):
    if not rng_2:
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            rng_2 = sum(1 for line in f)
    if rng_1: rng_1 -= 1
    gen = show_sales(range_1=rng_1, range_2=rng_2)
    for i in range(rng_1, rng_2):
            print(next(gen))


if len(argv) == 1: print_sales()
elif len(argv) == 2: print_sales(rng_1=int(argv[1]))
elif len(argv) == 3: print_sales(rng_1=int(argv[1]), rng_2=int(argv[2]))
else: print('Error')   
