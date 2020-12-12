"""
2. Инкапсулировать оба параметра (название и цену)
товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы
будет сгенерирована ошибка выполнения.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'Название: {self.__name}\n' \
               f'Цена: {self.__price}'  # AttributeError
        # return f'Название: {self._ItemDiscount__name}\n' \
        #        f'Цена: {self._ItemDiscount__price}'


item = ItemDiscountReport('Стол', 5000)
print(item.get_parent_data())
