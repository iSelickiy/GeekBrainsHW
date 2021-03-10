# 1. Написать генератор нечётных чисел от 1 до n (включительно), без использования ключевого слова yield, полностью истощить генератор. Например:
# Без использования ключевого слова yield: генератор нечётных чисел от 1 до n (включительно), для чисел, квадрат которых меньше 200.

n = 15

iterator_without_yield = (el for el in range(1, n + 1, 2) if el ** 2 < 200)

for el in range(1, n):
    print(next(iterator_without_yield))

print(next(iterator_without_yield))