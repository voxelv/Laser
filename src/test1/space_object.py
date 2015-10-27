import laser
import os


class SpaceObject:

    path = "resources/space_objects/"

    def __init__(self, pos):
        self.position = pos

        self.sprite_image_file = "default.png"
        self.sprite_image_path = os.path.join(self.path, self.sprite_image_file)


class ConnectibleSpaceObject(SpaceObject):

    connections = []
    resource_buffer = 0

    def add_connection(self, pos):
        self.connections.append(pos)

    def draw_connections(self):
        for conn in self.connections:
            # Draw each connection laser
            print conn

