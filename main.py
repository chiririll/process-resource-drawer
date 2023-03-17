import ProcessDrawer


def main():
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

    drawer = ProcessDrawer.ProcessDrawer(len(res), len(proc))
    drawer.draw()


if __name__ == "__main__":
    main()
