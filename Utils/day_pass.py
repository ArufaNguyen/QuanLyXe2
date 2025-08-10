import datetime
import pyodbc

def get_day_pass(username):
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=localhost,1433;'
        'DATABASE=QuanLyXeDB;'
        'UID=sa;'
        'PWD=Aa123456'
    )
    cursor = conn.cursor()
    query = "SELECT Day_started FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    row = cursor.fetchone()

    if not row or not row[0]:
        cursor.close()
        conn.close()
        return 0

    day_started = row[0]
    if day_started !="NULL":
        if isinstance(day_started, datetime.datetime) or isinstance(day_started, datetime.date):
            day_date = day_started.date() if isinstance(day_started, datetime.datetime) else day_started
        else:
            day_date = datetime.datetime.strptime(day_started, '%Y-%m-%d').date()
                    
        today = datetime.date.today()
        day_pass = (today - day_date).days

        cursor.close()
        conn.close()

        return day_pass
    else:
        
        return 0
        


def ghi_de(username):
    day_pass = get_day_pass(username)
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=localhost,1433;'
        'DATABASE=QuanLyXeDB;'
        'UID=sa;'
        'PWD=Aa123456'
    )
    cursor = conn.cursor()
    query = "UPDATE users SET Day_Pass = ? WHERE username = ?"
    cursor.execute(query, (day_pass, username))
    conn.commit()
    cursor.close()
    conn.close()
