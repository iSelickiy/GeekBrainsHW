# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
import os

some_dirs = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for key, values in some_dirs.items():
    if not os.path.exists(key):
        os.mkdir(key)
    for value in values:
        if not os.path.exists(f'{key}/{value}'):
            os.makedirs(f'{key}/{value}')
