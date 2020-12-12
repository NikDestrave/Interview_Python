"""
Задание 2.	Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath):

Функция принимает имя каталога и распечатывает его содержимое
в виде «путь и имя файла», а также любые другие
файлы во вложенных каталогах.

Эта функция подобна os.walk. Использовать функцию os.walk
нельзя. Данная задача показывает ваше умение работать с
вложенными структурами.
заполните далее
"""

import os


def print_directory_contents(sPath):
    def files_get(sPath):
        struct = []
        for file_dir in os.listdir(sPath):
            full_name = os.path.join(os.path.abspath(sPath), file_dir)
            if os.path.isfile(full_name):
                struct.append((os.path.abspath(sPath), file_dir))
            else:
                struct.extend(files_get(full_name))
        return struct

    return files_get(sPath)


my_res = print_directory_contents('mainapp')
print(my_res)
