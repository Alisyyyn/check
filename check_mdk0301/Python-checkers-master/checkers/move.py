# Класс Move представляет возможное движение шашки
class Move:
    def __init__(self, from_x: int = -1, from_y: int = -1, to_x: int = -1, to_y: int = -1):
        """
        Инициализация движения шашки.

        :param from_x: Начальная координата x (-1 для неопределенного)
        :param from_y: Начальная координата y (-1 для неопределенного)
        :param to_x: Конечная координата x (-1 для неопределенного)
        :param to_y: Конечная координата y (-1 для неопределенного)
        """
        self.__from_x = from_x
        self.__from_y = from_y
        self.__to_x = to_x
        self.__to_y = to_y

    # Свойства для доступа к координатам движения
    @property
    def from_x(self):
        return self.__from_x

    @property
    def from_y(self):
        return self.__from_y

    @property
    def to_x(self):
        return self.__to_x

    @property
    def to_y(self):
        return self.__to_y

    # Строковое представление движения
    def __str__(self):
        return f'{self.from_x}-{self.from_y} -> {self.to_x}-{self.to_y}'

    # Репрезентативное строковое представление
    def __repr__(self):
        return f'{self.from_x}-{self.from_y} -> {self.to_x}-{self.to_y}'

    # Метод сравнения объектов Move
    def __eq__(self, other):
        if isinstance(other, Move):
            return (
                    self.from_x == other.from_x and
                    self.from_y == other.from_y and
                    self.to_x == other.to_x and
                    self.to_y == other.to_y
            )
        return NotImplemented