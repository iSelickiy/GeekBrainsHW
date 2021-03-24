# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates

import os
import shutil

templ_path = os.path.join(os.getcwd(), 'my_project' ,'templates')
for paths, dirs, files in os.walk('my_project'):
    if dirs:
        dir_name = dirs[0].strip()
    if 'templates' in paths and not dirs:
        try:
            print(paths)
            shutil.copytree(paths, f'{templ_path}/{dir_name}')
        except: pass
