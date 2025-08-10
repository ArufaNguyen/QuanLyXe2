import datetime
from Utils.day_pass import ghi_de
def to_time(username):
    # Cập nhật Day_Pass trong DB trước
    ghi_de(username)
    import pyodbc
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=localhost,1433;'
        'DATABASE=QuanLyXeDB;'
        'UID=sa;'
        'PWD=Aa123456'
    )
    cursor = conn.cursor()

    # Lấy Time_started và Day_Pass từ DB
    query = "SELECT Time_started, Day_Pass FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    row = cursor.fetchone()

    cursor.close()
    conn.close()
    now = datetime.datetime.now().time()
    nhours, nminutes, nseconds = map(float, str(now).split(':'))

    hours, minutes, seconds = map(float, str(row[0]).split(':'))
    def convert_to_hour(hours, minutes, seconds,day_pass):
        if day_pass == 0:
            total_seconds = hours * 3600 + minutes * 60 + seconds
            total_hours = total_seconds / 3600

            return round(total_hours,2)
        else:
            total_seconds = hours * 3600 + minutes * 60 + seconds + day_pass * 24 * 3600
            total_hours = total_seconds / 3600

            return round(total_hours,2)
    
    table = {
        'hours': nhours-hours,
        'minutes': nminutes-minutes,
        'seconds': nseconds-seconds,
        'Perfect_hour': convert_to_hour(nhours-hours, nminutes-minutes, nseconds-seconds, row[1]),
    }
    return table
# print(to_time("attendant1"))