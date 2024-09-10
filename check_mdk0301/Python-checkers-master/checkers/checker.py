# Импорт перечислений из модуля enums для типов шашек
from checkers.enums import CheckerType
# Класс Checker представляет собой абстракцию шашки в игре Шашки
class Checker:
    def __init__(self, type: CheckerType = CheckerType.NONE):
        # Инициализирует новый экземпляр класса Checker.
        :param type: Тип шашки (по умолчанию NONE)
        # Атрибут типа шашки, защищен приватным методом
        self.__type = type
    @property
    def type(self):
        return self.__type

    def change_type(self, type: CheckerType):
        # Изменяет тип существующей шашки.
        :param type: Новый тип шашки (CheckerType)
        # Изменяет внутреннее состояние шашки
        self.__type = type