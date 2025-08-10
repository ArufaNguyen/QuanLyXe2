import pyodbc
from Database import SQL_connect
from datetime import datetime
from Repositories.sql_server.parking_repository import ParkingRepository 
from Repositories.sql_server.user_repository import AccountRepository 
import requests
class VehicleRepository:
    def __init__(self):
        self.conn = SQL_connect("Config/QuanLyXeDB.json")
        self.cursor = self.conn.cursor()
    def hook(self,url):
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            ID_xe = data.get("ID_xe")
            plate_image_url = data.get("plate_image_url")
            return ID_xe,plate_image_url
        return False

    def add_vehicle(self,ID_xe,plate_image_url):
        now = datetime.now()
        username = AccountRepository().account_has_no_slot()
        slot = ParkingRepository().get_slot_available()
        if len(username)>0 and len(slot)>0:
            query = f"""
                UPDATE users
                SET ID_xe ='{ID_xe}', Time_started = '{str(now.time())}', Day_started = '{str(now.date())}',plate_image_url = '{plate_image_url}',On_slot = 1,Slot_used = {slot[0]}
                WHERE username = '{username[0]}'
            """
            
            self.cursor.execute(query)
            self.conn.commit()
            ParkingRepository().update_slot(slot[0],ID_xe)
            return True
        return False

    def close(self):
        self.cursor.close()
        self.conn.close()