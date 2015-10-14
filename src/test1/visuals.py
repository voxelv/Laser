import pygame


class Laser:
    def __init__(self, colors=('red', 'red2', 'white')):
        self.glow = [pygame.color.THECOLORS[color] for color in colors]

    def draw_laser(self, surface, start, stop, magnitude):
        width = magnitude
        for color in self.glow:
            if width <= 0:
                break
            pygame.draw.line(surface, color, start, stop, width)
            width -= 2


class Visuals:

    max_width = 700
    max_height = 500
    size = (max_width, max_height)

    whiteColor = (255, 255, 255)
    bgColor = (0, 0, 0)
    redLaser = Laser(['red4', 'red', 'white'])
    blueLaser = Laser(['blue', 'blue2', 'white'])

    def __init__(self):
        pass
