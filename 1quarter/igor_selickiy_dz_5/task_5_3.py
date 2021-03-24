# 3. Есть два списка, Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>)
# Количество генерируемых кортежей не должно быть больше длины списка tutors. 
# Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None)
# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.

def klass_gen(tutors, klasses):
    for elem in range(0, len(tutors)):
        if elem < len(klasses):
            yield tutors[elem], klasses[elem]
        else:
            yield tutors[0], None

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]

gen1 = klass_gen(tutors, klasses)
print(type(gen1))

for elem in range(0, len(tutors)):
    print(next(gen1))
