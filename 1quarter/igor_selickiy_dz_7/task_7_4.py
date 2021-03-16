# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница размера файла (пусть будет кратна 10), 
# а значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0)
import os

file_stat = {100: 0, 1000: 0, 10000: 0, 100000: 0}

for paths, dirnames, files in os.walk('some_data'):
    for file in os.scandir(paths):
        file_size = file.stat().st_size
        if file_size <= 100: file_stat[100] += 1
        elif file_size > 100 and file_size <= 1000: file_stat[1000] += 1
        elif file_size > 1000 and file_size <= 10000: file_stat[10000] += 1
        elif file_size > 10000 and file_size <= 100000: file_stat[100000] += 1

print(file_stat)  
