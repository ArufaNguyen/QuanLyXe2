import json
import datetime
from Utils.day_pass import ghi_de
def to_time(username1):
    ghi_de(username1)
    def load_users():
        with open('static/users.json') as f:
            return json.load(f)
    user = load_users()
    for user in user:
        if user.get('username') == username1:
            time= user.get('Time_started')
            day_pass = user.get('Day_Pass')
    hours, minutes, seconds = map(int, time.split(':'))
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
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
        'Perfect_hour': convert_to_hour(hours, minutes, seconds, day_pass),
    }
    return table

