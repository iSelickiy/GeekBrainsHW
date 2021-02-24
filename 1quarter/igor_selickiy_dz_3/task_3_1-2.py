# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
# реализовать корректную работу с числительными, начинающимися с заглавной буквы
def num_translate(num_input):
    number_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'Пять', 
    'six': 'Шесть', 'seven': 'Семь', 'eight': 'Восемь', 'nine': 'Девять', 'ten': 'Десять'}
    if num_input in number_dict:
        return number_dict[num_input]
    elif num_input.istitle() and (num_input.lower() in number_dict):
        return number_dict[num_input.lower()].title()
    else:
        return None

num_input = num_translate(input('Print number for translate: '))
print(num_input)
