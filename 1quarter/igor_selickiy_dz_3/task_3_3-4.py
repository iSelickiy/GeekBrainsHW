# Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате 
# «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, 
# а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, 
# в которых фамилия начинается с соответствующей буквы.
# Сможете ли вы вернуть отсортированный по ключам словарь?
# --------------------------------------------
# 1-ая часть
# name_list = ["Иван", "Мария", "Петр", "Илья"]
# name_dict = {}
# for elem in name_list:
#     if not name_dict.get(elem[0]):
#         name_dict[elem[0]] = [elem]
#     else:
#         name_dict[elem[0]].append(elem)
# print(name_dict)
# --------------------------------------------

def thesaurus_adv(full_names):
    full_name_dict = {}
    for elem in full_names:
        split_name = elem.split(' ')
        name = split_name[0]
        surname = split_name[1]
        if not full_name_dict.get(surname[0]):
            full_name_dict[surname[0]] = {}
        if not full_name_dict[surname[0]].get(name[0]):
            full_name_dict[surname[0]][name[0]] = []
        full_name_dict[surname[0]][name[0]].append(elem)
    sort_dict = {}
    for surn_letter in sorted(full_name_dict.keys()):
        sort_dict[surn_letter] = {}
        for name_letter in sorted(full_name_dict[surn_letter].keys()):
            sort_dict[surn_letter][name_letter] = full_name_dict[surn_letter][name_letter]
    return sort_dict


full_names = ["Иван Сергеев", "Алла Сидорова", "Инна Серова", "Петр Алексеев", 
                "Илья Иванов", "Анна Савельева", "Василий Суриков"]    

print(thesaurus_adv(full_names))
