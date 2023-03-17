class UnitData:
    def __init__(self,
                 size: tuple[int] = None,
                 spacing: int = None,
                 color: str = None,
                 outline_color: str = None,
                 outline_thickness: int = 1):
        self.size = size if size is not None else (50, 50)
        self.spacing = spacing if spacing is not None else self.size[0] // 2

        self.color = color if color is not None else "#AAAAAA"

        self.outline_color = outline_color if outline_color is not None else "#000000"
        self.outline_thickness = outline_thickness


class DrawerData:
    def __init__(self,
                 resources: UnitData = None,
                 processes: UnitData = None,
                 vertical_spacing: int = 50) -> None:
        self.resources = resources if resources is not None else self.default_resources()
        self.processes = processes if processes is not None else self.default_processes()

        self.v_spacing = vertical_spacing

    @staticmethod
    def default_resources() -> UnitData:
        return UnitData()

    @staticmethod
    def default_processes() -> UnitData:
        return UnitData()
