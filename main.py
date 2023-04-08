import json

import GraphDrawer


def main():
    with open("config.json") as f:
        config = json.load(f)

    res = [
        [-1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, -1, 0, 0],
        [0, 1, 0, 0]
    ]
    proc = [
        [0, 0, -1, 0],
        [-1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1]
    ]

    drawer = GraphDrawer.GraphDrawer(config)
    dwg = drawer.draw(proc, res)
    dwg.saveas("images/example.svg")


if __name__ == "__main__":
    main()
