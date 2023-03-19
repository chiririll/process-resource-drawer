import math


def circle_edge_intersection(center: tuple[int, int], r: int, dst: tuple[int, int]) -> tuple[int, int]:
    vx, vy = dst[0] - center[0], dst[1] - center[1]
    d = math.sqrt(pow(vx, 2) + pow(vy, 2))
    k = r / d

    return int(center[0] + vx * k), int(center[1] + vy * k)
