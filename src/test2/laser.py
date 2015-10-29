import pygame


class Laser:
    def __init__(self, colors=('red', 'red2', 'white')):
        self.glow = [pygame.color.Color(color) for color in colors]

    def draw_laser(self, surface, start, stop, width):
        for color in self.glow:
            if width <= 0:
                break
            pygame.draw.line(surface, color, start, stop, width)
            width -= 5


