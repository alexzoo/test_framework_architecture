from business.model.controller import Controller
from business.model.datastore import Datastore
from business.model.device import Device
from business.model.nodes import Nodes


class IntegratedStorageService:

    def create_new_contoller(self, controller_id: int, slot: int) -> Controller:
        pass

    def format_device(self, device: Device) -> None:
        pass

    def assign_device_to_controller(self, device: Device, controller: Controller) -> None:
        pass

    def create_new_datastore(self, device: Device, controller: Controller, name: str, nodes: Nodes, replicas=1, copies=1) -> Datastore:
        pass

    def check_created_datastore(self, datastore: Datastore) -> None:
        pass
