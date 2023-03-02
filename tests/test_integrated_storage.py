from business.integrated_storage_service import IntegratedStorageService
from business.model.device import Device
from business.model.nodes import Nodes


class TestIntegratedStorage:

    def test_should_create_a_new_integrated_storage_with_datastore(self):
        # Arrange
        integrated_storage_service = IntegratedStorageService()
        device = Device(dev="/dev/sda", size=1000)
        nodes = Nodes()

        # Act
        controller = integrated_storage_service.create_new_contoller(
            controller_id=0, slot=0)

        integrated_storage_service.format_device(device)
        integrated_storage_service.assign_device_to_controller(
            device, controller)
        datastore = integrated_storage_service.create_new_datastore(
            device, controller, name="datastore1", nodes=nodes, replicas=1, copies=1)

        # Assert
        integrated_storage_service.check_created_datastore(datastore)
