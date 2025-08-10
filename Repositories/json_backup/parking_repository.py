import os
from BackupData.backup import backup_table_to_json

class ParkingBackupRepository:
    OUTPUT_FOLDER = "Backup/Data"
    CONFIG_PATH = "Config/QuanLyXeDB.json"

    def __init__(self):
        os.makedirs(self.OUTPUT_FOLDER, exist_ok=True)

    def backup(self):
        backup_table_to_json("slot", self.CONFIG_PATH)
        print("[OK] Đã backup bảng 'slot' vào Backup/Data/slot.json")

# if __name__ == "__main__":
#     ParkingBackupRepository().backup()
