import abc

import svgwrite


class BaseShape(abc.ABC):
    size = (0, 0)
    spacing = 0

    @abc.abstractmethod
    def draw(self, dwg: svgwrite.Drawing, pos: tuple[int, int], **extra):
        pass
