from svgwrite import shapes, Drawing, rgb

from .shapes import ProcessShape, ResourceShape, BaseShape


class ProcessDrawer:
    @staticmethod
    def _generate_data(count: int, name_format: str) -> list[dict]:
        return [{'name': name_format.format(i + 1), 'pos': None} for i in range(count)]

    @staticmethod
    def _calc_pos(offset: tuple[int, int], shape: BaseShape, i: int) -> tuple[int, int]:
        return offset[0] + i * (shape.size[0] + shape.spacing), offset[1]

    def __init__(self,
                 resources_count: int = 0,
                 processes_count: int = 0,
                 resources: list[dict] = None,
                 processes: list[dict] = None,
                 v_spacing: int = 100) -> None:
        self._resources = resources if resources is not None else self._generate_data(resources_count, "R{}")
        self._processes = processes if processes is not None else self._generate_data(processes_count, "P{}")

        self._v_spacing = v_spacing

        self._image_size = (0, 0)
        self._p_offset = (0, 0)
        self._r_offset = (0, 0)

        self._process_shape = ProcessShape()
        self._resource_shape = ResourceShape()

        self._recalculate_size()
        self._recalculate_positions()

    def draw(self) -> None:
        dwg = Drawing('test.svg', profile='tiny', size=self._image_size)

        for r in self._resources:
            self._resource_shape.draw(dwg, **r)

        for p in self._processes:
            self._process_shape.draw(dwg, **p)

        dwg.save()

    def _recalculate_size(self) -> None:
        p_width = len(self._processes) * (self._process_shape.size[0] + self._process_shape.spacing)
        r_width = len(self._resources) * (self._resource_shape.size[0] + self._resource_shape.spacing)
        height = 2 * self._v_spacing + self._process_shape.size[1] + self._resource_shape.size[1]

        self._image_size = (max(p_width, r_width), height)
        self._r_offset = ((self._image_size[0] - r_width + self._resource_shape.spacing) // 2, self._v_spacing // 2)
        self._p_offset = ((self._image_size[0] - p_width + self._process_shape.spacing) // 2,
                          self._v_spacing // 2 + self._v_spacing)

    def _recalculate_positions(self) -> None:
        for i in range(len(self._resources)):
            pos = self._calc_pos(self._r_offset, self._resource_shape, i)
            self._resources[i]['pos'] = pos

        for i in range(len(self._processes)):
            pos = self._calc_pos(self._p_offset, self._process_shape, i)
            self._processes[i]['pos'] = pos
