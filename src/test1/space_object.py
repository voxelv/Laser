import laser


class SpaceObject:

    connections = []

    def __init__(self, pos):
        self.position = pos


class ConnectibleSpaceObject(SpaceObject):

    def add_connection(self, pos):
        self.connections.append(pos)

    def draw_connections(self):
        for conn in self.connections:
            # Draw each connection laser
            print conn

