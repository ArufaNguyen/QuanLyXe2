from Repositories.sql_server.vehicle_repository import VehicleRepository

class VehicleService:
    def __init__(self):
        self.vehicle_repo = VehicleRepository()

    def fetch_vehicle_info_from_api(self, url):
        # Gọi API để lấy ID xe và hình ảnh biển số
        result = self.vehicle_repo.hook(url)
        if result:
            ID_xe, plate_image_url = result
            return {
                "ID_xe": ID_xe,
                "plate_image_url": plate_image_url
            }
        return None

    def register_vehicle(self, ID_xe, plate_image_url):
        # Logic nghiệp vụ trước khi thêm xe
        if not ID_xe or not plate_image_url:
            return False
        return self.vehicle_repo.add_vehicle(ID_xe, plate_image_url)

    def close(self):
        self.vehicle_repo.close()
