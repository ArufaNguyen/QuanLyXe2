import datetime
import json
def get_day_pass(username1):
    def load_users():
        with open('static/users.json') as f:
            return json.load(f)
    user = load_users()
    for user in user:
        if user.get('username') == username1:
            day = user.get('Day_started')
    nam,thang,ngay = map(int, day.split('-'))

    def convert_to_day(ngay, thang, nam): 
        today = str(datetime.date.today())
        curnam,curthang,curngay = map(int, today.split('-'))
        day_pass = 0
        passnam=curnam - nam
        passthang = curthang - thang
        passngay = curngay - ngay
        if passnam > 0:
            day_pass = day_pass + 365
        if passthang > 0:
            day_pass = day_pass + 30
        if passngay > 0:
            day_pass = day_pass + passngay
        return day_pass
    return convert_to_day(ngay, thang, nam)

def ghi_de(username1):
    with open('static/users.json', 'r', encoding='utf-8') as f:
        users = json.load(f)

    for user in users:
        if user['username'] == 'attendant1':
            user['Day_Pass'] = get_day_pass(username1) 
            break

    with open('static/users.json', 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=4, ensure_ascii=False)
# ghi_de('attendant1')