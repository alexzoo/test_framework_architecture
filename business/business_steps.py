class BusinessSteps:

    def __init__(self) -> None:
        self.controller = Controller()
        self.drive = Drive()
        self.datastore = Datastore()

    def create_new_contoller(self) -> Controller:
        controller = self.controller
        return controller

    def add_new_drive(self, dev: str) -> Drive:
        drive = self.drive(dev)
        return drive

    def format_drive(self, drive: Drive) -> None:
        drive.format()

    def assign_drive_to_controller(self, controller: Controller, drive: Drive) -> None:
        controller.add_drive(drive)

    def create_new_datastore(self, drive: Drive, controller: Controller) -> Datastore:
        datastore = self.datastore(drive, controller)
        return datastore

    def check_datastore(self, datastore: Datastore) -> None:
        assert datastore.drive is not None
        assert datastore.controller is not None
