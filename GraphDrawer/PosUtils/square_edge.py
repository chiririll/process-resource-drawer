# https://stackoverflow.com/questions/58055629/intersection-between-a-line-and-square

def square_edge_intersection(square_pos: tuple[int, int],
                             square_size: tuple[int],
                             out_point: tuple[int, int]) -> tuple[int, int]:
    x0, y0 = square_pos[0], square_pos[1]
    ox, oy = out_point[0], out_point[1]

    w, h = square_size[0] // 2, square_size[1] // 2
    x1, y1 = x0 - w, y0 - h
    x2, y2 = x0 + w, y0 + h

    vx = ox - x0
    vy = oy - y0

    ex = x2 if vx > 0 else x1
    ey = y2 if vy > 0 else y1

    if vx == 0:
        return x0, ey
    if vy == 0:
        return ex, y0

    tx = (ex - x0) / vx
    ty = (ey - y0) / vy

    if tx <= ty:
        return ex, y0 + tx * vy
    return x0 + ty * vx, ey
