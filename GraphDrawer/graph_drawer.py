import math

import svgwrite
from svgwrite import shapes, path as svgpath

from . import PosUtils


class GraphDrawer:
    def __init__(self, config: dict) -> None:
        self._img_size = config['image']['size']

        self._proc_rad = config['image']['process']['radius']
        self._res_size = config['image']['resource']['size']

        self._proc_data = config['image']['process']
        self._res_data = config['image']['resource']
        self._arrow_data = config['image']['arrow']

        self._resources = config['resources']
        self._processes = config['processes']

    def draw(self, proc_matr: list[list[int]], res_matr: list[list[int]]) -> svgwrite.Drawing:
        dwg = svgwrite.Drawing(size=self._img_size)

        for res in self._resources:
            self._draw_resource(dwg, res)

        for proc in self._processes:
            self._draw_process(dwg, proc)

        for ri, res in enumerate(res_matr):
            for pi, proc in enumerate(res):
                if proc != 0:
                    self._draw_arrow(dwg,
                                     self._get_res_position(ri, pi),
                                     self._get_proc_position(pi, ri),
                                     proc < 0)

        for pi, proc in enumerate(proc_matr):
            for ri, res in enumerate(proc):
                if res != 0:
                    self._draw_arrow(dwg,
                                     self._get_proc_position(pi, ri),
                                     self._get_res_position(ri, pi),
                                     res < 0)

        return dwg

    def _draw_resource(self, dwg: svgwrite.Drawing, res: dict) -> None:
        c_pos = (res['pos'][0] - self._res_size[0] // 2, res['pos'][1] - self._res_size[1] // 2)
        rect = svgwrite.shapes.Rect(c_pos,
                                    self._res_size,
                                    fill=self._res_data['fill_color'],
                                    stroke=self._res_data['stroke_color'],
                                    stroke_width=self._res_data['stroke_width'])
        dwg.add(rect)
        dwg.add(dwg.text(res['name'], res['pos'], dominant_baseline="middle", text_anchor="middle"))

    def _draw_process(self, dwg: svgwrite.Drawing, proc: dict) -> None:
        circle = shapes.Circle(proc['pos'],
                               self._proc_rad,
                               fill=self._proc_data['fill_color'],
                               stroke=self._proc_data['stroke_color'],
                               stroke_width=self._proc_data['stroke_width'])
        dwg.add(circle)
        dwg.add(dwg.text(proc['name'], proc['pos'], dominant_baseline="middle", text_anchor="middle"))

    def _get_res_position(self, ri: int, pi: int) -> tuple[int, int]:
        src = self._resources[ri]['pos']
        dst = self._processes[pi]['pos']

        return PosUtils.square_edge_intersection(src, self._res_size, dst)

    def _get_proc_position(self, pi: int, ri: int) -> tuple[int, int]:
        src = self._processes[pi]['pos']
        dst = self._resources[ri]['pos']

        return PosUtils.circle_edge_intersection(src, self._proc_rad, dst)

    def _draw_arrow(self,
                    dwg: svgwrite.Drawing,
                    src: tuple[int, int],
                    dst: tuple[int, int],
                    in_loop: bool = False) -> None:
        vx, vy = dst[0] - src[0], dst[1] - src[1]
        d = math.sqrt(pow(vx, 2) + pow(vy, 2))

        angle = math.degrees(math.acos(vx / d))
        angle *= -1 if vy < 0 else 1

        color = self._arrow_data.get('color', "black") \
            if not in_loop else self._arrow_data.get('loop_color', "black")

        x0, y0 = src[0], src[1]
        x1, y1 = src[0] + d, src[1]
        h1 = (0, -d // 4) if self._arrow_data.get('curved', False) else (0, 0)
        h2 = (d // 4, 0) if self._arrow_data.get('curved', False) else (0, 0)
        arrow = self._arrow_data['size']
        commands = [
            f"M {x0} {y0}",
            f"C {x0 + h1[0]} {y0 + h1[1]} {x0 + h2[0]} {y0 + h2[1]} {x1}, {y1}",
            f"L {x1 - arrow[0]} {y1 + arrow[1]} M {x1} {y1} L {x1 - arrow[0]} {y1 - arrow[1]}"
        ]
        path = svgpath.Path(' '.join(commands),
                            fill="none",
                            stroke=color,
                            stroke_width=self._arrow_data.get('thickness', 1),
                            transform=f"rotate({angle}, {src[0]}, {src[1]})")
        dwg.add(path)
