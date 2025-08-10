
import pyodbc
from Database import SQL_connect
from Utils.Qr_Gen import gen
class AccountRepository:
    def __init__(self):
        self.conn = SQL_connect("Config/QuanLyXeDB.json")
        self.cursor = self.conn.cursor()
    
    def authenticate(self,username,password):
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        self.cursor.execute(query)
        row = self.cursor.fetchall()
        if row:
            return True
        return False
    
    def is_used(self,username):
        query = f"SELECT * FROM users WHERE username = '{username}'"
        self.cursor.execute(query)
        row = self.cursor.fetchall()
        if row:
            return True
        return False
    
    def is_admin(self, username):
        query = f"SELECT * FROM users WHERE username = '{username}' AND role = 'admin'"
        self.cursor.execute(query)
        row = self.cursor.fetchall()
        if row:
            return True
        return False

    def is_owner(self,username):
        query = f"SELECT * FROM users WHERE username = '{username}' AND role = 'owner'"
        self.cursor.execute(query)
        row = self.cursor.fetchall()
        if row:
            return True
        return False
    
    def create_account(self,username,password,role,requirement_role):
        if self.is_owner(username) and self.is_used(username) == False:
            query = f"INSERT INTO users (username, password, role,qr_code) VALUES('{username}','{password}','{role}','{gen(username)}')"
            self.cursor.execute(query)
            self.conn.commit()
            return True
        return False
    
    def account_has_no_slot(self):
        query = f"SELECT username FROM users WHERE On_Slot = 0" #0 = false car 
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        slots = [row[0] for row in rows]
        return slots
    
    def reset_user_status(self, username: str) -> bool:
        query = """
            UPDATE users SET
                ID_xe = 'NULL',
                Time_used = 0,
                Time_started = 'NULL',
                Day_started = 'NULL',
                Day_Pass = 0,
                Slot_used = 0,
                On_slot = 0
            WHERE username = ?
        """
        self.cursor.execute(query, (username,))
        self.conn.commit()
        return True
    def load_username_data(self):
        query = "SELECT * FROM users"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        columns = [col[0] for col in self.cursor.description]  # Lấy tên cột từ description
        results = []
        for row in rows:
            # row là tuple giá trị
            # columns là list tên cột
            record = {}
            for col_name, value in zip(columns, row):
                record[col_name] = value
            results.append(record)
        return results
    def close(self):
        self.cursor.close()
        self.conn.close()