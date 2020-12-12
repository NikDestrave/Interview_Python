"""
6. Проверить на практике возможности полиморфизма.

Необходимо разделить дочерний класс ItemDiscountReport на два класса.

Инициализировать классы необязательно.

Внутри каждого поместить функцию get_info,
которая в первом классе будет отвечать за вывод названия товара,
а вторая — его цены.

Далее реализовать выполнение каждой из функции тремя способами.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport_1(ItemDiscount):
    def get_info(self):
        return f'Название: {self.name}'


class ItemDiscountReport_2(ItemDiscount):
    def get_info(self):
        return f'Цена: {self.price} р.\n'


# Вариант №1
item_1 = ItemDiscountReport_1('Стол', 5000)
print(item_1.get_info())

item_2 = ItemDiscountReport_2('Стул', 1500)
print(item_2.get_info())


# Вариант №2
def objs(obj):
    return obj.get_info()


print(objs(item_1))
print(objs(item_2))


# Вариант №3
for item in (item_1, item_2):
    print(item.get_info())
