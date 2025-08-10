
import pyodbc
from Database import SQL_connect
from Repositories.sql_server.user_repository import AccountRepository
class ParkingRepository:
    def __init__(self):
        self.conn = SQL_connect("Config/QuanLyXeDB.json")
        self.cursor = self.conn.cursor()

    def get_slot_available(self):
        query = f"SELECT slot FROM slot WHERE On_Slot = 0" #0 = false car 
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        slots = [row[0] for row in rows]
        return slots
    
    def already_slot(self,slot):
        query = f"SELECT slot FROM slot WHERE slot = {slot}" #0 = false car 
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        slots = rows is not None

        return slots 
    
    def update_slot(self,slot,ID_xe):
        query = f"UPDATE slot SET On_Slot = 1, ID_xe = '{ID_xe}' WHERE slot = {slot}"
        self.cursor.execute(query)
        self.conn.commit()

    def parking_slot(self,username,action,slot):
        if AccountRepository().is_admin(username) or AccountRepository().is_owner(username):
            if action == "ADD" and self.already_slot(slot) == False:
                query = f"INSERT INTO slot (slot, ID_xe, On_Slot) VALUES('{slot}','NULL',0)"
                self.cursor.execute(query)
                self.conn.commit()
                return True
            elif action == "POSTPONE" and self.already_slot(slot)== True:
                query = f"DELETE FROM slot WHERE slot ={slot}"
                self.cursor.execute(query)
                self.conn.commit()
                return True
            return False
        return False
    
    def close(self):
        self.cursor.close()
        self.conn.close()
