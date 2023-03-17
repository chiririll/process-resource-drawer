import json

import ProcessDrawer


def main():
    with open("config.json") as f:
        config = json.load(f)

    res = [
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1]
    ]
    proc = [
        [0, 0, 0, 1],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0]
    ]

    #drawer = ProcessDrawer.ProcessDrawer(len(res), len(proc))
    drawer = ProcessDrawer.ConfigDrawer(config)
    drawer.draw(proc, res)


if __name__ == "__main__":
    main()
