__author__ = 'Tim'


class Network:
    def __init__(self, net_type):
        self.objects = []
        self.connections = []
        self.net_type = net_type

    def add_object(self, obj):
        self.objects.append(obj)

    def add_cnxn(self, obj1, obj1_slot, obj2, obj2_slot):
        self.connections.append(NetworkConnection(obj1, obj1_slot, obj2, obj2_slot))


class NetworkConnection:
    def __init__(self, obj1, obj1_slot, obj2, obj2_slot):
        self.slot1 = obj1.net_slots[obj1_slot]
        self.slot2 = obj2.net_slots[obj2_slot]


class NetworkObject:
    def __init__(self, obj_type, pos):
        self.ID = "UPDATE ID CODE WITH REGISTRY"
        self.slots = []

    def add_slot(self, slot):
        self.slots.append(slot)


class Slot:
    def __init__(self, slot_type, pos, dir):
        self.type = slot_type
        self.position = pos
        self.dir = dir
