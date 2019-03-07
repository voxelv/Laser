import laser as lsr


class Visuals:

    max_width = 1000
    max_height = 1000
    size = (max_width, max_height)

    whiteColor = (255, 255, 255)
    bgColor = (0, 0, 0)
    redLaser = lsr.Laser(['red4', 'red', 'white'])
    blueLaser = lsr.Laser(['blue', 'blue2', 'white'])
    greenLaser = lsr.Laser(['forestgreen', 'limegreen', 'white'])
    yellowLaser = lsr.Laser(['goldenrod', 'yellow', 'white'])

    def __init__(self):
        pass







