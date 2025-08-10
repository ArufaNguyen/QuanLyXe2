from Repositories.sql_server.parking_repository import ParkingRepository
from Repositories.sql_server.user_repository import AccountRepository

class ParkingService:
    def __init__(self):
        self.parking_repo = ParkingRepository()
        self.account_repo = AccountRepository()

    def get_available_slots(self):
        # Lấy danh sách slot còn trống
        return self.parking_repo.get_slot_available()

    def add_slot(self, username, slot):
        return self.parking_repo.parking_slot(username, "ADD", slot)

    def remove_slot(self, username, slot):
        return self.parking_repo.parking_slot(username, "POSTPONE", slot)

    def update_slot_status(self, slot, id_xe, on_slot):
        # Cập nhật thông tin slot: có xe hay không
        return self.parking_repo.update_slot(slot, id_xe, on_slot)

        