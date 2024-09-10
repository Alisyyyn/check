# Импорт Enum и auto из модуля enum
from enum import Enum, auto

# Перечисление для определения сторон игроков
class SideType(Enum):
    WHITE = auto()
    BLACK = auto()

    # Статический метод для получения противоположной стороны
    @staticmethod
    def opposite(side):
        if side == SideType.WHITE:
            return SideType.BLACK
        elif side == SideType.BLACK:
            return SideType.WHITE
        else:
            raise ValueError()

# Перечисление для определения типов шашек
class CheckerType(Enum):
    NONE = auto()
    WHITE_REGULAR = auto()
    BLACK_REGULAR = auto()
    WHITE_QUEEN = auto()
    BLACK_QUEEN = auto()