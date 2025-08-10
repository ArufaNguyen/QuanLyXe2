import pyodbc
from Database import SQL_connect
class DashboardDataRepository:
    def __init__(self):
        self.conn = SQL_connect("Config/QuanLyXeDB.json")
        self.cursor = self.conn.cursor()
    def data_pull(self,element):
        query = f"SELECT {element} FROM dashboard_data" #0 = false car 
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        slots = [row[0] for row in rows]
        return slots[0]

    def update(self,element,value):
        values = self.data_pull(element) +value
        query = f"UPDATE dashboard_data SET {element} = {values}"
        self.cursor.execute(query)
        self.conn.commit()
        return True
    def close(self):
        self.cursor.close()
        self.conn.close()