import os
from BackupData.backup import backup_table_to_json

class VehicleBackupRepository:
    OUTPUT_FOLDER = "Backup/Data"
    CONFIG_PATH = "Config/QuanLyXeDB.json"

    def __init__(self):
        os.makedirs(self.OUTPUT_FOLDER, exist_ok=True)

    def backup(self):
        backup_table_to_json("data", self.CONFIG_PATH)
        backup_table_to_json("dashboard_data", self.CONFIG_PATH)

        print("[OK] Đã backup bảng 'xe_logger' vào Backup/Data/data.json")
        print("[OK] Đã backup bảng 'xe_logger' vào Backup/Data/ashboard_data.json")
        

if __name__ == "__main__":
    VehicleBackupRepository().backup()
