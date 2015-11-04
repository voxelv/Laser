import pygame

__author__ = 'Tim'


class Network:
    def __init__(self, net_type):
        self.objects = NetworkObjectContainer()
        self.connections = []
        self.net_type = net_type

    def add_object(self, obj):
        self.objects.append(obj)

    def add_connection(self, obj1, obj1_slot, obj2, obj2_slot):
        self.connections.append(NetworkConnection(obj1, obj1_slot, obj2, obj2_slot))


class NetworkConnection:
    def __init__(self, obj1, obj1_slot, obj2, obj2_slot):
        self.slot1 = obj1.net_slots[obj1_slot]
        self.slot2 = obj2.net_slots[obj2_slot]

    def render_connection(self):
        pass


class NetworkObject:
    def __init__(self):
        self.ID = "UPDATE ID CODE WITH REGISTRY"
        self.slots = [Slot("center", "control", (0, 0), "inout")]

    def add_slot(self, slot_name, slot_type, rel_pos, flow_dir):
        self.slots.append(Slot(slot_name, slot_type, rel_pos, flow_dir))

    def render(self, surface):
        pass
        """ ADD STUFF HERE!!! """


class Slot:
    def __init__(self, slot_name, slot_type, rel_pos, flow_dir):
        self.name = slot_name
        self.type = slot_type
        self.position = rel_pos
        self.dir = flow_dir


class NetworkObjectContainer(list):
    def __init__(self, iterable=None):
        super(NetworkObjectContainer, self).__init__(iterable)

    def render_objects(self):
        for obj in self:
            obj.render()
