"""
Задание 3. Разработать генератор случайных чисел.
В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить). Заполнить этими данными список и словарь.
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
Вывести содержимое созданных списка и словаря.
"""

import random


def gen_numbers(start, finish):
    list_numbers = []
    dict_numbers = {}
    for _ in range(10):
        rnd = int((finish - start) * random.random() + start)
        list_numbers.append(rnd)
        dict_numbers.update({f'elem_{rnd}': rnd})

    return list_numbers, dict_numbers


print(gen_numbers(13, 66))
