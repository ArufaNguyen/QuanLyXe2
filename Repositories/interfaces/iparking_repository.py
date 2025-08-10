from abc import ABC, abstractmethod

class IParkingRepository(ABC):
    @abstractmethod
    def get_slot_available(self):
        """Trả về danh sách các slot còn trống"""
        pass

    @abstractmethod
    def update_slot(self, slot, ID_xe):
        """Cập nhật thông tin slot với biển số xe"""
        pass
    @abstractmethod
    def already_slot(self,slot):
        pass
    @abstractmethod
    def parking_slot(self,username,action,slot):
        pass
    @abstractmethod
    def close(self):
        """Đóng kết nối nếu cần"""
        pass
