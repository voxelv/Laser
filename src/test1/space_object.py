import pygame
import laser
import math
import os
import random as rand


class SpaceObject:

    path = "resources/space_objects/"

    def __init__(self, game, pos, color):
        self.position = [pos[0], pos[1]]
        self.game = game
        self.color_name = color
        self.color = pygame.color.Color(color)

        self.sprite_image_file = "default.png"
        self.sprite_image_path = os.path.join(self.path, self.sprite_image_file)

    def in_range(self, pos, distance):
        return self.dist(pos, self.position) <= distance

    def dist(self, pos1, pos2):
        return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)


class ConnectibleSpaceObject(SpaceObject):

    def __init__(self, game, pos, color, laser_type):
        SpaceObject.__init__(self, game, pos, color)
        self.resource_buffer = 0
        self.connections = []
        self.laser = laser_type

    def rand_move(self, dist):
        r = rand.randint(0, 3)

        if r == 0:
            self.position[0] += dist
        elif r == 1:
            self.position[0] -= dist
        elif r == 2:
            self.position[1] += dist
        elif r == 3:
            self.position[1] -= dist

        if self.position[0] > self.game.visual_set.max_width:
            self.position[0] = 0

        if self.position[0] < 0:
            self.position[0] = self.game.visual_set.max_width

        if self.position[1] > self.game.visual_set.max_height:
            self.position[1] = 0

        if self.position[1] < 0:
            self.position[1] = self.game.visual_set.max_height

        for obj in self.game.sobjects:
            if self.in_range(obj.position, 20) and self.color_name != obj.color_name:
                self.color_name = obj.color_name
                self.color = pygame.color.Color(obj.color_name)


    def add_connection(self, pos):
        self.connections.append(pos)

    def recalculate_connections(self, min_range, max_range):
        self.connections = []
        for obj in self.game.sobjects:
            if self.in_range(obj.position, min_range):
                continue
            if self.color_name != obj.color_name:
                continue
            if self.in_range(obj.position, max_range):
                self.add_connection(obj.position)

    def draw_connections(self):
        for conn in self.connections:
            # Draw each connection laser
            self.laser.draw_laser(self.game.screen, self.position, conn, 5)

    def render(self):
        pygame.draw.circle(self.game.screen, self.color, self.position, 5, 0)
