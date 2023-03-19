import svgwrite
from svgwrite import shapes

from . import PosUtils

class ConfigDrawer:
    def __init__(self, config: dict) -> None:
        self._img_size = config['image']['size']

        self._proc_rad = config['image']['process']['radius']
        self._res_size = config['image']['resource']['size']

        self._proc_data = config['image']['process']
        self._res_data = config['image']['resource']
        self._arrow_data = config['image']['arrow']

        self._resources = config['resources']
        self._processes = config['processes']

    def draw(self, proc_matr: list[list[int]], res_matr: list[list[int]]) -> None:
        dwg = svgwrite.Drawing("test.svg", size=self._img_size)

        for res in self._resources:
            self._draw_resource(dwg, res)

        for proc in self._processes:
            self._draw_process(dwg, proc)

        for ri, res in enumerate(res_matr):
            for pi, proc in enumerate(res):
                if proc == 1:
                    self._draw_arrow(dwg, self._get_res_position(ri, pi), self._get_proc_position(pi, ri))

        for pi, proc in enumerate(proc_matr):
            for ri, res in enumerate(proc):
                if res == 1:
                    self._draw_arrow(dwg, self._get_proc_position(pi, ri), self._get_res_position(ri, pi))

        dwg.save()

    def _draw_resource(self, dwg: svgwrite.Drawing, res: dict) -> None:
        c_pos = (res['pos'][0] - self._res_size[0] // 2, res['pos'][1] - self._res_size[1] // 2)
        rect = svgwrite.shapes.Rect(c_pos,
                                    self._res_size,
                                    fill=self._res_data['fill_color'],
                                    stroke=self._res_data['stroke_color'],
                                    stroke_width=self._res_data['stroke_width'])
        dwg.add(rect)
        dwg.add(dwg.text(res['name'], res['pos']))

    def _draw_process(self, dwg: svgwrite.Drawing, proc: dict) -> None:
        circle = shapes.Circle(proc['pos'],
                               self._proc_rad,
                               fill=self._proc_data['fill_color'],
                               stroke=self._proc_data['stroke_color'],
                               stroke_width=self._proc_data['stroke_width'])
        dwg.add(circle)
        dwg.add(dwg.text(proc['name'], proc['pos']))

    def _draw_arrow(self, dwg: svgwrite.Drawing, src: tuple[int, int], dst: tuple[int, int]):
        line = shapes.Line(src, dst, stroke="#000000", stroke_width=2)
        dwg.add(line)
        dwg.add(shapes.Circle(dst, 5))

    def _get_res_position(self, ri: int, pi: int) -> tuple[int, int]:
        src = self._resources[ri]['pos']
        dst = self._processes[pi]['pos']

        return PosUtils.square_edge_intersection(src, self._res_size, dst)

    def _get_proc_position(self, pi, ri):
        src = self._processes[pi]['pos']
        dst = self._resources[ri]['pos']

        return PosUtils.circle_edge_intersection(src, self._proc_rad, dst)
