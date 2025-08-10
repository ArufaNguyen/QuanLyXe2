# import pyodbc

# # Kết nối tới database
# conn = pyodbc.connect(
#     'DRIVER={SQL Server};'
#     'SERVER=localhost,1433;'
#     'DATABASE=QuanLyXeDB;'
#     'UID=sa;'
#     'PWD=Aa123456'
# )
# cursor = conn.cursor()

# # Lấy dữ liệu
# cursor.execute("UPDATE slot SET On_Slot = ?, ID_xe = ? WHERE slot = ?", (1, 'doogshit', 5))

# # Cách 1: Duyệt từng dòng
# # for row in cursor.fetchall():
# #     print(row)

# # Cách 2: In tất cả một lúc
# # rows = cursor.fetchall()
# # print(rows)
# conn.commit()

# cursor.close()
# conn.close()
from datetime import datetime
from Repositories.sql_server import AccountRepository, ParkingRepository,DashboardDataRepository,VehicleRepository
slot = ParkingRepository().get_slot_available()
username = AccountRepository().account_has_no_slot()
now = datetime.now()
dashboard_data = AccountRepository().load_username_data()

for i in dashboard_data:
    if i.get("username") == "BansiCute":
        ID_xe = i.get('ID_xe')
        qr_code = i.get('qr_code')
        Time_used = i.get('Time_used')
        Time_started = i.get('Time_started')
        Day_started = i.get('Day_started')
        Day_Pass = i.get('Day_Pass')

print(AccountRepository().load_username_data())