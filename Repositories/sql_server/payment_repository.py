import pyodbc
from Database import SQL_connect
from datetime import datetime

class PaymentRepository:
    def __init__(self):
        self.conn = SQL_connect("Config/QuanLyXeDB.json")
        self.cursor = self.conn.cursor()
    
    def add_payment(self, username: str, amount: float, car_code: str, plate_image_url: str) -> bool:
        try:
            now = datetime.now()
            query = """
                INSERT INTO data (account, amount, car_code, time, plate_image_url)
                VALUES (?, ?, ?, ?, ?)
            """
            self.cursor.execute(query, (username, amount, car_code, now, plate_image_url))
            self.conn.commit()
            return True
        except Exception as e:
            print("Error inserting payment:", e)
            return False
    
    def close(self):
        self.cursor.close()
        self.conn.close()
