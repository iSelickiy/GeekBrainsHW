# Представлен список чисел. Определить элементы списка, не имеющие повторений. 
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке
# Используйте генераторы или генераторные выражения.
# Сначала найдите способ определить уникальность элемента в списке. Подумайте о сохранении порядка исходного списка.

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

gen1 = (elem for elem in src if src.count(elem) == 1)
result = [*gen1]
print(result)