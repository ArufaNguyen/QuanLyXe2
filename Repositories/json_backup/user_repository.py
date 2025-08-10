import os
from BackupData.backup import backup_table_to_json

class UserBackupRepository:
    OUTPUT_FOLDER = "Backup/Data"
    CONFIG_PATH = "Config/QuanLyXeDB.json"

    def __init__(self):
        os.makedirs(self.OUTPUT_FOLDER, exist_ok=True)

    def backup(self):
        backup_table_to_json("users", self.CONFIG_PATH)
        print("[OK] Đã backup bảng 'users' vào Backup/Data/users.json")

# if __name__ == "__main__":
#     UserBackupRepository().backup()
