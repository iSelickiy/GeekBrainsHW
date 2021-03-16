# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при хранении данных используется принцип: 
# одна строка — один пользователь, разделитель между значениями — запятая. 
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. 
# Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, то для оставшихся ФИО значение в словаре - None.
# Если наоборот — формируем словарь, исходя из количества ФИО и выходим из скрипта с кодом «1». Примечание: При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.

# ПЕРЕДЕЛАТЬ ПУТИ В CSV

def name_to_hobby(names, hobbys):
    res = {}
    for elem in range(0, len(names)):
        if elem >= len(hobbys):
            res[names[elem]] = None
        else:
            res[names[elem]] = hobbys[elem]
    if len(hobbys) > len(names):
        return 1
    with open('res.csv', 'w', encoding='utf-8') as f:
        for key, value in res.items():
            f.write(f'{key} : {value}\n')
    return res


with open('names.csv', 'r', encoding='utf-8') as f:
    name_list = [name.strip().replace(',', ' ') for name in f]
with open('hobby.csv', 'r', encoding='utf-8') as f:
    hobby_list = [hobby.strip() for hobby in f]

print(name_to_hobby(name_list, hobby_list))
