import pygame
import laser
import math
import os


class SpaceObject:

    path = "resources/space_objects/"

    def __init__(self, pos):
        self.position = pos

        self.sprite_image_file = "default.png"
        self.sprite_image_path = os.path.join(self.path, self.sprite_image_file)

    def in_range(self, pos, distance):
        return self.dist(pos, self.position) <= distance

    def dist(self, pos1, pos2):
        return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)


class ConnectibleSpaceObject(SpaceObject):

    def __init__(self, pos):
        SpaceObject.__init__(self, pos)
        self.resource_buffer = 0
        self.connections = []

    def add_connection(self, pos):
        self.connections.append(pos)

    def draw_connections(self, game):
        for conn in self.connections:
            # Draw each connection laser
            laser.Laser().draw_laser(game.screen, self.position, conn, 5)

    def render(self, game):
        pygame.draw.circle(game.screen, pygame.color.THECOLORS["green"], self.position, 5, 0)
