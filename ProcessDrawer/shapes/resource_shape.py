import svgwrite
from svgwrite import shapes

from .base import BaseShape


class ResourceShape(BaseShape):
    size = (50, 50)
    spacing = 50

    def draw(self, dwg: svgwrite.Drawing, pos: tuple[int, int], **extra):
        rect = svgwrite.shapes.Rect(pos, self.size, fill="#FFFFFF", stroke="#AA0000", stroke_width=3)
        dwg.add(rect)

        name = extra.get('name')
        if name is not None:
            dwg.add(dwg.text(name, pos))
