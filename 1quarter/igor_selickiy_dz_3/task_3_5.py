# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков:
# Документировать код функции.
import random 

def get_jokes(joke_count, *args):
    '''
    Create random count of random jokes from list of words
    :param joke_count: count of jokes
    :param args: tuples with words
    :return: joke 
    '''    
    for item in range(0, joke_count):
        joke = []
        for elem in args:
            joke.append(elem[random.randint(0, len(elem) - 1)])
        print(' '.join(joke))

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

get_jokes(3, nouns, adverbs, adjectives)
