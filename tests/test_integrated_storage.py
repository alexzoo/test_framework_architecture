

from business.business_steps import BusinessSteps


class TestIntegratedStorage:

    def __init__(self) -> None:
        self.bussines_steps = BusinessSteps()

    def test_should_create_a_new_integrated_storage_with_datastore(self):
        # Arrange
        dev = "/dev/sda"
        # Act
        controller = self.bussines_steps.create_new_contoller()
        drive = self.bussines_steps.add_new_drive(dev)
        self.bussines_steps.format_drive(drive)
        self.bussines_steps.assign_drive_to_controller(controller, drive)
        datastore = self.bussines_steps.create_new_datastore(drive, controller)
        # Assert
        self.check_datastore(datastore)
