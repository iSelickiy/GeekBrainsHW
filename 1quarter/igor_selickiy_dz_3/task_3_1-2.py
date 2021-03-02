# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
# реализовать корректную работу с числительными, начинающимися с заглавной буквы
def num_translate(num_input, number_dict):    
    if num_input in number_dict:
        return number_dict[num_input]
    elif num_input.istitle() and (num_input.lower() in number_dict):
        return number_dict[num_input.lower()].title()
    else:
        return None

number_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 
    'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
num_input = num_translate(input('Print number for translate: '), number_dict)
print(num_input)
