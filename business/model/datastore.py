from business.model.device import Device
from business.model.nodes import Nodes


class Datastore:

    def __init__(self, device: Device, name: str, nodes: Nodes, replicas=1, copies=1):
        self.device = device
        self.id = None
        self.name = name
        self.replicas = replicas
        self.copies = copies
        self.nodes = nodes
