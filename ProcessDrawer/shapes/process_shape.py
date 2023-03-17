import svgwrite
from svgwrite import shapes

from .base import BaseShape


class ProcessShape(BaseShape):
    size = (50, 50)
    spacing = 50

    def draw(self, dwg: svgwrite.Drawing, pos: tuple[int, int], **extra):
        pos = pos[0] + self.size[0] // 2, pos[1] + self.size[1] // 2
        rect = svgwrite.shapes.Circle(pos, self.size[0] // 2, fill="#FFFFFF", stroke="#0000AA", stroke_width=3)
        dwg.add(rect)

        name = extra.get('name')
        if name is not None:
            dwg.add(dwg.text(name, pos))
