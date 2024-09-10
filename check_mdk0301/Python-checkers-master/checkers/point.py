# Класс Point представляет точку в двумерной системе координат
class Point:
    def __init__(self, x: int = -1, y: int = -1):
        """
        Инициализация точки.

        :param x: Координата x (по умолчанию -1 для неопределенной)
        :param y: Координата y (по умолчанию -1 для неопределенной)
        """
        self.__x = x
        self.__y = y

    # Свойства для доступа к координатам
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    # Метод сравнения объектов Point
    def __eq__(self, other):
        if isinstance(other, Point):
            return (
                    self.x == other.x and
                    self.y == other.y
            )

        return NotImplemented