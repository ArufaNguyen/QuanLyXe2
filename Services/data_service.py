from Repositories.sql_server import DashboardDataRepository

class DashboardDataService:
    def __init__(self):
        self.repo = DashboardDataRepository()

    def get_dashboard_data(self):
        """Lấy toàn bộ dữ liệu dashboard"""
        return self.repo.load_dashboard_data()

    def get_element_value(self, element):
        """Lấy giá trị của 1 cột"""
        return self.repo.data_pull(element)

    def increment_element(self, element, value):
        """Tăng giá trị của cột element lên value"""
        if not isinstance(value, (int, float)):
            raise ValueError("Giá trị tăng phải là số")
        return self.repo.update(element, value)

    def decrement_element(self, element, value=1):
        """Giảm giá trị của cột element đi value"""
        if not isinstance(value, (int, float)):
            raise ValueError("Giá trị giảm phải là số")
        return self.repo.update(element, -value)

    def close(self):
        """Đóng kết nối DB"""
        self.repo.close()
